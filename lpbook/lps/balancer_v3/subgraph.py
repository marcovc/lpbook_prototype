from sgqlc.operation import Operation
from .artifacts.graphql_schema import graphql_schema as schema

from lpbook.thegraph.subgraph import GraphQLClient

from functools import partial

import aiohttp


class BalancerV3GraphQLClient(GraphQLClient):
    def __init__(self, url: str, session: aiohttp.ClientSession):
        self.url = url
        super().__init__(self.url, session)

    def set_pool_id_and_tokens_fields(self, pool):
        pool.id()
        pool.pool_tokens().address()
        pool.pool_tokens().symbol()
        pool.pool_tokens().decimals()
        pool.pool_tokens().balance()
        pool.pool_tokens().weight()
        pool.hook()
        pool.swap_fee_manager()

    def set_pool_state_fields(self, pool):
        self.set_pool_id_and_tokens_fields(pool)
        pool.type()
        pool.dynamic_data().swap_fee()

    async def get_pools_page(self, pools_filter, field_setter, last_id, first, **kwargs):
        op = Operation(schema.Query)
        pools_filter = {**pools_filter}
        if last_id is not None:
            pools_filter.update({'id_gt': last_id})

        pools = op.pool_get_pools(
            where=pools_filter,
            first=first,
            **kwargs
        )

        if field_setter is None:
            field_setter = self.set_pool_state_fields

        field_setter(pools)

        data = await self.get_data(op, 'poolGetPools')
        query = op + data
        return query.pool_get_pools if hasattr(query, 'pool_get_pools') else []

    def get_pools_state(self, pools_filter=dict(), field_setter=None, **kwargs):
        return self.paginated_on_id(
            partial(self.get_pools_page, pools_filter, field_setter, **kwargs)
        )

    async def get_last_block_number(self):
        op = Operation(schema.Query)
        latest_synced_blocks = op.latest_synced_blocks()
        latest_synced_blocks.pool_sync_block()
        data = await self.get_data(op, 'latestSyncedBlocks')
        query = op + data
        return int(query.latest_synced_blocks.pool_sync_block) if hasattr(query, 'latest_synced_blocks') else None

    async def get_aggregator_pools_page(self, pool_tokens_filter, last_id, first, **kwargs):
        op = Operation(schema.Query)
        pool_tokens_filter = {**pool_tokens_filter}
        if last_id is not None:
            pool_tokens_filter.update({'id_gt': last_id})

        aggregator_pools = op.aggregator_pools(
            where=pool_tokens_filter,
            first=first,
            **kwargs
        )

        aggregator_pools.id()
        aggregator_pools.pool_tokens().address()

        data = await self.get_data(op, 'aggregatorPools')
        query = op + data
        return query.aggregator_pools if hasattr(query, 'aggregator_pools') else []

    async def get_pools_containing_tokens(self, token_ids, pool_types, min_tvl, **kwargs):
        def accept_pool(pool):
            return sum(token.address in token_ids for token in pool.pool_tokens) >= 2        
        return {
            pool async for pool in self.paginated_on_id(
            partial(self.get_aggregator_pools_page, {
                "protocol_version_in": [3], 
                "pool_type_in": pool_types, 
                "min_tvl": min_tvl,
                "chain_in": ["MAINNET"]
            }, **kwargs)
            ) if accept_pool(pool)
        }
