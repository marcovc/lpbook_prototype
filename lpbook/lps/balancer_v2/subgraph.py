from sgqlc.operation import Operation
from .artifacts.graphql_schema import graphql_schema as schema

from lpbook.thegraph.subgraph import GraphQLClient

from functools import partial

import aiohttp


class BalancerV2GraphQLClient(GraphQLClient):
    def __init__(self, url: str, session: aiohttp.ClientSession):
        self.url = url
        super().__init__(self.url, session)

    def set_pool_id_and_tokens_fields(self, pool):
        pool.id()
        pool.tokens().address()
        pool.tokens().symbol()
        pool.tokens().decimals()
        pool.tokens().balance()
        pool.tokens().weight()

    def set_pool_state_fields(self, pool):
        self.set_pool_id_and_tokens_fields(pool)
        pool.pool_type()
        pool.swap_fee()

    async def get_pools_page(self, pools_filter, field_setter, last_id, first, **kwargs):
        op = Operation(schema.Query)
        pools_filter = {**pools_filter}
        if last_id is not None:
            pools_filter.update({'id_gt': last_id})

        pools = op.pools(
            where=pools_filter,
            first=first,
            **kwargs
        )

        if field_setter is None:
            field_setter = self.set_pool_state_fields

        field_setter(pools)

        data = await self.get_data(op, 'pools')
        query = op + data
        return query.pools if hasattr(query, 'pools') else []

    def get_pools_state(self, pools_filter=dict(), field_setter=None, **kwargs):
        return self.paginated_on_id(
            partial(self.get_pools_page, pools_filter, field_setter, **kwargs)
        )

    async def get_last_block(self):
        op = Operation(schema.Query)
        meta = op._meta()
        meta.block()
        meta.block().number()
        meta.block().hash()
        data = await self.get_data(op, '_meta')
        query = op + data
        return query._meta.block if hasattr(query, '_meta') else None

    async def get_pool_tokens_page(self, pool_tokens_filter, last_id, first, **kwargs):
        op = Operation(schema.Query)
        pool_tokens_filter = {**pool_tokens_filter}
        if last_id is not None:
            pool_tokens_filter.update({'id_gt': last_id})

        pool_tokens = op.pool_tokens(
            where=pool_tokens_filter,
            first=first,
            **kwargs
        )

        pool_tokens.id()
        pool_tokens.pool_id().id()
        pool_tokens.pool_id().pool_type()
        pool_tokens.pool_id().swap_enabled()
        pool_tokens.pool_id().is_paused()
        pool_tokens.pool_id().total_liquidity()
        #poolTokens.pool_id().tokens().address()

        data = await self.get_data(op, 'poolTokens')
        query = op + data
        return query.pool_tokens if hasattr(query, 'pool_tokens') else []

    async def get_pools_containing_tokens(self, token_addresses, **kwargs):
        return {
            pool_token.pool_id async for pool_token in self.paginated_on_id(
            partial(self.get_pool_tokens_page, {"address_in": token_addresses}, **kwargs)
        )}
