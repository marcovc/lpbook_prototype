from sgqlc.operation import Operation
from .artifacts.graphql_schema import graphql_schema as schema

from lpbook.thegraph.subgraph import GraphQLClient

from functools import partial

import aiohttp

from dotenv import load_dotenv
import os

load_dotenv()
THEGRAPH_API_KEY = os.getenv("THEGRAPH_API_KEY")

class CurveGraphQLClient(GraphQLClient):
    url = f'https://gateway-arbitrum.network.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/3fy93eAT56UJsRCEht8iFhfi6wjHWXtZ9dnnbQmvFopF'
    
    def __init__(self, session: aiohttp.ClientSession):
        super().__init__(self.url, session)

    def set_pool_state_fields(self, pool):
        pool.id()
        pool.input_tokens().id()

    def set_pool_id_field(self, pool):
        pool.id()

    async def get_pools_page(self, pools_filter, field_setter, last_id, first, **kwargs):
        op = Operation(schema.Query)
        pools_filter = {**pools_filter}
        if last_id is not None:
            pools_filter.update({'id_gt': last_id})

        pools = op.liquidity_pools(
            where=pools_filter,
            first=first,
            **kwargs
        )

        if field_setter is None:
            field_setter = self.set_pool_state_fields

        field_setter(pools)

        data = await self.get_data(op, 'liquidityPools')
        query = op + data
        return query.liquidity_pools if hasattr(query, 'liquidity_pools') else []

    def get_pools_state(self, pools_filter=dict(), field_setter=None, **kwargs):
        return self.paginated_on_id(
            partial(self.get_pools_page, pools_filter, field_setter, **kwargs)
        )
