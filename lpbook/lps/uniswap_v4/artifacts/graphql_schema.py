import sgqlc.types


graphql_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class Aggregation_interval(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('day', 'hour')


class BigDecimal(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = graphql_schema


Boolean = sgqlc.types.Boolean

class Bundle_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('ethPriceUSD', 'id')


class Bytes(sgqlc.types.Scalar):
    __schema__ = graphql_schema


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class Int8(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class ModifyLiquidity_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('amount', 'amount0', 'amount1', 'amountUSD', 'id', 'logIndex', 'origin', 'pool', 'pool__collectedFeesToken0', 'pool__collectedFeesToken1', 'pool__collectedFeesUSD', 'pool__createdAtBlockNumber', 'pool__createdAtTimestamp', 'pool__feeTier', 'pool__feesUSD', 'pool__hooks', 'pool__id', 'pool__liquidity', 'pool__liquidityProviderCount', 'pool__observationIndex', 'pool__sqrtPrice', 'pool__tick', 'pool__tickSpacing', 'pool__token0Price', 'pool__token1Price', 'pool__totalValueLockedETH', 'pool__totalValueLockedToken0', 'pool__totalValueLockedToken1', 'pool__totalValueLockedUSD', 'pool__totalValueLockedUSDUntracked', 'pool__txCount', 'pool__untrackedVolumeUSD', 'pool__volumeToken0', 'pool__volumeToken1', 'pool__volumeUSD', 'sender', 'tickLower', 'tickUpper', 'timestamp', 'token0', 'token0__decimals', 'token0__derivedETH', 'token0__feesUSD', 'token0__id', 'token0__name', 'token0__poolCount', 'token0__symbol', 'token0__totalSupply', 'token0__totalValueLocked', 'token0__totalValueLockedUSD', 'token0__totalValueLockedUSDUntracked', 'token0__txCount', 'token0__untrackedVolumeUSD', 'token0__volume', 'token0__volumeUSD', 'token1', 'token1__decimals', 'token1__derivedETH', 'token1__feesUSD', 'token1__id', 'token1__name', 'token1__poolCount', 'token1__symbol', 'token1__totalSupply', 'token1__totalValueLocked', 'token1__totalValueLockedUSD', 'token1__totalValueLockedUSDUntracked', 'token1__txCount', 'token1__untrackedVolumeUSD', 'token1__volume', 'token1__volumeUSD', 'transaction', 'transaction__blockNumber', 'transaction__gasPrice', 'transaction__gasUsed', 'transaction__id', 'transaction__timestamp')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('asc', 'desc')


class PoolDayData_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('close', 'date', 'feesUSD', 'high', 'id', 'liquidity', 'low', 'open', 'pool', 'pool__collectedFeesToken0', 'pool__collectedFeesToken1', 'pool__collectedFeesUSD', 'pool__createdAtBlockNumber', 'pool__createdAtTimestamp', 'pool__feeTier', 'pool__feesUSD', 'pool__hooks', 'pool__id', 'pool__liquidity', 'pool__liquidityProviderCount', 'pool__observationIndex', 'pool__sqrtPrice', 'pool__tick', 'pool__tickSpacing', 'pool__token0Price', 'pool__token1Price', 'pool__totalValueLockedETH', 'pool__totalValueLockedToken0', 'pool__totalValueLockedToken1', 'pool__totalValueLockedUSD', 'pool__totalValueLockedUSDUntracked', 'pool__txCount', 'pool__untrackedVolumeUSD', 'pool__volumeToken0', 'pool__volumeToken1', 'pool__volumeUSD', 'sqrtPrice', 'tick', 'token0Price', 'token1Price', 'tvlUSD', 'txCount', 'volumeToken0', 'volumeToken1', 'volumeUSD')


class PoolHourData_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('close', 'feesUSD', 'high', 'id', 'liquidity', 'low', 'open', 'periodStartUnix', 'pool', 'pool__collectedFeesToken0', 'pool__collectedFeesToken1', 'pool__collectedFeesUSD', 'pool__createdAtBlockNumber', 'pool__createdAtTimestamp', 'pool__feeTier', 'pool__feesUSD', 'pool__hooks', 'pool__id', 'pool__liquidity', 'pool__liquidityProviderCount', 'pool__observationIndex', 'pool__sqrtPrice', 'pool__tick', 'pool__tickSpacing', 'pool__token0Price', 'pool__token1Price', 'pool__totalValueLockedETH', 'pool__totalValueLockedToken0', 'pool__totalValueLockedToken1', 'pool__totalValueLockedUSD', 'pool__totalValueLockedUSDUntracked', 'pool__txCount', 'pool__untrackedVolumeUSD', 'pool__volumeToken0', 'pool__volumeToken1', 'pool__volumeUSD', 'sqrtPrice', 'tick', 'token0Price', 'token1Price', 'tvlUSD', 'txCount', 'volumeToken0', 'volumeToken1', 'volumeUSD')


class PoolManager_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'owner', 'poolCount', 'totalFeesETH', 'totalFeesUSD', 'totalValueLockedETH', 'totalValueLockedETHUntracked', 'totalValueLockedUSD', 'totalValueLockedUSDUntracked', 'totalVolumeETH', 'totalVolumeUSD', 'txCount', 'untrackedVolumeUSD')


class Pool_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('collectedFeesToken0', 'collectedFeesToken1', 'collectedFeesUSD', 'createdAtBlockNumber', 'createdAtTimestamp', 'feeTier', 'feesUSD', 'hooks', 'id', 'liquidity', 'liquidityProviderCount', 'modifyLiquiditys', 'observationIndex', 'poolDayData', 'poolHourData', 'sqrtPrice', 'swaps', 'tick', 'tickSpacing', 'ticks', 'token0', 'token0Price', 'token0__decimals', 'token0__derivedETH', 'token0__feesUSD', 'token0__id', 'token0__name', 'token0__poolCount', 'token0__symbol', 'token0__totalSupply', 'token0__totalValueLocked', 'token0__totalValueLockedUSD', 'token0__totalValueLockedUSDUntracked', 'token0__txCount', 'token0__untrackedVolumeUSD', 'token0__volume', 'token0__volumeUSD', 'token1', 'token1Price', 'token1__decimals', 'token1__derivedETH', 'token1__feesUSD', 'token1__id', 'token1__name', 'token1__poolCount', 'token1__symbol', 'token1__totalSupply', 'token1__totalValueLocked', 'token1__totalValueLockedUSD', 'token1__totalValueLockedUSDUntracked', 'token1__txCount', 'token1__untrackedVolumeUSD', 'token1__volume', 'token1__volumeUSD', 'totalValueLockedETH', 'totalValueLockedToken0', 'totalValueLockedToken1', 'totalValueLockedUSD', 'totalValueLockedUSDUntracked', 'txCount', 'untrackedVolumeUSD', 'volumeToken0', 'volumeToken1', 'volumeUSD')


class Position_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('createdAtTimestamp', 'id', 'origin', 'owner', 'subscriptions', 'tokenId', 'transfers', 'unsubscriptions')


String = sgqlc.types.String

class Subscribe_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'id', 'logIndex', 'origin', 'position', 'position__createdAtTimestamp', 'position__id', 'position__origin', 'position__owner', 'position__tokenId', 'timestamp', 'tokenId', 'transaction', 'transaction__blockNumber', 'transaction__gasPrice', 'transaction__gasUsed', 'transaction__id', 'transaction__timestamp')


class Swap_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('amount0', 'amount1', 'amountUSD', 'id', 'logIndex', 'origin', 'pool', 'pool__collectedFeesToken0', 'pool__collectedFeesToken1', 'pool__collectedFeesUSD', 'pool__createdAtBlockNumber', 'pool__createdAtTimestamp', 'pool__feeTier', 'pool__feesUSD', 'pool__hooks', 'pool__id', 'pool__liquidity', 'pool__liquidityProviderCount', 'pool__observationIndex', 'pool__sqrtPrice', 'pool__tick', 'pool__tickSpacing', 'pool__token0Price', 'pool__token1Price', 'pool__totalValueLockedETH', 'pool__totalValueLockedToken0', 'pool__totalValueLockedToken1', 'pool__totalValueLockedUSD', 'pool__totalValueLockedUSDUntracked', 'pool__txCount', 'pool__untrackedVolumeUSD', 'pool__volumeToken0', 'pool__volumeToken1', 'pool__volumeUSD', 'sender', 'sqrtPriceX96', 'tick', 'timestamp', 'token0', 'token0__decimals', 'token0__derivedETH', 'token0__feesUSD', 'token0__id', 'token0__name', 'token0__poolCount', 'token0__symbol', 'token0__totalSupply', 'token0__totalValueLocked', 'token0__totalValueLockedUSD', 'token0__totalValueLockedUSDUntracked', 'token0__txCount', 'token0__untrackedVolumeUSD', 'token0__volume', 'token0__volumeUSD', 'token1', 'token1__decimals', 'token1__derivedETH', 'token1__feesUSD', 'token1__id', 'token1__name', 'token1__poolCount', 'token1__symbol', 'token1__totalSupply', 'token1__totalValueLocked', 'token1__totalValueLockedUSD', 'token1__totalValueLockedUSDUntracked', 'token1__txCount', 'token1__untrackedVolumeUSD', 'token1__volume', 'token1__volumeUSD', 'transaction', 'transaction__blockNumber', 'transaction__gasPrice', 'transaction__gasUsed', 'transaction__id', 'transaction__timestamp')


class Tick_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('createdAtBlockNumber', 'createdAtTimestamp', 'id', 'liquidityGross', 'liquidityNet', 'pool', 'poolAddress', 'pool__collectedFeesToken0', 'pool__collectedFeesToken1', 'pool__collectedFeesUSD', 'pool__createdAtBlockNumber', 'pool__createdAtTimestamp', 'pool__feeTier', 'pool__feesUSD', 'pool__hooks', 'pool__id', 'pool__liquidity', 'pool__liquidityProviderCount', 'pool__observationIndex', 'pool__sqrtPrice', 'pool__tick', 'pool__tickSpacing', 'pool__token0Price', 'pool__token1Price', 'pool__totalValueLockedETH', 'pool__totalValueLockedToken0', 'pool__totalValueLockedToken1', 'pool__totalValueLockedUSD', 'pool__totalValueLockedUSDUntracked', 'pool__txCount', 'pool__untrackedVolumeUSD', 'pool__volumeToken0', 'pool__volumeToken1', 'pool__volumeUSD', 'price0', 'price1', 'tickIdx')


class Timestamp(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class TokenDayData_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('close', 'date', 'feesUSD', 'high', 'id', 'low', 'open', 'priceUSD', 'token', 'token__decimals', 'token__derivedETH', 'token__feesUSD', 'token__id', 'token__name', 'token__poolCount', 'token__symbol', 'token__totalSupply', 'token__totalValueLocked', 'token__totalValueLockedUSD', 'token__totalValueLockedUSDUntracked', 'token__txCount', 'token__untrackedVolumeUSD', 'token__volume', 'token__volumeUSD', 'totalValueLocked', 'totalValueLockedUSD', 'untrackedVolumeUSD', 'volume', 'volumeUSD')


class TokenHourData_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('close', 'feesUSD', 'high', 'id', 'low', 'open', 'periodStartUnix', 'priceUSD', 'token', 'token__decimals', 'token__derivedETH', 'token__feesUSD', 'token__id', 'token__name', 'token__poolCount', 'token__symbol', 'token__totalSupply', 'token__totalValueLocked', 'token__totalValueLockedUSD', 'token__totalValueLockedUSDUntracked', 'token__txCount', 'token__untrackedVolumeUSD', 'token__volume', 'token__volumeUSD', 'totalValueLocked', 'totalValueLockedUSD', 'untrackedVolumeUSD', 'volume', 'volumeUSD')


class Token_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('decimals', 'derivedETH', 'feesUSD', 'id', 'name', 'poolCount', 'symbol', 'tokenDayData', 'totalSupply', 'totalValueLocked', 'totalValueLockedUSD', 'totalValueLockedUSDUntracked', 'txCount', 'untrackedVolumeUSD', 'volume', 'volumeUSD', 'whitelistPools')


class Transaction_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('blockNumber', 'gasPrice', 'gasUsed', 'id', 'modifyLiquiditys', 'subscriptions', 'swaps', 'timestamp', 'transfers', 'unsubscriptions')


class Transfer_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('from', 'id', 'logIndex', 'origin', 'position', 'position__createdAtTimestamp', 'position__id', 'position__origin', 'position__owner', 'position__tokenId', 'timestamp', 'to', 'tokenId', 'transaction', 'transaction__blockNumber', 'transaction__gasPrice', 'transaction__gasUsed', 'transaction__id', 'transaction__timestamp')


class UniswapDayData_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('date', 'feesUSD', 'id', 'tvlUSD', 'txCount', 'volumeETH', 'volumeUSD', 'volumeUSDUntracked')


class Unsubscribe_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'id', 'logIndex', 'origin', 'position', 'position__createdAtTimestamp', 'position__id', 'position__origin', 'position__owner', 'position__tokenId', 'timestamp', 'tokenId', 'transaction', 'transaction__blockNumber', 'transaction__gasPrice', 'transaction__gasUsed', 'transaction__id', 'transaction__timestamp')


class _SubgraphErrorPolicy_(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('allow', 'deny')



########################################################################
# Input Objects
########################################################################
class BlockChangedFilter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('number_gte',)
    number_gte = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number_gte')


class Block_height(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('hash', 'number', 'number_gte')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(Int, graphql_name='number')
    number_gte = sgqlc.types.Field(Int, graphql_name='number_gte')


class Bundle_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'eth_price_usd', 'eth_price_usd_not', 'eth_price_usd_gt', 'eth_price_usd_lt', 'eth_price_usd_gte', 'eth_price_usd_lte', 'eth_price_usd_in', 'eth_price_usd_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    eth_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='ethPriceUSD')
    eth_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='ethPriceUSD_not')
    eth_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='ethPriceUSD_gt')
    eth_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='ethPriceUSD_lt')
    eth_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='ethPriceUSD_gte')
    eth_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='ethPriceUSD_lte')
    eth_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='ethPriceUSD_in')
    eth_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='ethPriceUSD_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Bundle_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Bundle_filter'), graphql_name='or')


class ModifyLiquidity_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'transaction', 'transaction_not', 'transaction_gt', 'transaction_lt', 'transaction_gte', 'transaction_lte', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_contains_nocase', 'transaction_not_contains', 'transaction_not_contains_nocase', 'transaction_starts_with', 'transaction_starts_with_nocase', 'transaction_not_starts_with', 'transaction_not_starts_with_nocase', 'transaction_ends_with', 'transaction_ends_with_nocase', 'transaction_not_ends_with', 'transaction_not_ends_with_nocase', 'transaction_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'token0', 'token0_not', 'token0_gt', 'token0_lt', 'token0_gte', 'token0_lte', 'token0_in', 'token0_not_in', 'token0_contains', 'token0_contains_nocase', 'token0_not_contains', 'token0_not_contains_nocase', 'token0_starts_with', 'token0_starts_with_nocase', 'token0_not_starts_with', 'token0_not_starts_with_nocase', 'token0_ends_with', 'token0_ends_with_nocase', 'token0_not_ends_with', 'token0_not_ends_with_nocase', 'token0_', 'token1', 'token1_not', 'token1_gt', 'token1_lt', 'token1_gte', 'token1_lte', 'token1_in', 'token1_not_in', 'token1_contains', 'token1_contains_nocase', 'token1_not_contains', 'token1_not_contains_nocase', 'token1_starts_with', 'token1_starts_with_nocase', 'token1_not_starts_with', 'token1_not_starts_with_nocase', 'token1_ends_with', 'token1_ends_with_nocase', 'token1_not_ends_with', 'token1_not_ends_with_nocase', 'token1_', 'sender', 'sender_not', 'sender_gt', 'sender_lt', 'sender_gte', 'sender_lte', 'sender_in', 'sender_not_in', 'sender_contains', 'sender_not_contains', 'origin', 'origin_not', 'origin_gt', 'origin_lt', 'origin_gte', 'origin_lte', 'origin_in', 'origin_not_in', 'origin_contains', 'origin_not_contains', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'amount0', 'amount0_not', 'amount0_gt', 'amount0_lt', 'amount0_gte', 'amount0_lte', 'amount0_in', 'amount0_not_in', 'amount1', 'amount1_not', 'amount1_gt', 'amount1_lt', 'amount1_gte', 'amount1_lte', 'amount1_in', 'amount1_not_in', 'amount_usd', 'amount_usd_not', 'amount_usd_gt', 'amount_usd_lt', 'amount_usd_gte', 'amount_usd_lte', 'amount_usd_in', 'amount_usd_not_in', 'tick_lower', 'tick_lower_not', 'tick_lower_gt', 'tick_lower_lt', 'tick_lower_gte', 'tick_lower_lte', 'tick_lower_in', 'tick_lower_not_in', 'tick_upper', 'tick_upper_not', 'tick_upper_gt', 'tick_upper_lt', 'tick_upper_gte', 'tick_upper_lte', 'tick_upper_in', 'tick_upper_not_in', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    transaction = sgqlc.types.Field(String, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(String, graphql_name='transaction_not')
    transaction_gt = sgqlc.types.Field(String, graphql_name='transaction_gt')
    transaction_lt = sgqlc.types.Field(String, graphql_name='transaction_lt')
    transaction_gte = sgqlc.types.Field(String, graphql_name='transaction_gte')
    transaction_lte = sgqlc.types.Field(String, graphql_name='transaction_lte')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(String, graphql_name='transaction_contains')
    transaction_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_contains_nocase')
    transaction_not_contains = sgqlc.types.Field(String, graphql_name='transaction_not_contains')
    transaction_not_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_contains_nocase')
    transaction_starts_with = sgqlc.types.Field(String, graphql_name='transaction_starts_with')
    transaction_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_starts_with_nocase')
    transaction_not_starts_with = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with')
    transaction_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with_nocase')
    transaction_ends_with = sgqlc.types.Field(String, graphql_name='transaction_ends_with')
    transaction_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_ends_with_nocase')
    transaction_not_ends_with = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with')
    transaction_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with_nocase')
    transaction_ = sgqlc.types.Field('Transaction_filter', graphql_name='transaction_')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    token0 = sgqlc.types.Field(String, graphql_name='token0')
    token0_not = sgqlc.types.Field(String, graphql_name='token0_not')
    token0_gt = sgqlc.types.Field(String, graphql_name='token0_gt')
    token0_lt = sgqlc.types.Field(String, graphql_name='token0_lt')
    token0_gte = sgqlc.types.Field(String, graphql_name='token0_gte')
    token0_lte = sgqlc.types.Field(String, graphql_name='token0_lte')
    token0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token0_in')
    token0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token0_not_in')
    token0_contains = sgqlc.types.Field(String, graphql_name='token0_contains')
    token0_contains_nocase = sgqlc.types.Field(String, graphql_name='token0_contains_nocase')
    token0_not_contains = sgqlc.types.Field(String, graphql_name='token0_not_contains')
    token0_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token0_not_contains_nocase')
    token0_starts_with = sgqlc.types.Field(String, graphql_name='token0_starts_with')
    token0_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token0_starts_with_nocase')
    token0_not_starts_with = sgqlc.types.Field(String, graphql_name='token0_not_starts_with')
    token0_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token0_not_starts_with_nocase')
    token0_ends_with = sgqlc.types.Field(String, graphql_name='token0_ends_with')
    token0_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token0_ends_with_nocase')
    token0_not_ends_with = sgqlc.types.Field(String, graphql_name='token0_not_ends_with')
    token0_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token0_not_ends_with_nocase')
    token0_ = sgqlc.types.Field('Token_filter', graphql_name='token0_')
    token1 = sgqlc.types.Field(String, graphql_name='token1')
    token1_not = sgqlc.types.Field(String, graphql_name='token1_not')
    token1_gt = sgqlc.types.Field(String, graphql_name='token1_gt')
    token1_lt = sgqlc.types.Field(String, graphql_name='token1_lt')
    token1_gte = sgqlc.types.Field(String, graphql_name='token1_gte')
    token1_lte = sgqlc.types.Field(String, graphql_name='token1_lte')
    token1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token1_in')
    token1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token1_not_in')
    token1_contains = sgqlc.types.Field(String, graphql_name='token1_contains')
    token1_contains_nocase = sgqlc.types.Field(String, graphql_name='token1_contains_nocase')
    token1_not_contains = sgqlc.types.Field(String, graphql_name='token1_not_contains')
    token1_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token1_not_contains_nocase')
    token1_starts_with = sgqlc.types.Field(String, graphql_name='token1_starts_with')
    token1_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token1_starts_with_nocase')
    token1_not_starts_with = sgqlc.types.Field(String, graphql_name='token1_not_starts_with')
    token1_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token1_not_starts_with_nocase')
    token1_ends_with = sgqlc.types.Field(String, graphql_name='token1_ends_with')
    token1_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token1_ends_with_nocase')
    token1_not_ends_with = sgqlc.types.Field(String, graphql_name='token1_not_ends_with')
    token1_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token1_not_ends_with_nocase')
    token1_ = sgqlc.types.Field('Token_filter', graphql_name='token1_')
    sender = sgqlc.types.Field(Bytes, graphql_name='sender')
    sender_not = sgqlc.types.Field(Bytes, graphql_name='sender_not')
    sender_gt = sgqlc.types.Field(Bytes, graphql_name='sender_gt')
    sender_lt = sgqlc.types.Field(Bytes, graphql_name='sender_lt')
    sender_gte = sgqlc.types.Field(Bytes, graphql_name='sender_gte')
    sender_lte = sgqlc.types.Field(Bytes, graphql_name='sender_lte')
    sender_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sender_in')
    sender_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sender_not_in')
    sender_contains = sgqlc.types.Field(Bytes, graphql_name='sender_contains')
    sender_not_contains = sgqlc.types.Field(Bytes, graphql_name='sender_not_contains')
    origin = sgqlc.types.Field(Bytes, graphql_name='origin')
    origin_not = sgqlc.types.Field(Bytes, graphql_name='origin_not')
    origin_gt = sgqlc.types.Field(Bytes, graphql_name='origin_gt')
    origin_lt = sgqlc.types.Field(Bytes, graphql_name='origin_lt')
    origin_gte = sgqlc.types.Field(Bytes, graphql_name='origin_gte')
    origin_lte = sgqlc.types.Field(Bytes, graphql_name='origin_lte')
    origin_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='origin_in')
    origin_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='origin_not_in')
    origin_contains = sgqlc.types.Field(Bytes, graphql_name='origin_contains')
    origin_not_contains = sgqlc.types.Field(Bytes, graphql_name='origin_not_contains')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigInt, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigInt, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigInt, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigInt, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigInt, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amount_not_in')
    amount0 = sgqlc.types.Field(BigDecimal, graphql_name='amount0')
    amount0_not = sgqlc.types.Field(BigDecimal, graphql_name='amount0_not')
    amount0_gt = sgqlc.types.Field(BigDecimal, graphql_name='amount0_gt')
    amount0_lt = sgqlc.types.Field(BigDecimal, graphql_name='amount0_lt')
    amount0_gte = sgqlc.types.Field(BigDecimal, graphql_name='amount0_gte')
    amount0_lte = sgqlc.types.Field(BigDecimal, graphql_name='amount0_lte')
    amount0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount0_in')
    amount0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount0_not_in')
    amount1 = sgqlc.types.Field(BigDecimal, graphql_name='amount1')
    amount1_not = sgqlc.types.Field(BigDecimal, graphql_name='amount1_not')
    amount1_gt = sgqlc.types.Field(BigDecimal, graphql_name='amount1_gt')
    amount1_lt = sgqlc.types.Field(BigDecimal, graphql_name='amount1_lt')
    amount1_gte = sgqlc.types.Field(BigDecimal, graphql_name='amount1_gte')
    amount1_lte = sgqlc.types.Field(BigDecimal, graphql_name='amount1_lte')
    amount1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount1_in')
    amount1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount1_not_in')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_not')
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gt')
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lt')
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gte')
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lte')
    amount_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_in')
    amount_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_not_in')
    tick_lower = sgqlc.types.Field(BigInt, graphql_name='tickLower')
    tick_lower_not = sgqlc.types.Field(BigInt, graphql_name='tickLower_not')
    tick_lower_gt = sgqlc.types.Field(BigInt, graphql_name='tickLower_gt')
    tick_lower_lt = sgqlc.types.Field(BigInt, graphql_name='tickLower_lt')
    tick_lower_gte = sgqlc.types.Field(BigInt, graphql_name='tickLower_gte')
    tick_lower_lte = sgqlc.types.Field(BigInt, graphql_name='tickLower_lte')
    tick_lower_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tickLower_in')
    tick_lower_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tickLower_not_in')
    tick_upper = sgqlc.types.Field(BigInt, graphql_name='tickUpper')
    tick_upper_not = sgqlc.types.Field(BigInt, graphql_name='tickUpper_not')
    tick_upper_gt = sgqlc.types.Field(BigInt, graphql_name='tickUpper_gt')
    tick_upper_lt = sgqlc.types.Field(BigInt, graphql_name='tickUpper_lt')
    tick_upper_gte = sgqlc.types.Field(BigInt, graphql_name='tickUpper_gte')
    tick_upper_lte = sgqlc.types.Field(BigInt, graphql_name='tickUpper_lte')
    tick_upper_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tickUpper_in')
    tick_upper_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tickUpper_not_in')
    log_index = sgqlc.types.Field(BigInt, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(BigInt, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(BigInt, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(BigInt, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(BigInt, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(BigInt, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('ModifyLiquidity_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('ModifyLiquidity_filter'), graphql_name='or')


class PoolDayData_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'date', 'date_not', 'date_gt', 'date_lt', 'date_gte', 'date_lte', 'date_in', 'date_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'liquidity', 'liquidity_not', 'liquidity_gt', 'liquidity_lt', 'liquidity_gte', 'liquidity_lte', 'liquidity_in', 'liquidity_not_in', 'sqrt_price', 'sqrt_price_not', 'sqrt_price_gt', 'sqrt_price_lt', 'sqrt_price_gte', 'sqrt_price_lte', 'sqrt_price_in', 'sqrt_price_not_in', 'token0_price', 'token0_price_not', 'token0_price_gt', 'token0_price_lt', 'token0_price_gte', 'token0_price_lte', 'token0_price_in', 'token0_price_not_in', 'token1_price', 'token1_price_not', 'token1_price_gt', 'token1_price_lt', 'token1_price_gte', 'token1_price_lte', 'token1_price_in', 'token1_price_not_in', 'tick', 'tick_not', 'tick_gt', 'tick_lt', 'tick_gte', 'tick_lte', 'tick_in', 'tick_not_in', 'tvl_usd', 'tvl_usd_not', 'tvl_usd_gt', 'tvl_usd_lt', 'tvl_usd_gte', 'tvl_usd_lte', 'tvl_usd_in', 'tvl_usd_not_in', 'volume_token0', 'volume_token0_not', 'volume_token0_gt', 'volume_token0_lt', 'volume_token0_gte', 'volume_token0_lte', 'volume_token0_in', 'volume_token0_not_in', 'volume_token1', 'volume_token1_not', 'volume_token1_gt', 'volume_token1_lt', 'volume_token1_gte', 'volume_token1_lte', 'volume_token1_in', 'volume_token1_not_in', 'volume_usd', 'volume_usd_not', 'volume_usd_gt', 'volume_usd_lt', 'volume_usd_gte', 'volume_usd_lte', 'volume_usd_in', 'volume_usd_not_in', 'fees_usd', 'fees_usd_not', 'fees_usd_gt', 'fees_usd_lt', 'fees_usd_gte', 'fees_usd_lte', 'fees_usd_in', 'fees_usd_not_in', 'tx_count', 'tx_count_not', 'tx_count_gt', 'tx_count_lt', 'tx_count_gte', 'tx_count_lte', 'tx_count_in', 'tx_count_not_in', 'open', 'open_not', 'open_gt', 'open_lt', 'open_gte', 'open_lte', 'open_in', 'open_not_in', 'high', 'high_not', 'high_gt', 'high_lt', 'high_gte', 'high_lte', 'high_in', 'high_not_in', 'low', 'low_not', 'low_gt', 'low_lt', 'low_gte', 'low_lte', 'low_in', 'low_not_in', 'close', 'close_not', 'close_gt', 'close_lt', 'close_gte', 'close_lte', 'close_in', 'close_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    date = sgqlc.types.Field(Int, graphql_name='date')
    date_not = sgqlc.types.Field(Int, graphql_name='date_not')
    date_gt = sgqlc.types.Field(Int, graphql_name='date_gt')
    date_lt = sgqlc.types.Field(Int, graphql_name='date_lt')
    date_gte = sgqlc.types.Field(Int, graphql_name='date_gte')
    date_lte = sgqlc.types.Field(Int, graphql_name='date_lte')
    date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='date_in')
    date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='date_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    liquidity = sgqlc.types.Field(BigInt, graphql_name='liquidity')
    liquidity_not = sgqlc.types.Field(BigInt, graphql_name='liquidity_not')
    liquidity_gt = sgqlc.types.Field(BigInt, graphql_name='liquidity_gt')
    liquidity_lt = sgqlc.types.Field(BigInt, graphql_name='liquidity_lt')
    liquidity_gte = sgqlc.types.Field(BigInt, graphql_name='liquidity_gte')
    liquidity_lte = sgqlc.types.Field(BigInt, graphql_name='liquidity_lte')
    liquidity_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidity_in')
    liquidity_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidity_not_in')
    sqrt_price = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice')
    sqrt_price_not = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_not')
    sqrt_price_gt = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_gt')
    sqrt_price_lt = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_lt')
    sqrt_price_gte = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_gte')
    sqrt_price_lte = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_lte')
    sqrt_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sqrtPrice_in')
    sqrt_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sqrtPrice_not_in')
    token0_price = sgqlc.types.Field(BigDecimal, graphql_name='token0Price')
    token0_price_not = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_not')
    token0_price_gt = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_gt')
    token0_price_lt = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_lt')
    token0_price_gte = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_gte')
    token0_price_lte = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_lte')
    token0_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token0Price_in')
    token0_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token0Price_not_in')
    token1_price = sgqlc.types.Field(BigDecimal, graphql_name='token1Price')
    token1_price_not = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_not')
    token1_price_gt = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_gt')
    token1_price_lt = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_lt')
    token1_price_gte = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_gte')
    token1_price_lte = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_lte')
    token1_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token1Price_in')
    token1_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token1Price_not_in')
    tick = sgqlc.types.Field(BigInt, graphql_name='tick')
    tick_not = sgqlc.types.Field(BigInt, graphql_name='tick_not')
    tick_gt = sgqlc.types.Field(BigInt, graphql_name='tick_gt')
    tick_lt = sgqlc.types.Field(BigInt, graphql_name='tick_lt')
    tick_gte = sgqlc.types.Field(BigInt, graphql_name='tick_gte')
    tick_lte = sgqlc.types.Field(BigInt, graphql_name='tick_lte')
    tick_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tick_in')
    tick_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tick_not_in')
    tvl_usd = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD')
    tvl_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_not')
    tvl_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_gt')
    tvl_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_lt')
    tvl_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_gte')
    tvl_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_lte')
    tvl_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tvlUSD_in')
    tvl_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tvlUSD_not_in')
    volume_token0 = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0')
    volume_token0_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_not')
    volume_token0_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_gt')
    volume_token0_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_lt')
    volume_token0_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_gte')
    volume_token0_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_lte')
    volume_token0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken0_in')
    volume_token0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken0_not_in')
    volume_token1 = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1')
    volume_token1_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_not')
    volume_token1_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_gt')
    volume_token1_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_lt')
    volume_token1_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_gte')
    volume_token1_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_lte')
    volume_token1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken1_in')
    volume_token1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken1_not_in')
    volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD')
    volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_not')
    volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gt')
    volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lt')
    volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gte')
    volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lte')
    volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_in')
    volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_not_in')
    fees_usd = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD')
    fees_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_not')
    fees_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gt')
    fees_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lt')
    fees_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gte')
    fees_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lte')
    fees_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_in')
    fees_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_not_in')
    tx_count = sgqlc.types.Field(BigInt, graphql_name='txCount')
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name='txCount_not')
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name='txCount_gt')
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name='txCount_lt')
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name='txCount_gte')
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name='txCount_lte')
    tx_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_in')
    tx_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_not_in')
    open = sgqlc.types.Field(BigDecimal, graphql_name='open')
    open_not = sgqlc.types.Field(BigDecimal, graphql_name='open_not')
    open_gt = sgqlc.types.Field(BigDecimal, graphql_name='open_gt')
    open_lt = sgqlc.types.Field(BigDecimal, graphql_name='open_lt')
    open_gte = sgqlc.types.Field(BigDecimal, graphql_name='open_gte')
    open_lte = sgqlc.types.Field(BigDecimal, graphql_name='open_lte')
    open_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='open_in')
    open_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='open_not_in')
    high = sgqlc.types.Field(BigDecimal, graphql_name='high')
    high_not = sgqlc.types.Field(BigDecimal, graphql_name='high_not')
    high_gt = sgqlc.types.Field(BigDecimal, graphql_name='high_gt')
    high_lt = sgqlc.types.Field(BigDecimal, graphql_name='high_lt')
    high_gte = sgqlc.types.Field(BigDecimal, graphql_name='high_gte')
    high_lte = sgqlc.types.Field(BigDecimal, graphql_name='high_lte')
    high_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='high_in')
    high_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='high_not_in')
    low = sgqlc.types.Field(BigDecimal, graphql_name='low')
    low_not = sgqlc.types.Field(BigDecimal, graphql_name='low_not')
    low_gt = sgqlc.types.Field(BigDecimal, graphql_name='low_gt')
    low_lt = sgqlc.types.Field(BigDecimal, graphql_name='low_lt')
    low_gte = sgqlc.types.Field(BigDecimal, graphql_name='low_gte')
    low_lte = sgqlc.types.Field(BigDecimal, graphql_name='low_lte')
    low_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='low_in')
    low_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='low_not_in')
    close = sgqlc.types.Field(BigDecimal, graphql_name='close')
    close_not = sgqlc.types.Field(BigDecimal, graphql_name='close_not')
    close_gt = sgqlc.types.Field(BigDecimal, graphql_name='close_gt')
    close_lt = sgqlc.types.Field(BigDecimal, graphql_name='close_lt')
    close_gte = sgqlc.types.Field(BigDecimal, graphql_name='close_gte')
    close_lte = sgqlc.types.Field(BigDecimal, graphql_name='close_lte')
    close_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='close_in')
    close_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='close_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PoolDayData_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PoolDayData_filter'), graphql_name='or')


class PoolHourData_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'period_start_unix', 'period_start_unix_not', 'period_start_unix_gt', 'period_start_unix_lt', 'period_start_unix_gte', 'period_start_unix_lte', 'period_start_unix_in', 'period_start_unix_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'liquidity', 'liquidity_not', 'liquidity_gt', 'liquidity_lt', 'liquidity_gte', 'liquidity_lte', 'liquidity_in', 'liquidity_not_in', 'sqrt_price', 'sqrt_price_not', 'sqrt_price_gt', 'sqrt_price_lt', 'sqrt_price_gte', 'sqrt_price_lte', 'sqrt_price_in', 'sqrt_price_not_in', 'token0_price', 'token0_price_not', 'token0_price_gt', 'token0_price_lt', 'token0_price_gte', 'token0_price_lte', 'token0_price_in', 'token0_price_not_in', 'token1_price', 'token1_price_not', 'token1_price_gt', 'token1_price_lt', 'token1_price_gte', 'token1_price_lte', 'token1_price_in', 'token1_price_not_in', 'tick', 'tick_not', 'tick_gt', 'tick_lt', 'tick_gte', 'tick_lte', 'tick_in', 'tick_not_in', 'tvl_usd', 'tvl_usd_not', 'tvl_usd_gt', 'tvl_usd_lt', 'tvl_usd_gte', 'tvl_usd_lte', 'tvl_usd_in', 'tvl_usd_not_in', 'volume_token0', 'volume_token0_not', 'volume_token0_gt', 'volume_token0_lt', 'volume_token0_gte', 'volume_token0_lte', 'volume_token0_in', 'volume_token0_not_in', 'volume_token1', 'volume_token1_not', 'volume_token1_gt', 'volume_token1_lt', 'volume_token1_gte', 'volume_token1_lte', 'volume_token1_in', 'volume_token1_not_in', 'volume_usd', 'volume_usd_not', 'volume_usd_gt', 'volume_usd_lt', 'volume_usd_gte', 'volume_usd_lte', 'volume_usd_in', 'volume_usd_not_in', 'fees_usd', 'fees_usd_not', 'fees_usd_gt', 'fees_usd_lt', 'fees_usd_gte', 'fees_usd_lte', 'fees_usd_in', 'fees_usd_not_in', 'tx_count', 'tx_count_not', 'tx_count_gt', 'tx_count_lt', 'tx_count_gte', 'tx_count_lte', 'tx_count_in', 'tx_count_not_in', 'open', 'open_not', 'open_gt', 'open_lt', 'open_gte', 'open_lte', 'open_in', 'open_not_in', 'high', 'high_not', 'high_gt', 'high_lt', 'high_gte', 'high_lte', 'high_in', 'high_not_in', 'low', 'low_not', 'low_gt', 'low_lt', 'low_gte', 'low_lte', 'low_in', 'low_not_in', 'close', 'close_not', 'close_gt', 'close_lt', 'close_gte', 'close_lte', 'close_in', 'close_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    period_start_unix = sgqlc.types.Field(Int, graphql_name='periodStartUnix')
    period_start_unix_not = sgqlc.types.Field(Int, graphql_name='periodStartUnix_not')
    period_start_unix_gt = sgqlc.types.Field(Int, graphql_name='periodStartUnix_gt')
    period_start_unix_lt = sgqlc.types.Field(Int, graphql_name='periodStartUnix_lt')
    period_start_unix_gte = sgqlc.types.Field(Int, graphql_name='periodStartUnix_gte')
    period_start_unix_lte = sgqlc.types.Field(Int, graphql_name='periodStartUnix_lte')
    period_start_unix_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='periodStartUnix_in')
    period_start_unix_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='periodStartUnix_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field('Pool_filter', graphql_name='pool_')
    liquidity = sgqlc.types.Field(BigInt, graphql_name='liquidity')
    liquidity_not = sgqlc.types.Field(BigInt, graphql_name='liquidity_not')
    liquidity_gt = sgqlc.types.Field(BigInt, graphql_name='liquidity_gt')
    liquidity_lt = sgqlc.types.Field(BigInt, graphql_name='liquidity_lt')
    liquidity_gte = sgqlc.types.Field(BigInt, graphql_name='liquidity_gte')
    liquidity_lte = sgqlc.types.Field(BigInt, graphql_name='liquidity_lte')
    liquidity_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidity_in')
    liquidity_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidity_not_in')
    sqrt_price = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice')
    sqrt_price_not = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_not')
    sqrt_price_gt = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_gt')
    sqrt_price_lt = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_lt')
    sqrt_price_gte = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_gte')
    sqrt_price_lte = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_lte')
    sqrt_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sqrtPrice_in')
    sqrt_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sqrtPrice_not_in')
    token0_price = sgqlc.types.Field(BigDecimal, graphql_name='token0Price')
    token0_price_not = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_not')
    token0_price_gt = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_gt')
    token0_price_lt = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_lt')
    token0_price_gte = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_gte')
    token0_price_lte = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_lte')
    token0_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token0Price_in')
    token0_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token0Price_not_in')
    token1_price = sgqlc.types.Field(BigDecimal, graphql_name='token1Price')
    token1_price_not = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_not')
    token1_price_gt = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_gt')
    token1_price_lt = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_lt')
    token1_price_gte = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_gte')
    token1_price_lte = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_lte')
    token1_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token1Price_in')
    token1_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token1Price_not_in')
    tick = sgqlc.types.Field(BigInt, graphql_name='tick')
    tick_not = sgqlc.types.Field(BigInt, graphql_name='tick_not')
    tick_gt = sgqlc.types.Field(BigInt, graphql_name='tick_gt')
    tick_lt = sgqlc.types.Field(BigInt, graphql_name='tick_lt')
    tick_gte = sgqlc.types.Field(BigInt, graphql_name='tick_gte')
    tick_lte = sgqlc.types.Field(BigInt, graphql_name='tick_lte')
    tick_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tick_in')
    tick_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tick_not_in')
    tvl_usd = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD')
    tvl_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_not')
    tvl_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_gt')
    tvl_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_lt')
    tvl_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_gte')
    tvl_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_lte')
    tvl_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tvlUSD_in')
    tvl_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tvlUSD_not_in')
    volume_token0 = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0')
    volume_token0_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_not')
    volume_token0_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_gt')
    volume_token0_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_lt')
    volume_token0_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_gte')
    volume_token0_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_lte')
    volume_token0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken0_in')
    volume_token0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken0_not_in')
    volume_token1 = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1')
    volume_token1_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_not')
    volume_token1_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_gt')
    volume_token1_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_lt')
    volume_token1_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_gte')
    volume_token1_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_lte')
    volume_token1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken1_in')
    volume_token1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken1_not_in')
    volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD')
    volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_not')
    volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gt')
    volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lt')
    volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gte')
    volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lte')
    volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_in')
    volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_not_in')
    fees_usd = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD')
    fees_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_not')
    fees_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gt')
    fees_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lt')
    fees_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gte')
    fees_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lte')
    fees_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_in')
    fees_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_not_in')
    tx_count = sgqlc.types.Field(BigInt, graphql_name='txCount')
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name='txCount_not')
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name='txCount_gt')
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name='txCount_lt')
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name='txCount_gte')
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name='txCount_lte')
    tx_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_in')
    tx_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_not_in')
    open = sgqlc.types.Field(BigDecimal, graphql_name='open')
    open_not = sgqlc.types.Field(BigDecimal, graphql_name='open_not')
    open_gt = sgqlc.types.Field(BigDecimal, graphql_name='open_gt')
    open_lt = sgqlc.types.Field(BigDecimal, graphql_name='open_lt')
    open_gte = sgqlc.types.Field(BigDecimal, graphql_name='open_gte')
    open_lte = sgqlc.types.Field(BigDecimal, graphql_name='open_lte')
    open_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='open_in')
    open_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='open_not_in')
    high = sgqlc.types.Field(BigDecimal, graphql_name='high')
    high_not = sgqlc.types.Field(BigDecimal, graphql_name='high_not')
    high_gt = sgqlc.types.Field(BigDecimal, graphql_name='high_gt')
    high_lt = sgqlc.types.Field(BigDecimal, graphql_name='high_lt')
    high_gte = sgqlc.types.Field(BigDecimal, graphql_name='high_gte')
    high_lte = sgqlc.types.Field(BigDecimal, graphql_name='high_lte')
    high_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='high_in')
    high_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='high_not_in')
    low = sgqlc.types.Field(BigDecimal, graphql_name='low')
    low_not = sgqlc.types.Field(BigDecimal, graphql_name='low_not')
    low_gt = sgqlc.types.Field(BigDecimal, graphql_name='low_gt')
    low_lt = sgqlc.types.Field(BigDecimal, graphql_name='low_lt')
    low_gte = sgqlc.types.Field(BigDecimal, graphql_name='low_gte')
    low_lte = sgqlc.types.Field(BigDecimal, graphql_name='low_lte')
    low_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='low_in')
    low_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='low_not_in')
    close = sgqlc.types.Field(BigDecimal, graphql_name='close')
    close_not = sgqlc.types.Field(BigDecimal, graphql_name='close_not')
    close_gt = sgqlc.types.Field(BigDecimal, graphql_name='close_gt')
    close_lt = sgqlc.types.Field(BigDecimal, graphql_name='close_lt')
    close_gte = sgqlc.types.Field(BigDecimal, graphql_name='close_gte')
    close_lte = sgqlc.types.Field(BigDecimal, graphql_name='close_lte')
    close_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='close_in')
    close_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='close_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PoolHourData_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PoolHourData_filter'), graphql_name='or')


class PoolManager_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_count', 'pool_count_not', 'pool_count_gt', 'pool_count_lt', 'pool_count_gte', 'pool_count_lte', 'pool_count_in', 'pool_count_not_in', 'tx_count', 'tx_count_not', 'tx_count_gt', 'tx_count_lt', 'tx_count_gte', 'tx_count_lte', 'tx_count_in', 'tx_count_not_in', 'total_volume_usd', 'total_volume_usd_not', 'total_volume_usd_gt', 'total_volume_usd_lt', 'total_volume_usd_gte', 'total_volume_usd_lte', 'total_volume_usd_in', 'total_volume_usd_not_in', 'total_volume_eth', 'total_volume_eth_not', 'total_volume_eth_gt', 'total_volume_eth_lt', 'total_volume_eth_gte', 'total_volume_eth_lte', 'total_volume_eth_in', 'total_volume_eth_not_in', 'total_fees_usd', 'total_fees_usd_not', 'total_fees_usd_gt', 'total_fees_usd_lt', 'total_fees_usd_gte', 'total_fees_usd_lte', 'total_fees_usd_in', 'total_fees_usd_not_in', 'total_fees_eth', 'total_fees_eth_not', 'total_fees_eth_gt', 'total_fees_eth_lt', 'total_fees_eth_gte', 'total_fees_eth_lte', 'total_fees_eth_in', 'total_fees_eth_not_in', 'untracked_volume_usd', 'untracked_volume_usd_not', 'untracked_volume_usd_gt', 'untracked_volume_usd_lt', 'untracked_volume_usd_gte', 'untracked_volume_usd_lte', 'untracked_volume_usd_in', 'untracked_volume_usd_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'total_value_locked_eth', 'total_value_locked_eth_not', 'total_value_locked_eth_gt', 'total_value_locked_eth_lt', 'total_value_locked_eth_gte', 'total_value_locked_eth_lte', 'total_value_locked_eth_in', 'total_value_locked_eth_not_in', 'total_value_locked_usduntracked', 'total_value_locked_usduntracked_not', 'total_value_locked_usduntracked_gt', 'total_value_locked_usduntracked_lt', 'total_value_locked_usduntracked_gte', 'total_value_locked_usduntracked_lte', 'total_value_locked_usduntracked_in', 'total_value_locked_usduntracked_not_in', 'total_value_locked_ethuntracked', 'total_value_locked_ethuntracked_not', 'total_value_locked_ethuntracked_gt', 'total_value_locked_ethuntracked_lt', 'total_value_locked_ethuntracked_gte', 'total_value_locked_ethuntracked_lte', 'total_value_locked_ethuntracked_in', 'total_value_locked_ethuntracked_not_in', 'owner', 'owner_not', 'owner_gt', 'owner_lt', 'owner_gte', 'owner_lte', 'owner_in', 'owner_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool_count = sgqlc.types.Field(BigInt, graphql_name='poolCount')
    pool_count_not = sgqlc.types.Field(BigInt, graphql_name='poolCount_not')
    pool_count_gt = sgqlc.types.Field(BigInt, graphql_name='poolCount_gt')
    pool_count_lt = sgqlc.types.Field(BigInt, graphql_name='poolCount_lt')
    pool_count_gte = sgqlc.types.Field(BigInt, graphql_name='poolCount_gte')
    pool_count_lte = sgqlc.types.Field(BigInt, graphql_name='poolCount_lte')
    pool_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='poolCount_in')
    pool_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='poolCount_not_in')
    tx_count = sgqlc.types.Field(BigInt, graphql_name='txCount')
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name='txCount_not')
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name='txCount_gt')
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name='txCount_lt')
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name='txCount_gte')
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name='txCount_lte')
    tx_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_in')
    tx_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_not_in')
    total_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD')
    total_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_not')
    total_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_gt')
    total_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_lt')
    total_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_gte')
    total_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_lte')
    total_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeUSD_in')
    total_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeUSD_not_in')
    total_volume_eth = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeETH')
    total_volume_eth_not = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeETH_not')
    total_volume_eth_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeETH_gt')
    total_volume_eth_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeETH_lt')
    total_volume_eth_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeETH_gte')
    total_volume_eth_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeETH_lte')
    total_volume_eth_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeETH_in')
    total_volume_eth_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeETH_not_in')
    total_fees_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesUSD')
    total_fees_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesUSD_not')
    total_fees_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesUSD_gt')
    total_fees_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesUSD_lt')
    total_fees_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesUSD_gte')
    total_fees_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesUSD_lte')
    total_fees_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalFeesUSD_in')
    total_fees_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalFeesUSD_not_in')
    total_fees_eth = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesETH')
    total_fees_eth_not = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesETH_not')
    total_fees_eth_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesETH_gt')
    total_fees_eth_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesETH_lt')
    total_fees_eth_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesETH_gte')
    total_fees_eth_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalFeesETH_lte')
    total_fees_eth_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalFeesETH_in')
    total_fees_eth_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalFeesETH_not_in')
    untracked_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD')
    untracked_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_not')
    untracked_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gt')
    untracked_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lt')
    untracked_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gte')
    untracked_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lte')
    untracked_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_in')
    untracked_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    total_value_locked_eth = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH')
    total_value_locked_eth_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_not')
    total_value_locked_eth_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_gt')
    total_value_locked_eth_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_lt')
    total_value_locked_eth_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_gte')
    total_value_locked_eth_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_lte')
    total_value_locked_eth_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedETH_in')
    total_value_locked_eth_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedETH_not_in')
    total_value_locked_usduntracked = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked')
    total_value_locked_usduntracked_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_not')
    total_value_locked_usduntracked_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_gt')
    total_value_locked_usduntracked_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_lt')
    total_value_locked_usduntracked_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_gte')
    total_value_locked_usduntracked_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_lte')
    total_value_locked_usduntracked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSDUntracked_in')
    total_value_locked_usduntracked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSDUntracked_not_in')
    total_value_locked_ethuntracked = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETHUntracked')
    total_value_locked_ethuntracked_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETHUntracked_not')
    total_value_locked_ethuntracked_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETHUntracked_gt')
    total_value_locked_ethuntracked_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETHUntracked_lt')
    total_value_locked_ethuntracked_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETHUntracked_gte')
    total_value_locked_ethuntracked_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETHUntracked_lte')
    total_value_locked_ethuntracked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedETHUntracked_in')
    total_value_locked_ethuntracked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedETHUntracked_not_in')
    owner = sgqlc.types.Field(ID, graphql_name='owner')
    owner_not = sgqlc.types.Field(ID, graphql_name='owner_not')
    owner_gt = sgqlc.types.Field(ID, graphql_name='owner_gt')
    owner_lt = sgqlc.types.Field(ID, graphql_name='owner_lt')
    owner_gte = sgqlc.types.Field(ID, graphql_name='owner_gte')
    owner_lte = sgqlc.types.Field(ID, graphql_name='owner_lte')
    owner_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='owner_in')
    owner_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='owner_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PoolManager_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PoolManager_filter'), graphql_name='or')


class Pool_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'created_at_timestamp', 'created_at_timestamp_not', 'created_at_timestamp_gt', 'created_at_timestamp_lt', 'created_at_timestamp_gte', 'created_at_timestamp_lte', 'created_at_timestamp_in', 'created_at_timestamp_not_in', 'created_at_block_number', 'created_at_block_number_not', 'created_at_block_number_gt', 'created_at_block_number_lt', 'created_at_block_number_gte', 'created_at_block_number_lte', 'created_at_block_number_in', 'created_at_block_number_not_in', 'token0', 'token0_not', 'token0_gt', 'token0_lt', 'token0_gte', 'token0_lte', 'token0_in', 'token0_not_in', 'token0_contains', 'token0_contains_nocase', 'token0_not_contains', 'token0_not_contains_nocase', 'token0_starts_with', 'token0_starts_with_nocase', 'token0_not_starts_with', 'token0_not_starts_with_nocase', 'token0_ends_with', 'token0_ends_with_nocase', 'token0_not_ends_with', 'token0_not_ends_with_nocase', 'token0_', 'token1', 'token1_not', 'token1_gt', 'token1_lt', 'token1_gte', 'token1_lte', 'token1_in', 'token1_not_in', 'token1_contains', 'token1_contains_nocase', 'token1_not_contains', 'token1_not_contains_nocase', 'token1_starts_with', 'token1_starts_with_nocase', 'token1_not_starts_with', 'token1_not_starts_with_nocase', 'token1_ends_with', 'token1_ends_with_nocase', 'token1_not_ends_with', 'token1_not_ends_with_nocase', 'token1_', 'fee_tier', 'fee_tier_not', 'fee_tier_gt', 'fee_tier_lt', 'fee_tier_gte', 'fee_tier_lte', 'fee_tier_in', 'fee_tier_not_in', 'liquidity', 'liquidity_not', 'liquidity_gt', 'liquidity_lt', 'liquidity_gte', 'liquidity_lte', 'liquidity_in', 'liquidity_not_in', 'sqrt_price', 'sqrt_price_not', 'sqrt_price_gt', 'sqrt_price_lt', 'sqrt_price_gte', 'sqrt_price_lte', 'sqrt_price_in', 'sqrt_price_not_in', 'token0_price', 'token0_price_not', 'token0_price_gt', 'token0_price_lt', 'token0_price_gte', 'token0_price_lte', 'token0_price_in', 'token0_price_not_in', 'token1_price', 'token1_price_not', 'token1_price_gt', 'token1_price_lt', 'token1_price_gte', 'token1_price_lte', 'token1_price_in', 'token1_price_not_in', 'tick', 'tick_not', 'tick_gt', 'tick_lt', 'tick_gte', 'tick_lte', 'tick_in', 'tick_not_in', 'tick_spacing', 'tick_spacing_not', 'tick_spacing_gt', 'tick_spacing_lt', 'tick_spacing_gte', 'tick_spacing_lte', 'tick_spacing_in', 'tick_spacing_not_in', 'observation_index', 'observation_index_not', 'observation_index_gt', 'observation_index_lt', 'observation_index_gte', 'observation_index_lte', 'observation_index_in', 'observation_index_not_in', 'volume_token0', 'volume_token0_not', 'volume_token0_gt', 'volume_token0_lt', 'volume_token0_gte', 'volume_token0_lte', 'volume_token0_in', 'volume_token0_not_in', 'volume_token1', 'volume_token1_not', 'volume_token1_gt', 'volume_token1_lt', 'volume_token1_gte', 'volume_token1_lte', 'volume_token1_in', 'volume_token1_not_in', 'volume_usd', 'volume_usd_not', 'volume_usd_gt', 'volume_usd_lt', 'volume_usd_gte', 'volume_usd_lte', 'volume_usd_in', 'volume_usd_not_in', 'untracked_volume_usd', 'untracked_volume_usd_not', 'untracked_volume_usd_gt', 'untracked_volume_usd_lt', 'untracked_volume_usd_gte', 'untracked_volume_usd_lte', 'untracked_volume_usd_in', 'untracked_volume_usd_not_in', 'fees_usd', 'fees_usd_not', 'fees_usd_gt', 'fees_usd_lt', 'fees_usd_gte', 'fees_usd_lte', 'fees_usd_in', 'fees_usd_not_in', 'tx_count', 'tx_count_not', 'tx_count_gt', 'tx_count_lt', 'tx_count_gte', 'tx_count_lte', 'tx_count_in', 'tx_count_not_in', 'collected_fees_token0', 'collected_fees_token0_not', 'collected_fees_token0_gt', 'collected_fees_token0_lt', 'collected_fees_token0_gte', 'collected_fees_token0_lte', 'collected_fees_token0_in', 'collected_fees_token0_not_in', 'collected_fees_token1', 'collected_fees_token1_not', 'collected_fees_token1_gt', 'collected_fees_token1_lt', 'collected_fees_token1_gte', 'collected_fees_token1_lte', 'collected_fees_token1_in', 'collected_fees_token1_not_in', 'collected_fees_usd', 'collected_fees_usd_not', 'collected_fees_usd_gt', 'collected_fees_usd_lt', 'collected_fees_usd_gte', 'collected_fees_usd_lte', 'collected_fees_usd_in', 'collected_fees_usd_not_in', 'total_value_locked_token0', 'total_value_locked_token0_not', 'total_value_locked_token0_gt', 'total_value_locked_token0_lt', 'total_value_locked_token0_gte', 'total_value_locked_token0_lte', 'total_value_locked_token0_in', 'total_value_locked_token0_not_in', 'total_value_locked_token1', 'total_value_locked_token1_not', 'total_value_locked_token1_gt', 'total_value_locked_token1_lt', 'total_value_locked_token1_gte', 'total_value_locked_token1_lte', 'total_value_locked_token1_in', 'total_value_locked_token1_not_in', 'total_value_locked_eth', 'total_value_locked_eth_not', 'total_value_locked_eth_gt', 'total_value_locked_eth_lt', 'total_value_locked_eth_gte', 'total_value_locked_eth_lte', 'total_value_locked_eth_in', 'total_value_locked_eth_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'total_value_locked_usduntracked', 'total_value_locked_usduntracked_not', 'total_value_locked_usduntracked_gt', 'total_value_locked_usduntracked_lt', 'total_value_locked_usduntracked_gte', 'total_value_locked_usduntracked_lte', 'total_value_locked_usduntracked_in', 'total_value_locked_usduntracked_not_in', 'liquidity_provider_count', 'liquidity_provider_count_not', 'liquidity_provider_count_gt', 'liquidity_provider_count_lt', 'liquidity_provider_count_gte', 'liquidity_provider_count_lte', 'liquidity_provider_count_in', 'liquidity_provider_count_not_in', 'pool_hour_data_', 'pool_day_data_', 'hooks', 'hooks_not', 'hooks_gt', 'hooks_lt', 'hooks_gte', 'hooks_lte', 'hooks_in', 'hooks_not_in', 'hooks_contains', 'hooks_contains_nocase', 'hooks_not_contains', 'hooks_not_contains_nocase', 'hooks_starts_with', 'hooks_starts_with_nocase', 'hooks_not_starts_with', 'hooks_not_starts_with_nocase', 'hooks_ends_with', 'hooks_ends_with_nocase', 'hooks_not_ends_with', 'hooks_not_ends_with_nocase', 'modify_liquiditys_', 'swaps_', 'ticks_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    created_at_timestamp = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp')
    created_at_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_not')
    created_at_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_gt')
    created_at_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_lt')
    created_at_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_gte')
    created_at_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_lte')
    created_at_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtTimestamp_in')
    created_at_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtTimestamp_not_in')
    created_at_block_number = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber')
    created_at_block_number_not = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_not')
    created_at_block_number_gt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_gt')
    created_at_block_number_lt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_lt')
    created_at_block_number_gte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_gte')
    created_at_block_number_lte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_lte')
    created_at_block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlockNumber_in')
    created_at_block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlockNumber_not_in')
    token0 = sgqlc.types.Field(String, graphql_name='token0')
    token0_not = sgqlc.types.Field(String, graphql_name='token0_not')
    token0_gt = sgqlc.types.Field(String, graphql_name='token0_gt')
    token0_lt = sgqlc.types.Field(String, graphql_name='token0_lt')
    token0_gte = sgqlc.types.Field(String, graphql_name='token0_gte')
    token0_lte = sgqlc.types.Field(String, graphql_name='token0_lte')
    token0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token0_in')
    token0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token0_not_in')
    token0_contains = sgqlc.types.Field(String, graphql_name='token0_contains')
    token0_contains_nocase = sgqlc.types.Field(String, graphql_name='token0_contains_nocase')
    token0_not_contains = sgqlc.types.Field(String, graphql_name='token0_not_contains')
    token0_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token0_not_contains_nocase')
    token0_starts_with = sgqlc.types.Field(String, graphql_name='token0_starts_with')
    token0_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token0_starts_with_nocase')
    token0_not_starts_with = sgqlc.types.Field(String, graphql_name='token0_not_starts_with')
    token0_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token0_not_starts_with_nocase')
    token0_ends_with = sgqlc.types.Field(String, graphql_name='token0_ends_with')
    token0_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token0_ends_with_nocase')
    token0_not_ends_with = sgqlc.types.Field(String, graphql_name='token0_not_ends_with')
    token0_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token0_not_ends_with_nocase')
    token0_ = sgqlc.types.Field('Token_filter', graphql_name='token0_')
    token1 = sgqlc.types.Field(String, graphql_name='token1')
    token1_not = sgqlc.types.Field(String, graphql_name='token1_not')
    token1_gt = sgqlc.types.Field(String, graphql_name='token1_gt')
    token1_lt = sgqlc.types.Field(String, graphql_name='token1_lt')
    token1_gte = sgqlc.types.Field(String, graphql_name='token1_gte')
    token1_lte = sgqlc.types.Field(String, graphql_name='token1_lte')
    token1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token1_in')
    token1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token1_not_in')
    token1_contains = sgqlc.types.Field(String, graphql_name='token1_contains')
    token1_contains_nocase = sgqlc.types.Field(String, graphql_name='token1_contains_nocase')
    token1_not_contains = sgqlc.types.Field(String, graphql_name='token1_not_contains')
    token1_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token1_not_contains_nocase')
    token1_starts_with = sgqlc.types.Field(String, graphql_name='token1_starts_with')
    token1_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token1_starts_with_nocase')
    token1_not_starts_with = sgqlc.types.Field(String, graphql_name='token1_not_starts_with')
    token1_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token1_not_starts_with_nocase')
    token1_ends_with = sgqlc.types.Field(String, graphql_name='token1_ends_with')
    token1_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token1_ends_with_nocase')
    token1_not_ends_with = sgqlc.types.Field(String, graphql_name='token1_not_ends_with')
    token1_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token1_not_ends_with_nocase')
    token1_ = sgqlc.types.Field('Token_filter', graphql_name='token1_')
    fee_tier = sgqlc.types.Field(BigInt, graphql_name='feeTier')
    fee_tier_not = sgqlc.types.Field(BigInt, graphql_name='feeTier_not')
    fee_tier_gt = sgqlc.types.Field(BigInt, graphql_name='feeTier_gt')
    fee_tier_lt = sgqlc.types.Field(BigInt, graphql_name='feeTier_lt')
    fee_tier_gte = sgqlc.types.Field(BigInt, graphql_name='feeTier_gte')
    fee_tier_lte = sgqlc.types.Field(BigInt, graphql_name='feeTier_lte')
    fee_tier_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='feeTier_in')
    fee_tier_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='feeTier_not_in')
    liquidity = sgqlc.types.Field(BigInt, graphql_name='liquidity')
    liquidity_not = sgqlc.types.Field(BigInt, graphql_name='liquidity_not')
    liquidity_gt = sgqlc.types.Field(BigInt, graphql_name='liquidity_gt')
    liquidity_lt = sgqlc.types.Field(BigInt, graphql_name='liquidity_lt')
    liquidity_gte = sgqlc.types.Field(BigInt, graphql_name='liquidity_gte')
    liquidity_lte = sgqlc.types.Field(BigInt, graphql_name='liquidity_lte')
    liquidity_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidity_in')
    liquidity_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidity_not_in')
    sqrt_price = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice')
    sqrt_price_not = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_not')
    sqrt_price_gt = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_gt')
    sqrt_price_lt = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_lt')
    sqrt_price_gte = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_gte')
    sqrt_price_lte = sgqlc.types.Field(BigInt, graphql_name='sqrtPrice_lte')
    sqrt_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sqrtPrice_in')
    sqrt_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sqrtPrice_not_in')
    token0_price = sgqlc.types.Field(BigDecimal, graphql_name='token0Price')
    token0_price_not = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_not')
    token0_price_gt = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_gt')
    token0_price_lt = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_lt')
    token0_price_gte = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_gte')
    token0_price_lte = sgqlc.types.Field(BigDecimal, graphql_name='token0Price_lte')
    token0_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token0Price_in')
    token0_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token0Price_not_in')
    token1_price = sgqlc.types.Field(BigDecimal, graphql_name='token1Price')
    token1_price_not = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_not')
    token1_price_gt = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_gt')
    token1_price_lt = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_lt')
    token1_price_gte = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_gte')
    token1_price_lte = sgqlc.types.Field(BigDecimal, graphql_name='token1Price_lte')
    token1_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token1Price_in')
    token1_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='token1Price_not_in')
    tick = sgqlc.types.Field(BigInt, graphql_name='tick')
    tick_not = sgqlc.types.Field(BigInt, graphql_name='tick_not')
    tick_gt = sgqlc.types.Field(BigInt, graphql_name='tick_gt')
    tick_lt = sgqlc.types.Field(BigInt, graphql_name='tick_lt')
    tick_gte = sgqlc.types.Field(BigInt, graphql_name='tick_gte')
    tick_lte = sgqlc.types.Field(BigInt, graphql_name='tick_lte')
    tick_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tick_in')
    tick_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tick_not_in')
    tick_spacing = sgqlc.types.Field(BigInt, graphql_name='tickSpacing')
    tick_spacing_not = sgqlc.types.Field(BigInt, graphql_name='tickSpacing_not')
    tick_spacing_gt = sgqlc.types.Field(BigInt, graphql_name='tickSpacing_gt')
    tick_spacing_lt = sgqlc.types.Field(BigInt, graphql_name='tickSpacing_lt')
    tick_spacing_gte = sgqlc.types.Field(BigInt, graphql_name='tickSpacing_gte')
    tick_spacing_lte = sgqlc.types.Field(BigInt, graphql_name='tickSpacing_lte')
    tick_spacing_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tickSpacing_in')
    tick_spacing_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tickSpacing_not_in')
    observation_index = sgqlc.types.Field(BigInt, graphql_name='observationIndex')
    observation_index_not = sgqlc.types.Field(BigInt, graphql_name='observationIndex_not')
    observation_index_gt = sgqlc.types.Field(BigInt, graphql_name='observationIndex_gt')
    observation_index_lt = sgqlc.types.Field(BigInt, graphql_name='observationIndex_lt')
    observation_index_gte = sgqlc.types.Field(BigInt, graphql_name='observationIndex_gte')
    observation_index_lte = sgqlc.types.Field(BigInt, graphql_name='observationIndex_lte')
    observation_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='observationIndex_in')
    observation_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='observationIndex_not_in')
    volume_token0 = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0')
    volume_token0_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_not')
    volume_token0_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_gt')
    volume_token0_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_lt')
    volume_token0_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_gte')
    volume_token0_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken0_lte')
    volume_token0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken0_in')
    volume_token0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken0_not_in')
    volume_token1 = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1')
    volume_token1_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_not')
    volume_token1_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_gt')
    volume_token1_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_lt')
    volume_token1_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_gte')
    volume_token1_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeToken1_lte')
    volume_token1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken1_in')
    volume_token1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeToken1_not_in')
    volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD')
    volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_not')
    volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gt')
    volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lt')
    volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gte')
    volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lte')
    volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_in')
    volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_not_in')
    untracked_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD')
    untracked_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_not')
    untracked_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gt')
    untracked_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lt')
    untracked_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gte')
    untracked_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lte')
    untracked_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_in')
    untracked_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_not_in')
    fees_usd = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD')
    fees_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_not')
    fees_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gt')
    fees_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lt')
    fees_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gte')
    fees_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lte')
    fees_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_in')
    fees_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_not_in')
    tx_count = sgqlc.types.Field(BigInt, graphql_name='txCount')
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name='txCount_not')
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name='txCount_gt')
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name='txCount_lt')
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name='txCount_gte')
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name='txCount_lte')
    tx_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_in')
    tx_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_not_in')
    collected_fees_token0 = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken0')
    collected_fees_token0_not = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken0_not')
    collected_fees_token0_gt = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken0_gt')
    collected_fees_token0_lt = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken0_lt')
    collected_fees_token0_gte = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken0_gte')
    collected_fees_token0_lte = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken0_lte')
    collected_fees_token0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='collectedFeesToken0_in')
    collected_fees_token0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='collectedFeesToken0_not_in')
    collected_fees_token1 = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken1')
    collected_fees_token1_not = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken1_not')
    collected_fees_token1_gt = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken1_gt')
    collected_fees_token1_lt = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken1_lt')
    collected_fees_token1_gte = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken1_gte')
    collected_fees_token1_lte = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesToken1_lte')
    collected_fees_token1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='collectedFeesToken1_in')
    collected_fees_token1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='collectedFeesToken1_not_in')
    collected_fees_usd = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesUSD')
    collected_fees_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesUSD_not')
    collected_fees_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesUSD_gt')
    collected_fees_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesUSD_lt')
    collected_fees_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesUSD_gte')
    collected_fees_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='collectedFeesUSD_lte')
    collected_fees_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='collectedFeesUSD_in')
    collected_fees_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='collectedFeesUSD_not_in')
    total_value_locked_token0 = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken0')
    total_value_locked_token0_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken0_not')
    total_value_locked_token0_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken0_gt')
    total_value_locked_token0_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken0_lt')
    total_value_locked_token0_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken0_gte')
    total_value_locked_token0_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken0_lte')
    total_value_locked_token0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedToken0_in')
    total_value_locked_token0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedToken0_not_in')
    total_value_locked_token1 = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken1')
    total_value_locked_token1_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken1_not')
    total_value_locked_token1_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken1_gt')
    total_value_locked_token1_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken1_lt')
    total_value_locked_token1_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken1_gte')
    total_value_locked_token1_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedToken1_lte')
    total_value_locked_token1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedToken1_in')
    total_value_locked_token1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedToken1_not_in')
    total_value_locked_eth = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH')
    total_value_locked_eth_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_not')
    total_value_locked_eth_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_gt')
    total_value_locked_eth_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_lt')
    total_value_locked_eth_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_gte')
    total_value_locked_eth_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedETH_lte')
    total_value_locked_eth_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedETH_in')
    total_value_locked_eth_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedETH_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    total_value_locked_usduntracked = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked')
    total_value_locked_usduntracked_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_not')
    total_value_locked_usduntracked_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_gt')
    total_value_locked_usduntracked_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_lt')
    total_value_locked_usduntracked_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_gte')
    total_value_locked_usduntracked_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_lte')
    total_value_locked_usduntracked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSDUntracked_in')
    total_value_locked_usduntracked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSDUntracked_not_in')
    liquidity_provider_count = sgqlc.types.Field(BigInt, graphql_name='liquidityProviderCount')
    liquidity_provider_count_not = sgqlc.types.Field(BigInt, graphql_name='liquidityProviderCount_not')
    liquidity_provider_count_gt = sgqlc.types.Field(BigInt, graphql_name='liquidityProviderCount_gt')
    liquidity_provider_count_lt = sgqlc.types.Field(BigInt, graphql_name='liquidityProviderCount_lt')
    liquidity_provider_count_gte = sgqlc.types.Field(BigInt, graphql_name='liquidityProviderCount_gte')
    liquidity_provider_count_lte = sgqlc.types.Field(BigInt, graphql_name='liquidityProviderCount_lte')
    liquidity_provider_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidityProviderCount_in')
    liquidity_provider_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidityProviderCount_not_in')
    pool_hour_data_ = sgqlc.types.Field(PoolHourData_filter, graphql_name='poolHourData_')
    pool_day_data_ = sgqlc.types.Field(PoolDayData_filter, graphql_name='poolDayData_')
    hooks = sgqlc.types.Field(String, graphql_name='hooks')
    hooks_not = sgqlc.types.Field(String, graphql_name='hooks_not')
    hooks_gt = sgqlc.types.Field(String, graphql_name='hooks_gt')
    hooks_lt = sgqlc.types.Field(String, graphql_name='hooks_lt')
    hooks_gte = sgqlc.types.Field(String, graphql_name='hooks_gte')
    hooks_lte = sgqlc.types.Field(String, graphql_name='hooks_lte')
    hooks_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hooks_in')
    hooks_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hooks_not_in')
    hooks_contains = sgqlc.types.Field(String, graphql_name='hooks_contains')
    hooks_contains_nocase = sgqlc.types.Field(String, graphql_name='hooks_contains_nocase')
    hooks_not_contains = sgqlc.types.Field(String, graphql_name='hooks_not_contains')
    hooks_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hooks_not_contains_nocase')
    hooks_starts_with = sgqlc.types.Field(String, graphql_name='hooks_starts_with')
    hooks_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hooks_starts_with_nocase')
    hooks_not_starts_with = sgqlc.types.Field(String, graphql_name='hooks_not_starts_with')
    hooks_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hooks_not_starts_with_nocase')
    hooks_ends_with = sgqlc.types.Field(String, graphql_name='hooks_ends_with')
    hooks_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hooks_ends_with_nocase')
    hooks_not_ends_with = sgqlc.types.Field(String, graphql_name='hooks_not_ends_with')
    hooks_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hooks_not_ends_with_nocase')
    modify_liquiditys_ = sgqlc.types.Field(ModifyLiquidity_filter, graphql_name='modifyLiquiditys_')
    swaps_ = sgqlc.types.Field('Swap_filter', graphql_name='swaps_')
    ticks_ = sgqlc.types.Field('Tick_filter', graphql_name='ticks_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Pool_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Pool_filter'), graphql_name='or')


class Position_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'token_id', 'token_id_not', 'token_id_gt', 'token_id_lt', 'token_id_gte', 'token_id_lte', 'token_id_in', 'token_id_not_in', 'owner', 'owner_not', 'owner_gt', 'owner_lt', 'owner_gte', 'owner_lte', 'owner_in', 'owner_not_in', 'owner_contains', 'owner_contains_nocase', 'owner_not_contains', 'owner_not_contains_nocase', 'owner_starts_with', 'owner_starts_with_nocase', 'owner_not_starts_with', 'owner_not_starts_with_nocase', 'owner_ends_with', 'owner_ends_with_nocase', 'owner_not_ends_with', 'owner_not_ends_with_nocase', 'origin', 'origin_not', 'origin_gt', 'origin_lt', 'origin_gte', 'origin_lte', 'origin_in', 'origin_not_in', 'origin_contains', 'origin_contains_nocase', 'origin_not_contains', 'origin_not_contains_nocase', 'origin_starts_with', 'origin_starts_with_nocase', 'origin_not_starts_with', 'origin_not_starts_with_nocase', 'origin_ends_with', 'origin_ends_with_nocase', 'origin_not_ends_with', 'origin_not_ends_with_nocase', 'created_at_timestamp', 'created_at_timestamp_not', 'created_at_timestamp_gt', 'created_at_timestamp_lt', 'created_at_timestamp_gte', 'created_at_timestamp_lte', 'created_at_timestamp_in', 'created_at_timestamp_not_in', 'subscriptions_', 'unsubscriptions_', 'transfers_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    token_id = sgqlc.types.Field(BigInt, graphql_name='tokenId')
    token_id_not = sgqlc.types.Field(BigInt, graphql_name='tokenId_not')
    token_id_gt = sgqlc.types.Field(BigInt, graphql_name='tokenId_gt')
    token_id_lt = sgqlc.types.Field(BigInt, graphql_name='tokenId_lt')
    token_id_gte = sgqlc.types.Field(BigInt, graphql_name='tokenId_gte')
    token_id_lte = sgqlc.types.Field(BigInt, graphql_name='tokenId_lte')
    token_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenId_in')
    token_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenId_not_in')
    owner = sgqlc.types.Field(String, graphql_name='owner')
    owner_not = sgqlc.types.Field(String, graphql_name='owner_not')
    owner_gt = sgqlc.types.Field(String, graphql_name='owner_gt')
    owner_lt = sgqlc.types.Field(String, graphql_name='owner_lt')
    owner_gte = sgqlc.types.Field(String, graphql_name='owner_gte')
    owner_lte = sgqlc.types.Field(String, graphql_name='owner_lte')
    owner_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='owner_in')
    owner_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='owner_not_in')
    owner_contains = sgqlc.types.Field(String, graphql_name='owner_contains')
    owner_contains_nocase = sgqlc.types.Field(String, graphql_name='owner_contains_nocase')
    owner_not_contains = sgqlc.types.Field(String, graphql_name='owner_not_contains')
    owner_not_contains_nocase = sgqlc.types.Field(String, graphql_name='owner_not_contains_nocase')
    owner_starts_with = sgqlc.types.Field(String, graphql_name='owner_starts_with')
    owner_starts_with_nocase = sgqlc.types.Field(String, graphql_name='owner_starts_with_nocase')
    owner_not_starts_with = sgqlc.types.Field(String, graphql_name='owner_not_starts_with')
    owner_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='owner_not_starts_with_nocase')
    owner_ends_with = sgqlc.types.Field(String, graphql_name='owner_ends_with')
    owner_ends_with_nocase = sgqlc.types.Field(String, graphql_name='owner_ends_with_nocase')
    owner_not_ends_with = sgqlc.types.Field(String, graphql_name='owner_not_ends_with')
    owner_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='owner_not_ends_with_nocase')
    origin = sgqlc.types.Field(String, graphql_name='origin')
    origin_not = sgqlc.types.Field(String, graphql_name='origin_not')
    origin_gt = sgqlc.types.Field(String, graphql_name='origin_gt')
    origin_lt = sgqlc.types.Field(String, graphql_name='origin_lt')
    origin_gte = sgqlc.types.Field(String, graphql_name='origin_gte')
    origin_lte = sgqlc.types.Field(String, graphql_name='origin_lte')
    origin_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='origin_in')
    origin_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='origin_not_in')
    origin_contains = sgqlc.types.Field(String, graphql_name='origin_contains')
    origin_contains_nocase = sgqlc.types.Field(String, graphql_name='origin_contains_nocase')
    origin_not_contains = sgqlc.types.Field(String, graphql_name='origin_not_contains')
    origin_not_contains_nocase = sgqlc.types.Field(String, graphql_name='origin_not_contains_nocase')
    origin_starts_with = sgqlc.types.Field(String, graphql_name='origin_starts_with')
    origin_starts_with_nocase = sgqlc.types.Field(String, graphql_name='origin_starts_with_nocase')
    origin_not_starts_with = sgqlc.types.Field(String, graphql_name='origin_not_starts_with')
    origin_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='origin_not_starts_with_nocase')
    origin_ends_with = sgqlc.types.Field(String, graphql_name='origin_ends_with')
    origin_ends_with_nocase = sgqlc.types.Field(String, graphql_name='origin_ends_with_nocase')
    origin_not_ends_with = sgqlc.types.Field(String, graphql_name='origin_not_ends_with')
    origin_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='origin_not_ends_with_nocase')
    created_at_timestamp = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp')
    created_at_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_not')
    created_at_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_gt')
    created_at_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_lt')
    created_at_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_gte')
    created_at_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_lte')
    created_at_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtTimestamp_in')
    created_at_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtTimestamp_not_in')
    subscriptions_ = sgqlc.types.Field('Subscribe_filter', graphql_name='subscriptions_')
    unsubscriptions_ = sgqlc.types.Field('Unsubscribe_filter', graphql_name='unsubscriptions_')
    transfers_ = sgqlc.types.Field('Transfer_filter', graphql_name='transfers_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Position_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Position_filter'), graphql_name='or')


class Subscribe_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'token_id', 'token_id_not', 'token_id_gt', 'token_id_lt', 'token_id_gte', 'token_id_lte', 'token_id_in', 'token_id_not_in', 'address', 'address_not', 'address_gt', 'address_lt', 'address_gte', 'address_lte', 'address_in', 'address_not_in', 'address_contains', 'address_contains_nocase', 'address_not_contains', 'address_not_contains_nocase', 'address_starts_with', 'address_starts_with_nocase', 'address_not_starts_with', 'address_not_starts_with_nocase', 'address_ends_with', 'address_ends_with_nocase', 'address_not_ends_with', 'address_not_ends_with_nocase', 'transaction', 'transaction_not', 'transaction_gt', 'transaction_lt', 'transaction_gte', 'transaction_lte', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_contains_nocase', 'transaction_not_contains', 'transaction_not_contains_nocase', 'transaction_starts_with', 'transaction_starts_with_nocase', 'transaction_not_starts_with', 'transaction_not_starts_with_nocase', 'transaction_ends_with', 'transaction_ends_with_nocase', 'transaction_not_ends_with', 'transaction_not_ends_with_nocase', 'transaction_', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'origin', 'origin_not', 'origin_gt', 'origin_lt', 'origin_gte', 'origin_lte', 'origin_in', 'origin_not_in', 'origin_contains', 'origin_contains_nocase', 'origin_not_contains', 'origin_not_contains_nocase', 'origin_starts_with', 'origin_starts_with_nocase', 'origin_not_starts_with', 'origin_not_starts_with_nocase', 'origin_ends_with', 'origin_ends_with_nocase', 'origin_not_ends_with', 'origin_not_ends_with_nocase', 'position', 'position_not', 'position_gt', 'position_lt', 'position_gte', 'position_lte', 'position_in', 'position_not_in', 'position_contains', 'position_contains_nocase', 'position_not_contains', 'position_not_contains_nocase', 'position_starts_with', 'position_starts_with_nocase', 'position_not_starts_with', 'position_not_starts_with_nocase', 'position_ends_with', 'position_ends_with_nocase', 'position_not_ends_with', 'position_not_ends_with_nocase', 'position_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    token_id = sgqlc.types.Field(BigInt, graphql_name='tokenId')
    token_id_not = sgqlc.types.Field(BigInt, graphql_name='tokenId_not')
    token_id_gt = sgqlc.types.Field(BigInt, graphql_name='tokenId_gt')
    token_id_lt = sgqlc.types.Field(BigInt, graphql_name='tokenId_lt')
    token_id_gte = sgqlc.types.Field(BigInt, graphql_name='tokenId_gte')
    token_id_lte = sgqlc.types.Field(BigInt, graphql_name='tokenId_lte')
    token_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenId_in')
    token_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenId_not_in')
    address = sgqlc.types.Field(String, graphql_name='address')
    address_not = sgqlc.types.Field(String, graphql_name='address_not')
    address_gt = sgqlc.types.Field(String, graphql_name='address_gt')
    address_lt = sgqlc.types.Field(String, graphql_name='address_lt')
    address_gte = sgqlc.types.Field(String, graphql_name='address_gte')
    address_lte = sgqlc.types.Field(String, graphql_name='address_lte')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(String, graphql_name='address_contains')
    address_contains_nocase = sgqlc.types.Field(String, graphql_name='address_contains_nocase')
    address_not_contains = sgqlc.types.Field(String, graphql_name='address_not_contains')
    address_not_contains_nocase = sgqlc.types.Field(String, graphql_name='address_not_contains_nocase')
    address_starts_with = sgqlc.types.Field(String, graphql_name='address_starts_with')
    address_starts_with_nocase = sgqlc.types.Field(String, graphql_name='address_starts_with_nocase')
    address_not_starts_with = sgqlc.types.Field(String, graphql_name='address_not_starts_with')
    address_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='address_not_starts_with_nocase')
    address_ends_with = sgqlc.types.Field(String, graphql_name='address_ends_with')
    address_ends_with_nocase = sgqlc.types.Field(String, graphql_name='address_ends_with_nocase')
    address_not_ends_with = sgqlc.types.Field(String, graphql_name='address_not_ends_with')
    address_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='address_not_ends_with_nocase')
    transaction = sgqlc.types.Field(String, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(String, graphql_name='transaction_not')
    transaction_gt = sgqlc.types.Field(String, graphql_name='transaction_gt')
    transaction_lt = sgqlc.types.Field(String, graphql_name='transaction_lt')
    transaction_gte = sgqlc.types.Field(String, graphql_name='transaction_gte')
    transaction_lte = sgqlc.types.Field(String, graphql_name='transaction_lte')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(String, graphql_name='transaction_contains')
    transaction_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_contains_nocase')
    transaction_not_contains = sgqlc.types.Field(String, graphql_name='transaction_not_contains')
    transaction_not_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_contains_nocase')
    transaction_starts_with = sgqlc.types.Field(String, graphql_name='transaction_starts_with')
    transaction_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_starts_with_nocase')
    transaction_not_starts_with = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with')
    transaction_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with_nocase')
    transaction_ends_with = sgqlc.types.Field(String, graphql_name='transaction_ends_with')
    transaction_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_ends_with_nocase')
    transaction_not_ends_with = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with')
    transaction_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with_nocase')
    transaction_ = sgqlc.types.Field('Transaction_filter', graphql_name='transaction_')
    log_index = sgqlc.types.Field(BigInt, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(BigInt, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(BigInt, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(BigInt, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(BigInt, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(BigInt, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    origin = sgqlc.types.Field(String, graphql_name='origin')
    origin_not = sgqlc.types.Field(String, graphql_name='origin_not')
    origin_gt = sgqlc.types.Field(String, graphql_name='origin_gt')
    origin_lt = sgqlc.types.Field(String, graphql_name='origin_lt')
    origin_gte = sgqlc.types.Field(String, graphql_name='origin_gte')
    origin_lte = sgqlc.types.Field(String, graphql_name='origin_lte')
    origin_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='origin_in')
    origin_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='origin_not_in')
    origin_contains = sgqlc.types.Field(String, graphql_name='origin_contains')
    origin_contains_nocase = sgqlc.types.Field(String, graphql_name='origin_contains_nocase')
    origin_not_contains = sgqlc.types.Field(String, graphql_name='origin_not_contains')
    origin_not_contains_nocase = sgqlc.types.Field(String, graphql_name='origin_not_contains_nocase')
    origin_starts_with = sgqlc.types.Field(String, graphql_name='origin_starts_with')
    origin_starts_with_nocase = sgqlc.types.Field(String, graphql_name='origin_starts_with_nocase')
    origin_not_starts_with = sgqlc.types.Field(String, graphql_name='origin_not_starts_with')
    origin_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='origin_not_starts_with_nocase')
    origin_ends_with = sgqlc.types.Field(String, graphql_name='origin_ends_with')
    origin_ends_with_nocase = sgqlc.types.Field(String, graphql_name='origin_ends_with_nocase')
    origin_not_ends_with = sgqlc.types.Field(String, graphql_name='origin_not_ends_with')
    origin_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='origin_not_ends_with_nocase')
    position = sgqlc.types.Field(String, graphql_name='position')
    position_not = sgqlc.types.Field(String, graphql_name='position_not')
    position_gt = sgqlc.types.Field(String, graphql_name='position_gt')
    position_lt = sgqlc.types.Field(String, graphql_name='position_lt')
    position_gte = sgqlc.types.Field(String, graphql_name='position_gte')
    position_lte = sgqlc.types.Field(String, graphql_name='position_lte')
    position_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='position_in')
    position_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='position_not_in')
    position_contains = sgqlc.types.Field(String, graphql_name='position_contains')
    position_contains_nocase = sgqlc.types.Field(String, graphql_name='position_contains_nocase')
    position_not_contains = sgqlc.types.Field(String, graphql_name='position_not_contains')
    position_not_contains_nocase = sgqlc.types.Field(String, graphql_name='position_not_contains_nocase')
    position_starts_with = sgqlc.types.Field(String, graphql_name='position_starts_with')
    position_starts_with_nocase = sgqlc.types.Field(String, graphql_name='position_starts_with_nocase')
    position_not_starts_with = sgqlc.types.Field(String, graphql_name='position_not_starts_with')
    position_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='position_not_starts_with_nocase')
    position_ends_with = sgqlc.types.Field(String, graphql_name='position_ends_with')
    position_ends_with_nocase = sgqlc.types.Field(String, graphql_name='position_ends_with_nocase')
    position_not_ends_with = sgqlc.types.Field(String, graphql_name='position_not_ends_with')
    position_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='position_not_ends_with_nocase')
    position_ = sgqlc.types.Field(Position_filter, graphql_name='position_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Subscribe_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Subscribe_filter'), graphql_name='or')


class Swap_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'transaction', 'transaction_not', 'transaction_gt', 'transaction_lt', 'transaction_gte', 'transaction_lte', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_contains_nocase', 'transaction_not_contains', 'transaction_not_contains_nocase', 'transaction_starts_with', 'transaction_starts_with_nocase', 'transaction_not_starts_with', 'transaction_not_starts_with_nocase', 'transaction_ends_with', 'transaction_ends_with_nocase', 'transaction_not_ends_with', 'transaction_not_ends_with_nocase', 'transaction_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'token0', 'token0_not', 'token0_gt', 'token0_lt', 'token0_gte', 'token0_lte', 'token0_in', 'token0_not_in', 'token0_contains', 'token0_contains_nocase', 'token0_not_contains', 'token0_not_contains_nocase', 'token0_starts_with', 'token0_starts_with_nocase', 'token0_not_starts_with', 'token0_not_starts_with_nocase', 'token0_ends_with', 'token0_ends_with_nocase', 'token0_not_ends_with', 'token0_not_ends_with_nocase', 'token0_', 'token1', 'token1_not', 'token1_gt', 'token1_lt', 'token1_gte', 'token1_lte', 'token1_in', 'token1_not_in', 'token1_contains', 'token1_contains_nocase', 'token1_not_contains', 'token1_not_contains_nocase', 'token1_starts_with', 'token1_starts_with_nocase', 'token1_not_starts_with', 'token1_not_starts_with_nocase', 'token1_ends_with', 'token1_ends_with_nocase', 'token1_not_ends_with', 'token1_not_ends_with_nocase', 'token1_', 'sender', 'sender_not', 'sender_gt', 'sender_lt', 'sender_gte', 'sender_lte', 'sender_in', 'sender_not_in', 'sender_contains', 'sender_not_contains', 'origin', 'origin_not', 'origin_gt', 'origin_lt', 'origin_gte', 'origin_lte', 'origin_in', 'origin_not_in', 'origin_contains', 'origin_not_contains', 'amount0', 'amount0_not', 'amount0_gt', 'amount0_lt', 'amount0_gte', 'amount0_lte', 'amount0_in', 'amount0_not_in', 'amount1', 'amount1_not', 'amount1_gt', 'amount1_lt', 'amount1_gte', 'amount1_lte', 'amount1_in', 'amount1_not_in', 'amount_usd', 'amount_usd_not', 'amount_usd_gt', 'amount_usd_lt', 'amount_usd_gte', 'amount_usd_lte', 'amount_usd_in', 'amount_usd_not_in', 'sqrt_price_x96', 'sqrt_price_x96_not', 'sqrt_price_x96_gt', 'sqrt_price_x96_lt', 'sqrt_price_x96_gte', 'sqrt_price_x96_lte', 'sqrt_price_x96_in', 'sqrt_price_x96_not_in', 'tick', 'tick_not', 'tick_gt', 'tick_lt', 'tick_gte', 'tick_lte', 'tick_in', 'tick_not_in', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    transaction = sgqlc.types.Field(String, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(String, graphql_name='transaction_not')
    transaction_gt = sgqlc.types.Field(String, graphql_name='transaction_gt')
    transaction_lt = sgqlc.types.Field(String, graphql_name='transaction_lt')
    transaction_gte = sgqlc.types.Field(String, graphql_name='transaction_gte')
    transaction_lte = sgqlc.types.Field(String, graphql_name='transaction_lte')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(String, graphql_name='transaction_contains')
    transaction_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_contains_nocase')
    transaction_not_contains = sgqlc.types.Field(String, graphql_name='transaction_not_contains')
    transaction_not_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_contains_nocase')
    transaction_starts_with = sgqlc.types.Field(String, graphql_name='transaction_starts_with')
    transaction_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_starts_with_nocase')
    transaction_not_starts_with = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with')
    transaction_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with_nocase')
    transaction_ends_with = sgqlc.types.Field(String, graphql_name='transaction_ends_with')
    transaction_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_ends_with_nocase')
    transaction_not_ends_with = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with')
    transaction_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with_nocase')
    transaction_ = sgqlc.types.Field('Transaction_filter', graphql_name='transaction_')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field(Pool_filter, graphql_name='pool_')
    token0 = sgqlc.types.Field(String, graphql_name='token0')
    token0_not = sgqlc.types.Field(String, graphql_name='token0_not')
    token0_gt = sgqlc.types.Field(String, graphql_name='token0_gt')
    token0_lt = sgqlc.types.Field(String, graphql_name='token0_lt')
    token0_gte = sgqlc.types.Field(String, graphql_name='token0_gte')
    token0_lte = sgqlc.types.Field(String, graphql_name='token0_lte')
    token0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token0_in')
    token0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token0_not_in')
    token0_contains = sgqlc.types.Field(String, graphql_name='token0_contains')
    token0_contains_nocase = sgqlc.types.Field(String, graphql_name='token0_contains_nocase')
    token0_not_contains = sgqlc.types.Field(String, graphql_name='token0_not_contains')
    token0_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token0_not_contains_nocase')
    token0_starts_with = sgqlc.types.Field(String, graphql_name='token0_starts_with')
    token0_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token0_starts_with_nocase')
    token0_not_starts_with = sgqlc.types.Field(String, graphql_name='token0_not_starts_with')
    token0_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token0_not_starts_with_nocase')
    token0_ends_with = sgqlc.types.Field(String, graphql_name='token0_ends_with')
    token0_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token0_ends_with_nocase')
    token0_not_ends_with = sgqlc.types.Field(String, graphql_name='token0_not_ends_with')
    token0_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token0_not_ends_with_nocase')
    token0_ = sgqlc.types.Field('Token_filter', graphql_name='token0_')
    token1 = sgqlc.types.Field(String, graphql_name='token1')
    token1_not = sgqlc.types.Field(String, graphql_name='token1_not')
    token1_gt = sgqlc.types.Field(String, graphql_name='token1_gt')
    token1_lt = sgqlc.types.Field(String, graphql_name='token1_lt')
    token1_gte = sgqlc.types.Field(String, graphql_name='token1_gte')
    token1_lte = sgqlc.types.Field(String, graphql_name='token1_lte')
    token1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token1_in')
    token1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token1_not_in')
    token1_contains = sgqlc.types.Field(String, graphql_name='token1_contains')
    token1_contains_nocase = sgqlc.types.Field(String, graphql_name='token1_contains_nocase')
    token1_not_contains = sgqlc.types.Field(String, graphql_name='token1_not_contains')
    token1_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token1_not_contains_nocase')
    token1_starts_with = sgqlc.types.Field(String, graphql_name='token1_starts_with')
    token1_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token1_starts_with_nocase')
    token1_not_starts_with = sgqlc.types.Field(String, graphql_name='token1_not_starts_with')
    token1_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token1_not_starts_with_nocase')
    token1_ends_with = sgqlc.types.Field(String, graphql_name='token1_ends_with')
    token1_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token1_ends_with_nocase')
    token1_not_ends_with = sgqlc.types.Field(String, graphql_name='token1_not_ends_with')
    token1_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token1_not_ends_with_nocase')
    token1_ = sgqlc.types.Field('Token_filter', graphql_name='token1_')
    sender = sgqlc.types.Field(Bytes, graphql_name='sender')
    sender_not = sgqlc.types.Field(Bytes, graphql_name='sender_not')
    sender_gt = sgqlc.types.Field(Bytes, graphql_name='sender_gt')
    sender_lt = sgqlc.types.Field(Bytes, graphql_name='sender_lt')
    sender_gte = sgqlc.types.Field(Bytes, graphql_name='sender_gte')
    sender_lte = sgqlc.types.Field(Bytes, graphql_name='sender_lte')
    sender_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sender_in')
    sender_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='sender_not_in')
    sender_contains = sgqlc.types.Field(Bytes, graphql_name='sender_contains')
    sender_not_contains = sgqlc.types.Field(Bytes, graphql_name='sender_not_contains')
    origin = sgqlc.types.Field(Bytes, graphql_name='origin')
    origin_not = sgqlc.types.Field(Bytes, graphql_name='origin_not')
    origin_gt = sgqlc.types.Field(Bytes, graphql_name='origin_gt')
    origin_lt = sgqlc.types.Field(Bytes, graphql_name='origin_lt')
    origin_gte = sgqlc.types.Field(Bytes, graphql_name='origin_gte')
    origin_lte = sgqlc.types.Field(Bytes, graphql_name='origin_lte')
    origin_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='origin_in')
    origin_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='origin_not_in')
    origin_contains = sgqlc.types.Field(Bytes, graphql_name='origin_contains')
    origin_not_contains = sgqlc.types.Field(Bytes, graphql_name='origin_not_contains')
    amount0 = sgqlc.types.Field(BigDecimal, graphql_name='amount0')
    amount0_not = sgqlc.types.Field(BigDecimal, graphql_name='amount0_not')
    amount0_gt = sgqlc.types.Field(BigDecimal, graphql_name='amount0_gt')
    amount0_lt = sgqlc.types.Field(BigDecimal, graphql_name='amount0_lt')
    amount0_gte = sgqlc.types.Field(BigDecimal, graphql_name='amount0_gte')
    amount0_lte = sgqlc.types.Field(BigDecimal, graphql_name='amount0_lte')
    amount0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount0_in')
    amount0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount0_not_in')
    amount1 = sgqlc.types.Field(BigDecimal, graphql_name='amount1')
    amount1_not = sgqlc.types.Field(BigDecimal, graphql_name='amount1_not')
    amount1_gt = sgqlc.types.Field(BigDecimal, graphql_name='amount1_gt')
    amount1_lt = sgqlc.types.Field(BigDecimal, graphql_name='amount1_lt')
    amount1_gte = sgqlc.types.Field(BigDecimal, graphql_name='amount1_gte')
    amount1_lte = sgqlc.types.Field(BigDecimal, graphql_name='amount1_lte')
    amount1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount1_in')
    amount1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount1_not_in')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_not')
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gt')
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lt')
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gte')
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lte')
    amount_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_in')
    amount_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_not_in')
    sqrt_price_x96 = sgqlc.types.Field(BigInt, graphql_name='sqrtPriceX96')
    sqrt_price_x96_not = sgqlc.types.Field(BigInt, graphql_name='sqrtPriceX96_not')
    sqrt_price_x96_gt = sgqlc.types.Field(BigInt, graphql_name='sqrtPriceX96_gt')
    sqrt_price_x96_lt = sgqlc.types.Field(BigInt, graphql_name='sqrtPriceX96_lt')
    sqrt_price_x96_gte = sgqlc.types.Field(BigInt, graphql_name='sqrtPriceX96_gte')
    sqrt_price_x96_lte = sgqlc.types.Field(BigInt, graphql_name='sqrtPriceX96_lte')
    sqrt_price_x96_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sqrtPriceX96_in')
    sqrt_price_x96_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='sqrtPriceX96_not_in')
    tick = sgqlc.types.Field(BigInt, graphql_name='tick')
    tick_not = sgqlc.types.Field(BigInt, graphql_name='tick_not')
    tick_gt = sgqlc.types.Field(BigInt, graphql_name='tick_gt')
    tick_lt = sgqlc.types.Field(BigInt, graphql_name='tick_lt')
    tick_gte = sgqlc.types.Field(BigInt, graphql_name='tick_gte')
    tick_lte = sgqlc.types.Field(BigInt, graphql_name='tick_lte')
    tick_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tick_in')
    tick_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tick_not_in')
    log_index = sgqlc.types.Field(BigInt, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(BigInt, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(BigInt, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(BigInt, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(BigInt, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(BigInt, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Swap_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Swap_filter'), graphql_name='or')


class Tick_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_address', 'pool_address_not', 'pool_address_gt', 'pool_address_lt', 'pool_address_gte', 'pool_address_lte', 'pool_address_in', 'pool_address_not_in', 'pool_address_contains', 'pool_address_contains_nocase', 'pool_address_not_contains', 'pool_address_not_contains_nocase', 'pool_address_starts_with', 'pool_address_starts_with_nocase', 'pool_address_not_starts_with', 'pool_address_not_starts_with_nocase', 'pool_address_ends_with', 'pool_address_ends_with_nocase', 'pool_address_not_ends_with', 'pool_address_not_ends_with_nocase', 'tick_idx', 'tick_idx_not', 'tick_idx_gt', 'tick_idx_lt', 'tick_idx_gte', 'tick_idx_lte', 'tick_idx_in', 'tick_idx_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'liquidity_gross', 'liquidity_gross_not', 'liquidity_gross_gt', 'liquidity_gross_lt', 'liquidity_gross_gte', 'liquidity_gross_lte', 'liquidity_gross_in', 'liquidity_gross_not_in', 'liquidity_net', 'liquidity_net_not', 'liquidity_net_gt', 'liquidity_net_lt', 'liquidity_net_gte', 'liquidity_net_lte', 'liquidity_net_in', 'liquidity_net_not_in', 'price0', 'price0_not', 'price0_gt', 'price0_lt', 'price0_gte', 'price0_lte', 'price0_in', 'price0_not_in', 'price1', 'price1_not', 'price1_gt', 'price1_lt', 'price1_gte', 'price1_lte', 'price1_in', 'price1_not_in', 'created_at_timestamp', 'created_at_timestamp_not', 'created_at_timestamp_gt', 'created_at_timestamp_lt', 'created_at_timestamp_gte', 'created_at_timestamp_lte', 'created_at_timestamp_in', 'created_at_timestamp_not_in', 'created_at_block_number', 'created_at_block_number_not', 'created_at_block_number_gt', 'created_at_block_number_lt', 'created_at_block_number_gte', 'created_at_block_number_lte', 'created_at_block_number_in', 'created_at_block_number_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool_address = sgqlc.types.Field(String, graphql_name='poolAddress')
    pool_address_not = sgqlc.types.Field(String, graphql_name='poolAddress_not')
    pool_address_gt = sgqlc.types.Field(String, graphql_name='poolAddress_gt')
    pool_address_lt = sgqlc.types.Field(String, graphql_name='poolAddress_lt')
    pool_address_gte = sgqlc.types.Field(String, graphql_name='poolAddress_gte')
    pool_address_lte = sgqlc.types.Field(String, graphql_name='poolAddress_lte')
    pool_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolAddress_in')
    pool_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolAddress_not_in')
    pool_address_contains = sgqlc.types.Field(String, graphql_name='poolAddress_contains')
    pool_address_contains_nocase = sgqlc.types.Field(String, graphql_name='poolAddress_contains_nocase')
    pool_address_not_contains = sgqlc.types.Field(String, graphql_name='poolAddress_not_contains')
    pool_address_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolAddress_not_contains_nocase')
    pool_address_starts_with = sgqlc.types.Field(String, graphql_name='poolAddress_starts_with')
    pool_address_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolAddress_starts_with_nocase')
    pool_address_not_starts_with = sgqlc.types.Field(String, graphql_name='poolAddress_not_starts_with')
    pool_address_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolAddress_not_starts_with_nocase')
    pool_address_ends_with = sgqlc.types.Field(String, graphql_name='poolAddress_ends_with')
    pool_address_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolAddress_ends_with_nocase')
    pool_address_not_ends_with = sgqlc.types.Field(String, graphql_name='poolAddress_not_ends_with')
    pool_address_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolAddress_not_ends_with_nocase')
    tick_idx = sgqlc.types.Field(BigInt, graphql_name='tickIdx')
    tick_idx_not = sgqlc.types.Field(BigInt, graphql_name='tickIdx_not')
    tick_idx_gt = sgqlc.types.Field(BigInt, graphql_name='tickIdx_gt')
    tick_idx_lt = sgqlc.types.Field(BigInt, graphql_name='tickIdx_lt')
    tick_idx_gte = sgqlc.types.Field(BigInt, graphql_name='tickIdx_gte')
    tick_idx_lte = sgqlc.types.Field(BigInt, graphql_name='tickIdx_lte')
    tick_idx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tickIdx_in')
    tick_idx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tickIdx_not_in')
    pool = sgqlc.types.Field(String, graphql_name='pool')
    pool_not = sgqlc.types.Field(String, graphql_name='pool_not')
    pool_gt = sgqlc.types.Field(String, graphql_name='pool_gt')
    pool_lt = sgqlc.types.Field(String, graphql_name='pool_lt')
    pool_gte = sgqlc.types.Field(String, graphql_name='pool_gte')
    pool_lte = sgqlc.types.Field(String, graphql_name='pool_lte')
    pool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_in')
    pool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pool_not_in')
    pool_contains = sgqlc.types.Field(String, graphql_name='pool_contains')
    pool_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_contains_nocase')
    pool_not_contains = sgqlc.types.Field(String, graphql_name='pool_not_contains')
    pool_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pool_not_contains_nocase')
    pool_starts_with = sgqlc.types.Field(String, graphql_name='pool_starts_with')
    pool_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_starts_with_nocase')
    pool_not_starts_with = sgqlc.types.Field(String, graphql_name='pool_not_starts_with')
    pool_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_starts_with_nocase')
    pool_ends_with = sgqlc.types.Field(String, graphql_name='pool_ends_with')
    pool_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_ends_with_nocase')
    pool_not_ends_with = sgqlc.types.Field(String, graphql_name='pool_not_ends_with')
    pool_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pool_not_ends_with_nocase')
    pool_ = sgqlc.types.Field(Pool_filter, graphql_name='pool_')
    liquidity_gross = sgqlc.types.Field(BigInt, graphql_name='liquidityGross')
    liquidity_gross_not = sgqlc.types.Field(BigInt, graphql_name='liquidityGross_not')
    liquidity_gross_gt = sgqlc.types.Field(BigInt, graphql_name='liquidityGross_gt')
    liquidity_gross_lt = sgqlc.types.Field(BigInt, graphql_name='liquidityGross_lt')
    liquidity_gross_gte = sgqlc.types.Field(BigInt, graphql_name='liquidityGross_gte')
    liquidity_gross_lte = sgqlc.types.Field(BigInt, graphql_name='liquidityGross_lte')
    liquidity_gross_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidityGross_in')
    liquidity_gross_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidityGross_not_in')
    liquidity_net = sgqlc.types.Field(BigInt, graphql_name='liquidityNet')
    liquidity_net_not = sgqlc.types.Field(BigInt, graphql_name='liquidityNet_not')
    liquidity_net_gt = sgqlc.types.Field(BigInt, graphql_name='liquidityNet_gt')
    liquidity_net_lt = sgqlc.types.Field(BigInt, graphql_name='liquidityNet_lt')
    liquidity_net_gte = sgqlc.types.Field(BigInt, graphql_name='liquidityNet_gte')
    liquidity_net_lte = sgqlc.types.Field(BigInt, graphql_name='liquidityNet_lte')
    liquidity_net_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidityNet_in')
    liquidity_net_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='liquidityNet_not_in')
    price0 = sgqlc.types.Field(BigDecimal, graphql_name='price0')
    price0_not = sgqlc.types.Field(BigDecimal, graphql_name='price0_not')
    price0_gt = sgqlc.types.Field(BigDecimal, graphql_name='price0_gt')
    price0_lt = sgqlc.types.Field(BigDecimal, graphql_name='price0_lt')
    price0_gte = sgqlc.types.Field(BigDecimal, graphql_name='price0_gte')
    price0_lte = sgqlc.types.Field(BigDecimal, graphql_name='price0_lte')
    price0_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='price0_in')
    price0_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='price0_not_in')
    price1 = sgqlc.types.Field(BigDecimal, graphql_name='price1')
    price1_not = sgqlc.types.Field(BigDecimal, graphql_name='price1_not')
    price1_gt = sgqlc.types.Field(BigDecimal, graphql_name='price1_gt')
    price1_lt = sgqlc.types.Field(BigDecimal, graphql_name='price1_lt')
    price1_gte = sgqlc.types.Field(BigDecimal, graphql_name='price1_gte')
    price1_lte = sgqlc.types.Field(BigDecimal, graphql_name='price1_lte')
    price1_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='price1_in')
    price1_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='price1_not_in')
    created_at_timestamp = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp')
    created_at_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_not')
    created_at_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_gt')
    created_at_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_lt')
    created_at_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_gte')
    created_at_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='createdAtTimestamp_lte')
    created_at_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtTimestamp_in')
    created_at_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtTimestamp_not_in')
    created_at_block_number = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber')
    created_at_block_number_not = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_not')
    created_at_block_number_gt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_gt')
    created_at_block_number_lt = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_lt')
    created_at_block_number_gte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_gte')
    created_at_block_number_lte = sgqlc.types.Field(BigInt, graphql_name='createdAtBlockNumber_lte')
    created_at_block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlockNumber_in')
    created_at_block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdAtBlockNumber_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Tick_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Tick_filter'), graphql_name='or')


class TokenDayData_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'date', 'date_not', 'date_gt', 'date_lt', 'date_gte', 'date_lte', 'date_in', 'date_not_in', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'token_', 'volume', 'volume_not', 'volume_gt', 'volume_lt', 'volume_gte', 'volume_lte', 'volume_in', 'volume_not_in', 'volume_usd', 'volume_usd_not', 'volume_usd_gt', 'volume_usd_lt', 'volume_usd_gte', 'volume_usd_lte', 'volume_usd_in', 'volume_usd_not_in', 'untracked_volume_usd', 'untracked_volume_usd_not', 'untracked_volume_usd_gt', 'untracked_volume_usd_lt', 'untracked_volume_usd_gte', 'untracked_volume_usd_lte', 'untracked_volume_usd_in', 'untracked_volume_usd_not_in', 'total_value_locked', 'total_value_locked_not', 'total_value_locked_gt', 'total_value_locked_lt', 'total_value_locked_gte', 'total_value_locked_lte', 'total_value_locked_in', 'total_value_locked_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'price_usd', 'price_usd_not', 'price_usd_gt', 'price_usd_lt', 'price_usd_gte', 'price_usd_lte', 'price_usd_in', 'price_usd_not_in', 'fees_usd', 'fees_usd_not', 'fees_usd_gt', 'fees_usd_lt', 'fees_usd_gte', 'fees_usd_lte', 'fees_usd_in', 'fees_usd_not_in', 'open', 'open_not', 'open_gt', 'open_lt', 'open_gte', 'open_lte', 'open_in', 'open_not_in', 'high', 'high_not', 'high_gt', 'high_lt', 'high_gte', 'high_lte', 'high_in', 'high_not_in', 'low', 'low_not', 'low_gt', 'low_lt', 'low_gte', 'low_lte', 'low_in', 'low_not_in', 'close', 'close_not', 'close_gt', 'close_lt', 'close_gte', 'close_lte', 'close_in', 'close_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    date = sgqlc.types.Field(Int, graphql_name='date')
    date_not = sgqlc.types.Field(Int, graphql_name='date_not')
    date_gt = sgqlc.types.Field(Int, graphql_name='date_gt')
    date_lt = sgqlc.types.Field(Int, graphql_name='date_lt')
    date_gte = sgqlc.types.Field(Int, graphql_name='date_gte')
    date_lte = sgqlc.types.Field(Int, graphql_name='date_lte')
    date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='date_in')
    date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='date_not_in')
    token = sgqlc.types.Field(String, graphql_name='token')
    token_not = sgqlc.types.Field(String, graphql_name='token_not')
    token_gt = sgqlc.types.Field(String, graphql_name='token_gt')
    token_lt = sgqlc.types.Field(String, graphql_name='token_lt')
    token_gte = sgqlc.types.Field(String, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(String, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_in')
    token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_not_in')
    token_contains = sgqlc.types.Field(String, graphql_name='token_contains')
    token_contains_nocase = sgqlc.types.Field(String, graphql_name='token_contains_nocase')
    token_not_contains = sgqlc.types.Field(String, graphql_name='token_not_contains')
    token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token_not_contains_nocase')
    token_starts_with = sgqlc.types.Field(String, graphql_name='token_starts_with')
    token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_starts_with_nocase')
    token_not_starts_with = sgqlc.types.Field(String, graphql_name='token_not_starts_with')
    token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_starts_with_nocase')
    token_ends_with = sgqlc.types.Field(String, graphql_name='token_ends_with')
    token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_ends_with_nocase')
    token_not_ends_with = sgqlc.types.Field(String, graphql_name='token_not_ends_with')
    token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_ends_with_nocase')
    token_ = sgqlc.types.Field('Token_filter', graphql_name='token_')
    volume = sgqlc.types.Field(BigDecimal, graphql_name='volume')
    volume_not = sgqlc.types.Field(BigDecimal, graphql_name='volume_not')
    volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='volume_gt')
    volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='volume_lt')
    volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='volume_gte')
    volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='volume_lte')
    volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_in')
    volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_not_in')
    volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD')
    volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_not')
    volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gt')
    volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lt')
    volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gte')
    volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lte')
    volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_in')
    volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_not_in')
    untracked_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD')
    untracked_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_not')
    untracked_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gt')
    untracked_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lt')
    untracked_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gte')
    untracked_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lte')
    untracked_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_in')
    untracked_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_not_in')
    total_value_locked = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked')
    total_value_locked_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_not')
    total_value_locked_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_gt')
    total_value_locked_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_lt')
    total_value_locked_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_gte')
    total_value_locked_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_lte')
    total_value_locked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLocked_in')
    total_value_locked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLocked_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    price_usd = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD')
    price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_not')
    price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_gt')
    price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_lt')
    price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_gte')
    price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_lte')
    price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='priceUSD_in')
    price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='priceUSD_not_in')
    fees_usd = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD')
    fees_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_not')
    fees_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gt')
    fees_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lt')
    fees_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gte')
    fees_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lte')
    fees_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_in')
    fees_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_not_in')
    open = sgqlc.types.Field(BigDecimal, graphql_name='open')
    open_not = sgqlc.types.Field(BigDecimal, graphql_name='open_not')
    open_gt = sgqlc.types.Field(BigDecimal, graphql_name='open_gt')
    open_lt = sgqlc.types.Field(BigDecimal, graphql_name='open_lt')
    open_gte = sgqlc.types.Field(BigDecimal, graphql_name='open_gte')
    open_lte = sgqlc.types.Field(BigDecimal, graphql_name='open_lte')
    open_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='open_in')
    open_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='open_not_in')
    high = sgqlc.types.Field(BigDecimal, graphql_name='high')
    high_not = sgqlc.types.Field(BigDecimal, graphql_name='high_not')
    high_gt = sgqlc.types.Field(BigDecimal, graphql_name='high_gt')
    high_lt = sgqlc.types.Field(BigDecimal, graphql_name='high_lt')
    high_gte = sgqlc.types.Field(BigDecimal, graphql_name='high_gte')
    high_lte = sgqlc.types.Field(BigDecimal, graphql_name='high_lte')
    high_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='high_in')
    high_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='high_not_in')
    low = sgqlc.types.Field(BigDecimal, graphql_name='low')
    low_not = sgqlc.types.Field(BigDecimal, graphql_name='low_not')
    low_gt = sgqlc.types.Field(BigDecimal, graphql_name='low_gt')
    low_lt = sgqlc.types.Field(BigDecimal, graphql_name='low_lt')
    low_gte = sgqlc.types.Field(BigDecimal, graphql_name='low_gte')
    low_lte = sgqlc.types.Field(BigDecimal, graphql_name='low_lte')
    low_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='low_in')
    low_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='low_not_in')
    close = sgqlc.types.Field(BigDecimal, graphql_name='close')
    close_not = sgqlc.types.Field(BigDecimal, graphql_name='close_not')
    close_gt = sgqlc.types.Field(BigDecimal, graphql_name='close_gt')
    close_lt = sgqlc.types.Field(BigDecimal, graphql_name='close_lt')
    close_gte = sgqlc.types.Field(BigDecimal, graphql_name='close_gte')
    close_lte = sgqlc.types.Field(BigDecimal, graphql_name='close_lte')
    close_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='close_in')
    close_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='close_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('TokenDayData_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('TokenDayData_filter'), graphql_name='or')


class TokenHourData_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'period_start_unix', 'period_start_unix_not', 'period_start_unix_gt', 'period_start_unix_lt', 'period_start_unix_gte', 'period_start_unix_lte', 'period_start_unix_in', 'period_start_unix_not_in', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'token_', 'volume', 'volume_not', 'volume_gt', 'volume_lt', 'volume_gte', 'volume_lte', 'volume_in', 'volume_not_in', 'volume_usd', 'volume_usd_not', 'volume_usd_gt', 'volume_usd_lt', 'volume_usd_gte', 'volume_usd_lte', 'volume_usd_in', 'volume_usd_not_in', 'untracked_volume_usd', 'untracked_volume_usd_not', 'untracked_volume_usd_gt', 'untracked_volume_usd_lt', 'untracked_volume_usd_gte', 'untracked_volume_usd_lte', 'untracked_volume_usd_in', 'untracked_volume_usd_not_in', 'total_value_locked', 'total_value_locked_not', 'total_value_locked_gt', 'total_value_locked_lt', 'total_value_locked_gte', 'total_value_locked_lte', 'total_value_locked_in', 'total_value_locked_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'price_usd', 'price_usd_not', 'price_usd_gt', 'price_usd_lt', 'price_usd_gte', 'price_usd_lte', 'price_usd_in', 'price_usd_not_in', 'fees_usd', 'fees_usd_not', 'fees_usd_gt', 'fees_usd_lt', 'fees_usd_gte', 'fees_usd_lte', 'fees_usd_in', 'fees_usd_not_in', 'open', 'open_not', 'open_gt', 'open_lt', 'open_gte', 'open_lte', 'open_in', 'open_not_in', 'high', 'high_not', 'high_gt', 'high_lt', 'high_gte', 'high_lte', 'high_in', 'high_not_in', 'low', 'low_not', 'low_gt', 'low_lt', 'low_gte', 'low_lte', 'low_in', 'low_not_in', 'close', 'close_not', 'close_gt', 'close_lt', 'close_gte', 'close_lte', 'close_in', 'close_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    period_start_unix = sgqlc.types.Field(Int, graphql_name='periodStartUnix')
    period_start_unix_not = sgqlc.types.Field(Int, graphql_name='periodStartUnix_not')
    period_start_unix_gt = sgqlc.types.Field(Int, graphql_name='periodStartUnix_gt')
    period_start_unix_lt = sgqlc.types.Field(Int, graphql_name='periodStartUnix_lt')
    period_start_unix_gte = sgqlc.types.Field(Int, graphql_name='periodStartUnix_gte')
    period_start_unix_lte = sgqlc.types.Field(Int, graphql_name='periodStartUnix_lte')
    period_start_unix_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='periodStartUnix_in')
    period_start_unix_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='periodStartUnix_not_in')
    token = sgqlc.types.Field(String, graphql_name='token')
    token_not = sgqlc.types.Field(String, graphql_name='token_not')
    token_gt = sgqlc.types.Field(String, graphql_name='token_gt')
    token_lt = sgqlc.types.Field(String, graphql_name='token_lt')
    token_gte = sgqlc.types.Field(String, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(String, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_in')
    token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='token_not_in')
    token_contains = sgqlc.types.Field(String, graphql_name='token_contains')
    token_contains_nocase = sgqlc.types.Field(String, graphql_name='token_contains_nocase')
    token_not_contains = sgqlc.types.Field(String, graphql_name='token_not_contains')
    token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='token_not_contains_nocase')
    token_starts_with = sgqlc.types.Field(String, graphql_name='token_starts_with')
    token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_starts_with_nocase')
    token_not_starts_with = sgqlc.types.Field(String, graphql_name='token_not_starts_with')
    token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_starts_with_nocase')
    token_ends_with = sgqlc.types.Field(String, graphql_name='token_ends_with')
    token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_ends_with_nocase')
    token_not_ends_with = sgqlc.types.Field(String, graphql_name='token_not_ends_with')
    token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='token_not_ends_with_nocase')
    token_ = sgqlc.types.Field('Token_filter', graphql_name='token_')
    volume = sgqlc.types.Field(BigDecimal, graphql_name='volume')
    volume_not = sgqlc.types.Field(BigDecimal, graphql_name='volume_not')
    volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='volume_gt')
    volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='volume_lt')
    volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='volume_gte')
    volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='volume_lte')
    volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_in')
    volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_not_in')
    volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD')
    volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_not')
    volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gt')
    volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lt')
    volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gte')
    volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lte')
    volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_in')
    volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_not_in')
    untracked_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD')
    untracked_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_not')
    untracked_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gt')
    untracked_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lt')
    untracked_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gte')
    untracked_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lte')
    untracked_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_in')
    untracked_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_not_in')
    total_value_locked = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked')
    total_value_locked_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_not')
    total_value_locked_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_gt')
    total_value_locked_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_lt')
    total_value_locked_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_gte')
    total_value_locked_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_lte')
    total_value_locked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLocked_in')
    total_value_locked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLocked_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    price_usd = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD')
    price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_not')
    price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_gt')
    price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_lt')
    price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_gte')
    price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='priceUSD_lte')
    price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='priceUSD_in')
    price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='priceUSD_not_in')
    fees_usd = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD')
    fees_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_not')
    fees_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gt')
    fees_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lt')
    fees_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gte')
    fees_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lte')
    fees_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_in')
    fees_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_not_in')
    open = sgqlc.types.Field(BigDecimal, graphql_name='open')
    open_not = sgqlc.types.Field(BigDecimal, graphql_name='open_not')
    open_gt = sgqlc.types.Field(BigDecimal, graphql_name='open_gt')
    open_lt = sgqlc.types.Field(BigDecimal, graphql_name='open_lt')
    open_gte = sgqlc.types.Field(BigDecimal, graphql_name='open_gte')
    open_lte = sgqlc.types.Field(BigDecimal, graphql_name='open_lte')
    open_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='open_in')
    open_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='open_not_in')
    high = sgqlc.types.Field(BigDecimal, graphql_name='high')
    high_not = sgqlc.types.Field(BigDecimal, graphql_name='high_not')
    high_gt = sgqlc.types.Field(BigDecimal, graphql_name='high_gt')
    high_lt = sgqlc.types.Field(BigDecimal, graphql_name='high_lt')
    high_gte = sgqlc.types.Field(BigDecimal, graphql_name='high_gte')
    high_lte = sgqlc.types.Field(BigDecimal, graphql_name='high_lte')
    high_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='high_in')
    high_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='high_not_in')
    low = sgqlc.types.Field(BigDecimal, graphql_name='low')
    low_not = sgqlc.types.Field(BigDecimal, graphql_name='low_not')
    low_gt = sgqlc.types.Field(BigDecimal, graphql_name='low_gt')
    low_lt = sgqlc.types.Field(BigDecimal, graphql_name='low_lt')
    low_gte = sgqlc.types.Field(BigDecimal, graphql_name='low_gte')
    low_lte = sgqlc.types.Field(BigDecimal, graphql_name='low_lte')
    low_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='low_in')
    low_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='low_not_in')
    close = sgqlc.types.Field(BigDecimal, graphql_name='close')
    close_not = sgqlc.types.Field(BigDecimal, graphql_name='close_not')
    close_gt = sgqlc.types.Field(BigDecimal, graphql_name='close_gt')
    close_lt = sgqlc.types.Field(BigDecimal, graphql_name='close_lt')
    close_gte = sgqlc.types.Field(BigDecimal, graphql_name='close_gte')
    close_lte = sgqlc.types.Field(BigDecimal, graphql_name='close_lte')
    close_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='close_in')
    close_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='close_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('TokenHourData_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('TokenHourData_filter'), graphql_name='or')


class Token_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_contains_nocase', 'symbol_not_contains', 'symbol_not_contains_nocase', 'symbol_starts_with', 'symbol_starts_with_nocase', 'symbol_not_starts_with', 'symbol_not_starts_with_nocase', 'symbol_ends_with', 'symbol_ends_with_nocase', 'symbol_not_ends_with', 'symbol_not_ends_with_nocase', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'decimals', 'decimals_not', 'decimals_gt', 'decimals_lt', 'decimals_gte', 'decimals_lte', 'decimals_in', 'decimals_not_in', 'total_supply', 'total_supply_not', 'total_supply_gt', 'total_supply_lt', 'total_supply_gte', 'total_supply_lte', 'total_supply_in', 'total_supply_not_in', 'volume', 'volume_not', 'volume_gt', 'volume_lt', 'volume_gte', 'volume_lte', 'volume_in', 'volume_not_in', 'volume_usd', 'volume_usd_not', 'volume_usd_gt', 'volume_usd_lt', 'volume_usd_gte', 'volume_usd_lte', 'volume_usd_in', 'volume_usd_not_in', 'untracked_volume_usd', 'untracked_volume_usd_not', 'untracked_volume_usd_gt', 'untracked_volume_usd_lt', 'untracked_volume_usd_gte', 'untracked_volume_usd_lte', 'untracked_volume_usd_in', 'untracked_volume_usd_not_in', 'fees_usd', 'fees_usd_not', 'fees_usd_gt', 'fees_usd_lt', 'fees_usd_gte', 'fees_usd_lte', 'fees_usd_in', 'fees_usd_not_in', 'tx_count', 'tx_count_not', 'tx_count_gt', 'tx_count_lt', 'tx_count_gte', 'tx_count_lte', 'tx_count_in', 'tx_count_not_in', 'pool_count', 'pool_count_not', 'pool_count_gt', 'pool_count_lt', 'pool_count_gte', 'pool_count_lte', 'pool_count_in', 'pool_count_not_in', 'total_value_locked', 'total_value_locked_not', 'total_value_locked_gt', 'total_value_locked_lt', 'total_value_locked_gte', 'total_value_locked_lte', 'total_value_locked_in', 'total_value_locked_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'total_value_locked_usduntracked', 'total_value_locked_usduntracked_not', 'total_value_locked_usduntracked_gt', 'total_value_locked_usduntracked_lt', 'total_value_locked_usduntracked_gte', 'total_value_locked_usduntracked_lte', 'total_value_locked_usduntracked_in', 'total_value_locked_usduntracked_not_in', 'derived_eth', 'derived_eth_not', 'derived_eth_gt', 'derived_eth_lt', 'derived_eth_gte', 'derived_eth_lte', 'derived_eth_in', 'derived_eth_not_in', 'whitelist_pools', 'whitelist_pools_not', 'whitelist_pools_contains', 'whitelist_pools_contains_nocase', 'whitelist_pools_not_contains', 'whitelist_pools_not_contains_nocase', 'whitelist_pools_', 'token_day_data_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    symbol_not = sgqlc.types.Field(String, graphql_name='symbol_not')
    symbol_gt = sgqlc.types.Field(String, graphql_name='symbol_gt')
    symbol_lt = sgqlc.types.Field(String, graphql_name='symbol_lt')
    symbol_gte = sgqlc.types.Field(String, graphql_name='symbol_gte')
    symbol_lte = sgqlc.types.Field(String, graphql_name='symbol_lte')
    symbol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_in')
    symbol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='symbol_not_in')
    symbol_contains = sgqlc.types.Field(String, graphql_name='symbol_contains')
    symbol_contains_nocase = sgqlc.types.Field(String, graphql_name='symbol_contains_nocase')
    symbol_not_contains = sgqlc.types.Field(String, graphql_name='symbol_not_contains')
    symbol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_contains_nocase')
    symbol_starts_with = sgqlc.types.Field(String, graphql_name='symbol_starts_with')
    symbol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_starts_with_nocase')
    symbol_not_starts_with = sgqlc.types.Field(String, graphql_name='symbol_not_starts_with')
    symbol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_starts_with_nocase')
    symbol_ends_with = sgqlc.types.Field(String, graphql_name='symbol_ends_with')
    symbol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_ends_with_nocase')
    symbol_not_ends_with = sgqlc.types.Field(String, graphql_name='symbol_not_ends_with')
    symbol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='symbol_not_ends_with_nocase')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_not = sgqlc.types.Field(String, graphql_name='name_not')
    name_gt = sgqlc.types.Field(String, graphql_name='name_gt')
    name_lt = sgqlc.types.Field(String, graphql_name='name_lt')
    name_gte = sgqlc.types.Field(String, graphql_name='name_gte')
    name_lte = sgqlc.types.Field(String, graphql_name='name_lte')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_in')
    name_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='name_not_in')
    name_contains = sgqlc.types.Field(String, graphql_name='name_contains')
    name_contains_nocase = sgqlc.types.Field(String, graphql_name='name_contains_nocase')
    name_not_contains = sgqlc.types.Field(String, graphql_name='name_not_contains')
    name_not_contains_nocase = sgqlc.types.Field(String, graphql_name='name_not_contains_nocase')
    name_starts_with = sgqlc.types.Field(String, graphql_name='name_starts_with')
    name_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_starts_with_nocase')
    name_not_starts_with = sgqlc.types.Field(String, graphql_name='name_not_starts_with')
    name_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_starts_with_nocase')
    name_ends_with = sgqlc.types.Field(String, graphql_name='name_ends_with')
    name_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_ends_with_nocase')
    name_not_ends_with = sgqlc.types.Field(String, graphql_name='name_not_ends_with')
    name_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='name_not_ends_with_nocase')
    decimals = sgqlc.types.Field(BigInt, graphql_name='decimals')
    decimals_not = sgqlc.types.Field(BigInt, graphql_name='decimals_not')
    decimals_gt = sgqlc.types.Field(BigInt, graphql_name='decimals_gt')
    decimals_lt = sgqlc.types.Field(BigInt, graphql_name='decimals_lt')
    decimals_gte = sgqlc.types.Field(BigInt, graphql_name='decimals_gte')
    decimals_lte = sgqlc.types.Field(BigInt, graphql_name='decimals_lte')
    decimals_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='decimals_in')
    decimals_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='decimals_not_in')
    total_supply = sgqlc.types.Field(BigInt, graphql_name='totalSupply')
    total_supply_not = sgqlc.types.Field(BigInt, graphql_name='totalSupply_not')
    total_supply_gt = sgqlc.types.Field(BigInt, graphql_name='totalSupply_gt')
    total_supply_lt = sgqlc.types.Field(BigInt, graphql_name='totalSupply_lt')
    total_supply_gte = sgqlc.types.Field(BigInt, graphql_name='totalSupply_gte')
    total_supply_lte = sgqlc.types.Field(BigInt, graphql_name='totalSupply_lte')
    total_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSupply_in')
    total_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSupply_not_in')
    volume = sgqlc.types.Field(BigDecimal, graphql_name='volume')
    volume_not = sgqlc.types.Field(BigDecimal, graphql_name='volume_not')
    volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='volume_gt')
    volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='volume_lt')
    volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='volume_gte')
    volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='volume_lte')
    volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_in')
    volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volume_not_in')
    volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD')
    volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_not')
    volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gt')
    volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lt')
    volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gte')
    volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lte')
    volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_in')
    volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_not_in')
    untracked_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD')
    untracked_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_not')
    untracked_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gt')
    untracked_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lt')
    untracked_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_gte')
    untracked_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='untrackedVolumeUSD_lte')
    untracked_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_in')
    untracked_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='untrackedVolumeUSD_not_in')
    fees_usd = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD')
    fees_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_not')
    fees_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gt')
    fees_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lt')
    fees_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gte')
    fees_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lte')
    fees_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_in')
    fees_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_not_in')
    tx_count = sgqlc.types.Field(BigInt, graphql_name='txCount')
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name='txCount_not')
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name='txCount_gt')
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name='txCount_lt')
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name='txCount_gte')
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name='txCount_lte')
    tx_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_in')
    tx_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_not_in')
    pool_count = sgqlc.types.Field(BigInt, graphql_name='poolCount')
    pool_count_not = sgqlc.types.Field(BigInt, graphql_name='poolCount_not')
    pool_count_gt = sgqlc.types.Field(BigInt, graphql_name='poolCount_gt')
    pool_count_lt = sgqlc.types.Field(BigInt, graphql_name='poolCount_lt')
    pool_count_gte = sgqlc.types.Field(BigInt, graphql_name='poolCount_gte')
    pool_count_lte = sgqlc.types.Field(BigInt, graphql_name='poolCount_lte')
    pool_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='poolCount_in')
    pool_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='poolCount_not_in')
    total_value_locked = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked')
    total_value_locked_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_not')
    total_value_locked_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_gt')
    total_value_locked_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_lt')
    total_value_locked_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_gte')
    total_value_locked_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLocked_lte')
    total_value_locked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLocked_in')
    total_value_locked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLocked_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    total_value_locked_usduntracked = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked')
    total_value_locked_usduntracked_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_not')
    total_value_locked_usduntracked_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_gt')
    total_value_locked_usduntracked_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_lt')
    total_value_locked_usduntracked_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_gte')
    total_value_locked_usduntracked_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSDUntracked_lte')
    total_value_locked_usduntracked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSDUntracked_in')
    total_value_locked_usduntracked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSDUntracked_not_in')
    derived_eth = sgqlc.types.Field(BigDecimal, graphql_name='derivedETH')
    derived_eth_not = sgqlc.types.Field(BigDecimal, graphql_name='derivedETH_not')
    derived_eth_gt = sgqlc.types.Field(BigDecimal, graphql_name='derivedETH_gt')
    derived_eth_lt = sgqlc.types.Field(BigDecimal, graphql_name='derivedETH_lt')
    derived_eth_gte = sgqlc.types.Field(BigDecimal, graphql_name='derivedETH_gte')
    derived_eth_lte = sgqlc.types.Field(BigDecimal, graphql_name='derivedETH_lte')
    derived_eth_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='derivedETH_in')
    derived_eth_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='derivedETH_not_in')
    whitelist_pools = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='whitelistPools')
    whitelist_pools_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='whitelistPools_not')
    whitelist_pools_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='whitelistPools_contains')
    whitelist_pools_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='whitelistPools_contains_nocase')
    whitelist_pools_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='whitelistPools_not_contains')
    whitelist_pools_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='whitelistPools_not_contains_nocase')
    whitelist_pools_ = sgqlc.types.Field(Pool_filter, graphql_name='whitelistPools_')
    token_day_data_ = sgqlc.types.Field(TokenDayData_filter, graphql_name='tokenDayData_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Token_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Token_filter'), graphql_name='or')


class Transaction_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'gas_used', 'gas_used_not', 'gas_used_gt', 'gas_used_lt', 'gas_used_gte', 'gas_used_lte', 'gas_used_in', 'gas_used_not_in', 'gas_price', 'gas_price_not', 'gas_price_gt', 'gas_price_lt', 'gas_price_gte', 'gas_price_lte', 'gas_price_in', 'gas_price_not_in', 'modify_liquiditys_', 'swaps_', 'transfers_', 'subscriptions_', 'unsubscriptions_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    block_number = sgqlc.types.Field(BigInt, graphql_name='blockNumber')
    block_number_not = sgqlc.types.Field(BigInt, graphql_name='blockNumber_not')
    block_number_gt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gt')
    block_number_lt = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lt')
    block_number_gte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_gte')
    block_number_lte = sgqlc.types.Field(BigInt, graphql_name='blockNumber_lte')
    block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_in')
    block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='blockNumber_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    gas_used = sgqlc.types.Field(BigInt, graphql_name='gasUsed')
    gas_used_not = sgqlc.types.Field(BigInt, graphql_name='gasUsed_not')
    gas_used_gt = sgqlc.types.Field(BigInt, graphql_name='gasUsed_gt')
    gas_used_lt = sgqlc.types.Field(BigInt, graphql_name='gasUsed_lt')
    gas_used_gte = sgqlc.types.Field(BigInt, graphql_name='gasUsed_gte')
    gas_used_lte = sgqlc.types.Field(BigInt, graphql_name='gasUsed_lte')
    gas_used_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gasUsed_in')
    gas_used_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gasUsed_not_in')
    gas_price = sgqlc.types.Field(BigInt, graphql_name='gasPrice')
    gas_price_not = sgqlc.types.Field(BigInt, graphql_name='gasPrice_not')
    gas_price_gt = sgqlc.types.Field(BigInt, graphql_name='gasPrice_gt')
    gas_price_lt = sgqlc.types.Field(BigInt, graphql_name='gasPrice_lt')
    gas_price_gte = sgqlc.types.Field(BigInt, graphql_name='gasPrice_gte')
    gas_price_lte = sgqlc.types.Field(BigInt, graphql_name='gasPrice_lte')
    gas_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gasPrice_in')
    gas_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='gasPrice_not_in')
    modify_liquiditys_ = sgqlc.types.Field(ModifyLiquidity_filter, graphql_name='modifyLiquiditys_')
    swaps_ = sgqlc.types.Field(Swap_filter, graphql_name='swaps_')
    transfers_ = sgqlc.types.Field('Transfer_filter', graphql_name='transfers_')
    subscriptions_ = sgqlc.types.Field(Subscribe_filter, graphql_name='subscriptions_')
    unsubscriptions_ = sgqlc.types.Field('Unsubscribe_filter', graphql_name='unsubscriptions_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Transaction_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Transaction_filter'), graphql_name='or')


class Transfer_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'token_id', 'token_id_not', 'token_id_gt', 'token_id_lt', 'token_id_gte', 'token_id_lte', 'token_id_in', 'token_id_not_in', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'transaction', 'transaction_not', 'transaction_gt', 'transaction_lt', 'transaction_gte', 'transaction_lte', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_contains_nocase', 'transaction_not_contains', 'transaction_not_contains_nocase', 'transaction_starts_with', 'transaction_starts_with_nocase', 'transaction_not_starts_with', 'transaction_not_starts_with_nocase', 'transaction_ends_with', 'transaction_ends_with_nocase', 'transaction_not_ends_with', 'transaction_not_ends_with_nocase', 'transaction_', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'origin', 'origin_not', 'origin_gt', 'origin_lt', 'origin_gte', 'origin_lte', 'origin_in', 'origin_not_in', 'origin_contains', 'origin_contains_nocase', 'origin_not_contains', 'origin_not_contains_nocase', 'origin_starts_with', 'origin_starts_with_nocase', 'origin_not_starts_with', 'origin_not_starts_with_nocase', 'origin_ends_with', 'origin_ends_with_nocase', 'origin_not_ends_with', 'origin_not_ends_with_nocase', 'position', 'position_not', 'position_gt', 'position_lt', 'position_gte', 'position_lte', 'position_in', 'position_not_in', 'position_contains', 'position_contains_nocase', 'position_not_contains', 'position_not_contains_nocase', 'position_starts_with', 'position_starts_with_nocase', 'position_not_starts_with', 'position_not_starts_with_nocase', 'position_ends_with', 'position_ends_with_nocase', 'position_not_ends_with', 'position_not_ends_with_nocase', 'position_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    token_id = sgqlc.types.Field(BigInt, graphql_name='tokenId')
    token_id_not = sgqlc.types.Field(BigInt, graphql_name='tokenId_not')
    token_id_gt = sgqlc.types.Field(BigInt, graphql_name='tokenId_gt')
    token_id_lt = sgqlc.types.Field(BigInt, graphql_name='tokenId_lt')
    token_id_gte = sgqlc.types.Field(BigInt, graphql_name='tokenId_gte')
    token_id_lte = sgqlc.types.Field(BigInt, graphql_name='tokenId_lte')
    token_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenId_in')
    token_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenId_not_in')
    from_ = sgqlc.types.Field(String, graphql_name='from')
    from_not = sgqlc.types.Field(String, graphql_name='from_not')
    from_gt = sgqlc.types.Field(String, graphql_name='from_gt')
    from_lt = sgqlc.types.Field(String, graphql_name='from_lt')
    from_gte = sgqlc.types.Field(String, graphql_name='from_gte')
    from_lte = sgqlc.types.Field(String, graphql_name='from_lte')
    from_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_in')
    from_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='from_not_in')
    from_contains = sgqlc.types.Field(String, graphql_name='from_contains')
    from_contains_nocase = sgqlc.types.Field(String, graphql_name='from_contains_nocase')
    from_not_contains = sgqlc.types.Field(String, graphql_name='from_not_contains')
    from_not_contains_nocase = sgqlc.types.Field(String, graphql_name='from_not_contains_nocase')
    from_starts_with = sgqlc.types.Field(String, graphql_name='from_starts_with')
    from_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_starts_with_nocase')
    from_not_starts_with = sgqlc.types.Field(String, graphql_name='from_not_starts_with')
    from_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_starts_with_nocase')
    from_ends_with = sgqlc.types.Field(String, graphql_name='from_ends_with')
    from_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_ends_with_nocase')
    from_not_ends_with = sgqlc.types.Field(String, graphql_name='from_not_ends_with')
    from_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='from_not_ends_with_nocase')
    to = sgqlc.types.Field(String, graphql_name='to')
    to_not = sgqlc.types.Field(String, graphql_name='to_not')
    to_gt = sgqlc.types.Field(String, graphql_name='to_gt')
    to_lt = sgqlc.types.Field(String, graphql_name='to_lt')
    to_gte = sgqlc.types.Field(String, graphql_name='to_gte')
    to_lte = sgqlc.types.Field(String, graphql_name='to_lte')
    to_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_in')
    to_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='to_not_in')
    to_contains = sgqlc.types.Field(String, graphql_name='to_contains')
    to_contains_nocase = sgqlc.types.Field(String, graphql_name='to_contains_nocase')
    to_not_contains = sgqlc.types.Field(String, graphql_name='to_not_contains')
    to_not_contains_nocase = sgqlc.types.Field(String, graphql_name='to_not_contains_nocase')
    to_starts_with = sgqlc.types.Field(String, graphql_name='to_starts_with')
    to_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_starts_with_nocase')
    to_not_starts_with = sgqlc.types.Field(String, graphql_name='to_not_starts_with')
    to_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_starts_with_nocase')
    to_ends_with = sgqlc.types.Field(String, graphql_name='to_ends_with')
    to_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_ends_with_nocase')
    to_not_ends_with = sgqlc.types.Field(String, graphql_name='to_not_ends_with')
    to_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='to_not_ends_with_nocase')
    transaction = sgqlc.types.Field(String, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(String, graphql_name='transaction_not')
    transaction_gt = sgqlc.types.Field(String, graphql_name='transaction_gt')
    transaction_lt = sgqlc.types.Field(String, graphql_name='transaction_lt')
    transaction_gte = sgqlc.types.Field(String, graphql_name='transaction_gte')
    transaction_lte = sgqlc.types.Field(String, graphql_name='transaction_lte')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(String, graphql_name='transaction_contains')
    transaction_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_contains_nocase')
    transaction_not_contains = sgqlc.types.Field(String, graphql_name='transaction_not_contains')
    transaction_not_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_contains_nocase')
    transaction_starts_with = sgqlc.types.Field(String, graphql_name='transaction_starts_with')
    transaction_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_starts_with_nocase')
    transaction_not_starts_with = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with')
    transaction_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with_nocase')
    transaction_ends_with = sgqlc.types.Field(String, graphql_name='transaction_ends_with')
    transaction_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_ends_with_nocase')
    transaction_not_ends_with = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with')
    transaction_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with_nocase')
    transaction_ = sgqlc.types.Field(Transaction_filter, graphql_name='transaction_')
    log_index = sgqlc.types.Field(BigInt, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(BigInt, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(BigInt, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(BigInt, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(BigInt, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(BigInt, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    origin = sgqlc.types.Field(String, graphql_name='origin')
    origin_not = sgqlc.types.Field(String, graphql_name='origin_not')
    origin_gt = sgqlc.types.Field(String, graphql_name='origin_gt')
    origin_lt = sgqlc.types.Field(String, graphql_name='origin_lt')
    origin_gte = sgqlc.types.Field(String, graphql_name='origin_gte')
    origin_lte = sgqlc.types.Field(String, graphql_name='origin_lte')
    origin_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='origin_in')
    origin_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='origin_not_in')
    origin_contains = sgqlc.types.Field(String, graphql_name='origin_contains')
    origin_contains_nocase = sgqlc.types.Field(String, graphql_name='origin_contains_nocase')
    origin_not_contains = sgqlc.types.Field(String, graphql_name='origin_not_contains')
    origin_not_contains_nocase = sgqlc.types.Field(String, graphql_name='origin_not_contains_nocase')
    origin_starts_with = sgqlc.types.Field(String, graphql_name='origin_starts_with')
    origin_starts_with_nocase = sgqlc.types.Field(String, graphql_name='origin_starts_with_nocase')
    origin_not_starts_with = sgqlc.types.Field(String, graphql_name='origin_not_starts_with')
    origin_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='origin_not_starts_with_nocase')
    origin_ends_with = sgqlc.types.Field(String, graphql_name='origin_ends_with')
    origin_ends_with_nocase = sgqlc.types.Field(String, graphql_name='origin_ends_with_nocase')
    origin_not_ends_with = sgqlc.types.Field(String, graphql_name='origin_not_ends_with')
    origin_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='origin_not_ends_with_nocase')
    position = sgqlc.types.Field(String, graphql_name='position')
    position_not = sgqlc.types.Field(String, graphql_name='position_not')
    position_gt = sgqlc.types.Field(String, graphql_name='position_gt')
    position_lt = sgqlc.types.Field(String, graphql_name='position_lt')
    position_gte = sgqlc.types.Field(String, graphql_name='position_gte')
    position_lte = sgqlc.types.Field(String, graphql_name='position_lte')
    position_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='position_in')
    position_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='position_not_in')
    position_contains = sgqlc.types.Field(String, graphql_name='position_contains')
    position_contains_nocase = sgqlc.types.Field(String, graphql_name='position_contains_nocase')
    position_not_contains = sgqlc.types.Field(String, graphql_name='position_not_contains')
    position_not_contains_nocase = sgqlc.types.Field(String, graphql_name='position_not_contains_nocase')
    position_starts_with = sgqlc.types.Field(String, graphql_name='position_starts_with')
    position_starts_with_nocase = sgqlc.types.Field(String, graphql_name='position_starts_with_nocase')
    position_not_starts_with = sgqlc.types.Field(String, graphql_name='position_not_starts_with')
    position_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='position_not_starts_with_nocase')
    position_ends_with = sgqlc.types.Field(String, graphql_name='position_ends_with')
    position_ends_with_nocase = sgqlc.types.Field(String, graphql_name='position_ends_with_nocase')
    position_not_ends_with = sgqlc.types.Field(String, graphql_name='position_not_ends_with')
    position_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='position_not_ends_with_nocase')
    position_ = sgqlc.types.Field(Position_filter, graphql_name='position_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Transfer_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Transfer_filter'), graphql_name='or')


class UniswapDayData_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'date', 'date_not', 'date_gt', 'date_lt', 'date_gte', 'date_lte', 'date_in', 'date_not_in', 'volume_eth', 'volume_eth_not', 'volume_eth_gt', 'volume_eth_lt', 'volume_eth_gte', 'volume_eth_lte', 'volume_eth_in', 'volume_eth_not_in', 'volume_usd', 'volume_usd_not', 'volume_usd_gt', 'volume_usd_lt', 'volume_usd_gte', 'volume_usd_lte', 'volume_usd_in', 'volume_usd_not_in', 'volume_usduntracked', 'volume_usduntracked_not', 'volume_usduntracked_gt', 'volume_usduntracked_lt', 'volume_usduntracked_gte', 'volume_usduntracked_lte', 'volume_usduntracked_in', 'volume_usduntracked_not_in', 'fees_usd', 'fees_usd_not', 'fees_usd_gt', 'fees_usd_lt', 'fees_usd_gte', 'fees_usd_lte', 'fees_usd_in', 'fees_usd_not_in', 'tx_count', 'tx_count_not', 'tx_count_gt', 'tx_count_lt', 'tx_count_gte', 'tx_count_lte', 'tx_count_in', 'tx_count_not_in', 'tvl_usd', 'tvl_usd_not', 'tvl_usd_gt', 'tvl_usd_lt', 'tvl_usd_gte', 'tvl_usd_lte', 'tvl_usd_in', 'tvl_usd_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    date = sgqlc.types.Field(Int, graphql_name='date')
    date_not = sgqlc.types.Field(Int, graphql_name='date_not')
    date_gt = sgqlc.types.Field(Int, graphql_name='date_gt')
    date_lt = sgqlc.types.Field(Int, graphql_name='date_lt')
    date_gte = sgqlc.types.Field(Int, graphql_name='date_gte')
    date_lte = sgqlc.types.Field(Int, graphql_name='date_lte')
    date_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='date_in')
    date_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='date_not_in')
    volume_eth = sgqlc.types.Field(BigDecimal, graphql_name='volumeETH')
    volume_eth_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeETH_not')
    volume_eth_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeETH_gt')
    volume_eth_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeETH_lt')
    volume_eth_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeETH_gte')
    volume_eth_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeETH_lte')
    volume_eth_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeETH_in')
    volume_eth_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeETH_not_in')
    volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD')
    volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_not')
    volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gt')
    volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lt')
    volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_gte')
    volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSD_lte')
    volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_in')
    volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSD_not_in')
    volume_usduntracked = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSDUntracked')
    volume_usduntracked_not = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSDUntracked_not')
    volume_usduntracked_gt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSDUntracked_gt')
    volume_usduntracked_lt = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSDUntracked_lt')
    volume_usduntracked_gte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSDUntracked_gte')
    volume_usduntracked_lte = sgqlc.types.Field(BigDecimal, graphql_name='volumeUSDUntracked_lte')
    volume_usduntracked_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSDUntracked_in')
    volume_usduntracked_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='volumeUSDUntracked_not_in')
    fees_usd = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD')
    fees_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_not')
    fees_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gt')
    fees_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lt')
    fees_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_gte')
    fees_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='feesUSD_lte')
    fees_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_in')
    fees_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feesUSD_not_in')
    tx_count = sgqlc.types.Field(BigInt, graphql_name='txCount')
    tx_count_not = sgqlc.types.Field(BigInt, graphql_name='txCount_not')
    tx_count_gt = sgqlc.types.Field(BigInt, graphql_name='txCount_gt')
    tx_count_lt = sgqlc.types.Field(BigInt, graphql_name='txCount_lt')
    tx_count_gte = sgqlc.types.Field(BigInt, graphql_name='txCount_gte')
    tx_count_lte = sgqlc.types.Field(BigInt, graphql_name='txCount_lte')
    tx_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_in')
    tx_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='txCount_not_in')
    tvl_usd = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD')
    tvl_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_not')
    tvl_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_gt')
    tvl_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_lt')
    tvl_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_gte')
    tvl_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='tvlUSD_lte')
    tvl_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tvlUSD_in')
    tvl_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tvlUSD_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('UniswapDayData_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('UniswapDayData_filter'), graphql_name='or')


class Unsubscribe_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'token_id', 'token_id_not', 'token_id_gt', 'token_id_lt', 'token_id_gte', 'token_id_lte', 'token_id_in', 'token_id_not_in', 'address', 'address_not', 'address_gt', 'address_lt', 'address_gte', 'address_lte', 'address_in', 'address_not_in', 'address_contains', 'address_contains_nocase', 'address_not_contains', 'address_not_contains_nocase', 'address_starts_with', 'address_starts_with_nocase', 'address_not_starts_with', 'address_not_starts_with_nocase', 'address_ends_with', 'address_ends_with_nocase', 'address_not_ends_with', 'address_not_ends_with_nocase', 'transaction', 'transaction_not', 'transaction_gt', 'transaction_lt', 'transaction_gte', 'transaction_lte', 'transaction_in', 'transaction_not_in', 'transaction_contains', 'transaction_contains_nocase', 'transaction_not_contains', 'transaction_not_contains_nocase', 'transaction_starts_with', 'transaction_starts_with_nocase', 'transaction_not_starts_with', 'transaction_not_starts_with_nocase', 'transaction_ends_with', 'transaction_ends_with_nocase', 'transaction_not_ends_with', 'transaction_not_ends_with_nocase', 'transaction_', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'origin', 'origin_not', 'origin_gt', 'origin_lt', 'origin_gte', 'origin_lte', 'origin_in', 'origin_not_in', 'origin_contains', 'origin_contains_nocase', 'origin_not_contains', 'origin_not_contains_nocase', 'origin_starts_with', 'origin_starts_with_nocase', 'origin_not_starts_with', 'origin_not_starts_with_nocase', 'origin_ends_with', 'origin_ends_with_nocase', 'origin_not_ends_with', 'origin_not_ends_with_nocase', 'position', 'position_not', 'position_gt', 'position_lt', 'position_gte', 'position_lte', 'position_in', 'position_not_in', 'position_contains', 'position_contains_nocase', 'position_not_contains', 'position_not_contains_nocase', 'position_starts_with', 'position_starts_with_nocase', 'position_not_starts_with', 'position_not_starts_with_nocase', 'position_ends_with', 'position_ends_with_nocase', 'position_not_ends_with', 'position_not_ends_with_nocase', 'position_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    token_id = sgqlc.types.Field(BigInt, graphql_name='tokenId')
    token_id_not = sgqlc.types.Field(BigInt, graphql_name='tokenId_not')
    token_id_gt = sgqlc.types.Field(BigInt, graphql_name='tokenId_gt')
    token_id_lt = sgqlc.types.Field(BigInt, graphql_name='tokenId_lt')
    token_id_gte = sgqlc.types.Field(BigInt, graphql_name='tokenId_gte')
    token_id_lte = sgqlc.types.Field(BigInt, graphql_name='tokenId_lte')
    token_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenId_in')
    token_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='tokenId_not_in')
    address = sgqlc.types.Field(String, graphql_name='address')
    address_not = sgqlc.types.Field(String, graphql_name='address_not')
    address_gt = sgqlc.types.Field(String, graphql_name='address_gt')
    address_lt = sgqlc.types.Field(String, graphql_name='address_lt')
    address_gte = sgqlc.types.Field(String, graphql_name='address_gte')
    address_lte = sgqlc.types.Field(String, graphql_name='address_lte')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(String, graphql_name='address_contains')
    address_contains_nocase = sgqlc.types.Field(String, graphql_name='address_contains_nocase')
    address_not_contains = sgqlc.types.Field(String, graphql_name='address_not_contains')
    address_not_contains_nocase = sgqlc.types.Field(String, graphql_name='address_not_contains_nocase')
    address_starts_with = sgqlc.types.Field(String, graphql_name='address_starts_with')
    address_starts_with_nocase = sgqlc.types.Field(String, graphql_name='address_starts_with_nocase')
    address_not_starts_with = sgqlc.types.Field(String, graphql_name='address_not_starts_with')
    address_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='address_not_starts_with_nocase')
    address_ends_with = sgqlc.types.Field(String, graphql_name='address_ends_with')
    address_ends_with_nocase = sgqlc.types.Field(String, graphql_name='address_ends_with_nocase')
    address_not_ends_with = sgqlc.types.Field(String, graphql_name='address_not_ends_with')
    address_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='address_not_ends_with_nocase')
    transaction = sgqlc.types.Field(String, graphql_name='transaction')
    transaction_not = sgqlc.types.Field(String, graphql_name='transaction_not')
    transaction_gt = sgqlc.types.Field(String, graphql_name='transaction_gt')
    transaction_lt = sgqlc.types.Field(String, graphql_name='transaction_lt')
    transaction_gte = sgqlc.types.Field(String, graphql_name='transaction_gte')
    transaction_lte = sgqlc.types.Field(String, graphql_name='transaction_lte')
    transaction_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_in')
    transaction_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='transaction_not_in')
    transaction_contains = sgqlc.types.Field(String, graphql_name='transaction_contains')
    transaction_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_contains_nocase')
    transaction_not_contains = sgqlc.types.Field(String, graphql_name='transaction_not_contains')
    transaction_not_contains_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_contains_nocase')
    transaction_starts_with = sgqlc.types.Field(String, graphql_name='transaction_starts_with')
    transaction_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_starts_with_nocase')
    transaction_not_starts_with = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with')
    transaction_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_starts_with_nocase')
    transaction_ends_with = sgqlc.types.Field(String, graphql_name='transaction_ends_with')
    transaction_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_ends_with_nocase')
    transaction_not_ends_with = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with')
    transaction_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='transaction_not_ends_with_nocase')
    transaction_ = sgqlc.types.Field(Transaction_filter, graphql_name='transaction_')
    log_index = sgqlc.types.Field(BigInt, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(BigInt, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(BigInt, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(BigInt, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(BigInt, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(BigInt, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='logIndex_not_in')
    timestamp = sgqlc.types.Field(BigInt, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(BigInt, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='timestamp_not_in')
    origin = sgqlc.types.Field(String, graphql_name='origin')
    origin_not = sgqlc.types.Field(String, graphql_name='origin_not')
    origin_gt = sgqlc.types.Field(String, graphql_name='origin_gt')
    origin_lt = sgqlc.types.Field(String, graphql_name='origin_lt')
    origin_gte = sgqlc.types.Field(String, graphql_name='origin_gte')
    origin_lte = sgqlc.types.Field(String, graphql_name='origin_lte')
    origin_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='origin_in')
    origin_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='origin_not_in')
    origin_contains = sgqlc.types.Field(String, graphql_name='origin_contains')
    origin_contains_nocase = sgqlc.types.Field(String, graphql_name='origin_contains_nocase')
    origin_not_contains = sgqlc.types.Field(String, graphql_name='origin_not_contains')
    origin_not_contains_nocase = sgqlc.types.Field(String, graphql_name='origin_not_contains_nocase')
    origin_starts_with = sgqlc.types.Field(String, graphql_name='origin_starts_with')
    origin_starts_with_nocase = sgqlc.types.Field(String, graphql_name='origin_starts_with_nocase')
    origin_not_starts_with = sgqlc.types.Field(String, graphql_name='origin_not_starts_with')
    origin_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='origin_not_starts_with_nocase')
    origin_ends_with = sgqlc.types.Field(String, graphql_name='origin_ends_with')
    origin_ends_with_nocase = sgqlc.types.Field(String, graphql_name='origin_ends_with_nocase')
    origin_not_ends_with = sgqlc.types.Field(String, graphql_name='origin_not_ends_with')
    origin_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='origin_not_ends_with_nocase')
    position = sgqlc.types.Field(String, graphql_name='position')
    position_not = sgqlc.types.Field(String, graphql_name='position_not')
    position_gt = sgqlc.types.Field(String, graphql_name='position_gt')
    position_lt = sgqlc.types.Field(String, graphql_name='position_lt')
    position_gte = sgqlc.types.Field(String, graphql_name='position_gte')
    position_lte = sgqlc.types.Field(String, graphql_name='position_lte')
    position_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='position_in')
    position_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='position_not_in')
    position_contains = sgqlc.types.Field(String, graphql_name='position_contains')
    position_contains_nocase = sgqlc.types.Field(String, graphql_name='position_contains_nocase')
    position_not_contains = sgqlc.types.Field(String, graphql_name='position_not_contains')
    position_not_contains_nocase = sgqlc.types.Field(String, graphql_name='position_not_contains_nocase')
    position_starts_with = sgqlc.types.Field(String, graphql_name='position_starts_with')
    position_starts_with_nocase = sgqlc.types.Field(String, graphql_name='position_starts_with_nocase')
    position_not_starts_with = sgqlc.types.Field(String, graphql_name='position_not_starts_with')
    position_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='position_not_starts_with_nocase')
    position_ends_with = sgqlc.types.Field(String, graphql_name='position_ends_with')
    position_ends_with_nocase = sgqlc.types.Field(String, graphql_name='position_ends_with_nocase')
    position_not_ends_with = sgqlc.types.Field(String, graphql_name='position_not_ends_with')
    position_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='position_not_ends_with_nocase')
    position_ = sgqlc.types.Field(Position_filter, graphql_name='position_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Unsubscribe_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Unsubscribe_filter'), graphql_name='or')



########################################################################
# Output Objects and Interfaces
########################################################################
class Bundle(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'eth_price_usd')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    eth_price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='ethPriceUSD')


class ModifyLiquidity(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'transaction', 'timestamp', 'pool', 'token0', 'token1', 'sender', 'origin', 'amount', 'amount0', 'amount1', 'amount_usd', 'tick_lower', 'tick_upper', 'log_index')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    transaction = sgqlc.types.Field(sgqlc.types.non_null('Transaction'), graphql_name='transaction')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    pool = sgqlc.types.Field(sgqlc.types.non_null('Pool'), graphql_name='pool')
    token0 = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token0')
    token1 = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token1')
    sender = sgqlc.types.Field(Bytes, graphql_name='sender')
    origin = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='origin')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    amount0 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amount0')
    amount1 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amount1')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    tick_lower = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tickLower')
    tick_upper = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tickUpper')
    log_index = sgqlc.types.Field(BigInt, graphql_name='logIndex')


class Pool(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'created_at_timestamp', 'created_at_block_number', 'token0', 'token1', 'fee_tier', 'liquidity', 'sqrt_price', 'token0_price', 'token1_price', 'tick', 'tick_spacing', 'observation_index', 'volume_token0', 'volume_token1', 'volume_usd', 'untracked_volume_usd', 'fees_usd', 'tx_count', 'collected_fees_token0', 'collected_fees_token1', 'collected_fees_usd', 'total_value_locked_token0', 'total_value_locked_token1', 'total_value_locked_eth', 'total_value_locked_usd', 'total_value_locked_usduntracked', 'liquidity_provider_count', 'pool_hour_data', 'pool_day_data', 'hooks', 'modify_liquiditys', 'swaps', 'ticks')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    created_at_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdAtTimestamp')
    created_at_block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdAtBlockNumber')
    token0 = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token0')
    token1 = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token1')
    fee_tier = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='feeTier')
    liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='liquidity')
    sqrt_price = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='sqrtPrice')
    token0_price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='token0Price')
    token1_price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='token1Price')
    tick = sgqlc.types.Field(BigInt, graphql_name='tick')
    tick_spacing = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tickSpacing')
    observation_index = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='observationIndex')
    volume_token0 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeToken0')
    volume_token1 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeToken1')
    volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeUSD')
    untracked_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='untrackedVolumeUSD')
    fees_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='feesUSD')
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='txCount')
    collected_fees_token0 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='collectedFeesToken0')
    collected_fees_token1 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='collectedFeesToken1')
    collected_fees_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='collectedFeesUSD')
    total_value_locked_token0 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedToken0')
    total_value_locked_token1 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedToken1')
    total_value_locked_eth = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedETH')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    total_value_locked_usduntracked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSDUntracked')
    liquidity_provider_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='liquidityProviderCount')
    pool_hour_data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PoolHourData'))), graphql_name='poolHourData', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolHourData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolHourData_filter, graphql_name='where', default=None)),
))
    )
    pool_day_data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PoolDayData'))), graphql_name='poolDayData', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolDayData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolDayData_filter, graphql_name='where', default=None)),
))
    )
    hooks = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='hooks')
    modify_liquiditys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ModifyLiquidity))), graphql_name='modifyLiquiditys', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ModifyLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ModifyLiquidity_filter, graphql_name='where', default=None)),
))
    )
    swaps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Swap'))), graphql_name='swaps', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Swap_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Swap_filter, graphql_name='where', default=None)),
))
    )
    ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tick'))), graphql_name='ticks', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Tick_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Tick_filter, graphql_name='where', default=None)),
))
    )


class PoolDayData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'date', 'pool', 'liquidity', 'sqrt_price', 'token0_price', 'token1_price', 'tick', 'tvl_usd', 'volume_token0', 'volume_token1', 'volume_usd', 'fees_usd', 'tx_count', 'open', 'high', 'low', 'close')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    date = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='date')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')
    liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='liquidity')
    sqrt_price = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='sqrtPrice')
    token0_price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='token0Price')
    token1_price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='token1Price')
    tick = sgqlc.types.Field(BigInt, graphql_name='tick')
    tvl_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='tvlUSD')
    volume_token0 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeToken0')
    volume_token1 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeToken1')
    volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeUSD')
    fees_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='feesUSD')
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='txCount')
    open = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='open')
    high = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='high')
    low = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='low')
    close = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='close')


class PoolHourData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'period_start_unix', 'pool', 'liquidity', 'sqrt_price', 'token0_price', 'token1_price', 'tick', 'tvl_usd', 'volume_token0', 'volume_token1', 'volume_usd', 'fees_usd', 'tx_count', 'open', 'high', 'low', 'close')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    period_start_unix = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='periodStartUnix')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')
    liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='liquidity')
    sqrt_price = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='sqrtPrice')
    token0_price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='token0Price')
    token1_price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='token1Price')
    tick = sgqlc.types.Field(BigInt, graphql_name='tick')
    tvl_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='tvlUSD')
    volume_token0 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeToken0')
    volume_token1 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeToken1')
    volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeUSD')
    fees_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='feesUSD')
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='txCount')
    open = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='open')
    high = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='high')
    low = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='low')
    close = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='close')


class PoolManager(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_count', 'tx_count', 'total_volume_usd', 'total_volume_eth', 'total_fees_usd', 'total_fees_eth', 'untracked_volume_usd', 'total_value_locked_usd', 'total_value_locked_eth', 'total_value_locked_usduntracked', 'total_value_locked_ethuntracked', 'owner')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='poolCount')
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='txCount')
    total_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalVolumeUSD')
    total_volume_eth = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalVolumeETH')
    total_fees_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalFeesUSD')
    total_fees_eth = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalFeesETH')
    untracked_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='untrackedVolumeUSD')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    total_value_locked_eth = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedETH')
    total_value_locked_usduntracked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSDUntracked')
    total_value_locked_ethuntracked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedETHUntracked')
    owner = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='owner')


class Position(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'token_id', 'owner', 'origin', 'created_at_timestamp', 'subscriptions', 'unsubscriptions', 'transfers')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    token_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tokenId')
    owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='owner')
    origin = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='origin')
    created_at_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdAtTimestamp')
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Subscribe'))), graphql_name='subscriptions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Subscribe_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Subscribe_filter, graphql_name='where', default=None)),
))
    )
    unsubscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Unsubscribe'))), graphql_name='unsubscriptions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Unsubscribe_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Unsubscribe_filter, graphql_name='where', default=None)),
))
    )
    transfers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Transfer'))), graphql_name='transfers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Transfer_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Transfer_filter, graphql_name='where', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('pool_manager', 'pool_managers', 'bundle', 'bundles', 'token', 'tokens', 'pool', 'pools', 'tick', 'ticks', 'transaction', 'transactions', 'swap', 'swaps', 'modify_liquidity', 'modify_liquidities', 'uniswap_day_data', 'uniswap_day_datas', 'pool_day_data', 'pool_day_datas', 'pool_hour_data', 'pool_hour_datas', 'token_day_data', 'token_day_datas', 'token_hour_data', 'token_hour_datas', 'position', 'positions', 'subscribe', 'subscribes', 'unsubscribe', 'unsubscribes', 'transfer', 'transfers', '_meta')
    pool_manager = sgqlc.types.Field(PoolManager, graphql_name='poolManager', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_managers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolManager))), graphql_name='poolManagers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolManager_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolManager_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    bundle = sgqlc.types.Field(Bundle, graphql_name='bundle', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    bundles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bundle))), graphql_name='bundles', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Bundle_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Bundle_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token = sgqlc.types.Field('Token', graphql_name='token', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='tokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool = sgqlc.types.Field(Pool, graphql_name='pool', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Pool))), graphql_name='pools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Pool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Pool_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    tick = sgqlc.types.Field('Tick', graphql_name='tick', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tick'))), graphql_name='ticks', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Tick_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Tick_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transaction = sgqlc.types.Field('Transaction', graphql_name='transaction', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Transaction'))), graphql_name='transactions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Transaction_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Transaction_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    swap = sgqlc.types.Field('Swap', graphql_name='swap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    swaps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Swap'))), graphql_name='swaps', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Swap_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Swap_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    modify_liquidity = sgqlc.types.Field(ModifyLiquidity, graphql_name='modifyLiquidity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    modify_liquidities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ModifyLiquidity))), graphql_name='modifyLiquidities', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ModifyLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ModifyLiquidity_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    uniswap_day_data = sgqlc.types.Field('UniswapDayData', graphql_name='uniswapDayData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    uniswap_day_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UniswapDayData'))), graphql_name='uniswapDayDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UniswapDayData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UniswapDayData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_day_data = sgqlc.types.Field(PoolDayData, graphql_name='poolDayData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_day_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolDayData))), graphql_name='poolDayDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolDayData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolDayData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_hour_data = sgqlc.types.Field(PoolHourData, graphql_name='poolHourData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_hour_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolHourData))), graphql_name='poolHourDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolHourData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolHourData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_day_data = sgqlc.types.Field('TokenDayData', graphql_name='tokenDayData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_day_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TokenDayData'))), graphql_name='tokenDayDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TokenDayData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TokenDayData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_hour_data = sgqlc.types.Field('TokenHourData', graphql_name='tokenHourData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_hour_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TokenHourData'))), graphql_name='tokenHourDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TokenHourData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TokenHourData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    position = sgqlc.types.Field(Position, graphql_name='position', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    positions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Position))), graphql_name='positions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Position_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Position_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    subscribe = sgqlc.types.Field('Subscribe', graphql_name='subscribe', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    subscribes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Subscribe'))), graphql_name='subscribes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Subscribe_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Subscribe_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    unsubscribe = sgqlc.types.Field('Unsubscribe', graphql_name='unsubscribe', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    unsubscribes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Unsubscribe'))), graphql_name='unsubscribes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Unsubscribe_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Unsubscribe_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer = sgqlc.types.Field('Transfer', graphql_name='transfer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Transfer'))), graphql_name='transfers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Transfer_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Transfer_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class Subscribe(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'token_id', 'address', 'transaction', 'log_index', 'timestamp', 'origin', 'position')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    token_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tokenId')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    transaction = sgqlc.types.Field(sgqlc.types.non_null('Transaction'), graphql_name='transaction')
    log_index = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='logIndex')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    origin = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='origin')
    position = sgqlc.types.Field(sgqlc.types.non_null(Position), graphql_name='position')


class Subscription(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('pool_manager', 'pool_managers', 'bundle', 'bundles', 'token', 'tokens', 'pool', 'pools', 'tick', 'ticks', 'transaction', 'transactions', 'swap', 'swaps', 'modify_liquidity', 'modify_liquidities', 'uniswap_day_data', 'uniswap_day_datas', 'pool_day_data', 'pool_day_datas', 'pool_hour_data', 'pool_hour_datas', 'token_day_data', 'token_day_datas', 'token_hour_data', 'token_hour_datas', 'position', 'positions', 'subscribe', 'subscribes', 'unsubscribe', 'unsubscribes', 'transfer', 'transfers', '_meta')
    pool_manager = sgqlc.types.Field(PoolManager, graphql_name='poolManager', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_managers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolManager))), graphql_name='poolManagers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolManager_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolManager_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    bundle = sgqlc.types.Field(Bundle, graphql_name='bundle', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    bundles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bundle))), graphql_name='bundles', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Bundle_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Bundle_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token = sgqlc.types.Field('Token', graphql_name='token', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='tokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool = sgqlc.types.Field(Pool, graphql_name='pool', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Pool))), graphql_name='pools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Pool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Pool_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    tick = sgqlc.types.Field('Tick', graphql_name='tick', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    ticks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tick'))), graphql_name='ticks', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Tick_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Tick_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transaction = sgqlc.types.Field('Transaction', graphql_name='transaction', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transactions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Transaction'))), graphql_name='transactions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Transaction_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Transaction_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    swap = sgqlc.types.Field('Swap', graphql_name='swap', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    swaps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Swap'))), graphql_name='swaps', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Swap_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Swap_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    modify_liquidity = sgqlc.types.Field(ModifyLiquidity, graphql_name='modifyLiquidity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    modify_liquidities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ModifyLiquidity))), graphql_name='modifyLiquidities', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ModifyLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ModifyLiquidity_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    uniswap_day_data = sgqlc.types.Field('UniswapDayData', graphql_name='uniswapDayData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    uniswap_day_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UniswapDayData'))), graphql_name='uniswapDayDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UniswapDayData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UniswapDayData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_day_data = sgqlc.types.Field(PoolDayData, graphql_name='poolDayData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_day_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolDayData))), graphql_name='poolDayDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolDayData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolDayData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_hour_data = sgqlc.types.Field(PoolHourData, graphql_name='poolHourData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_hour_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolHourData))), graphql_name='poolHourDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolHourData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolHourData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_day_data = sgqlc.types.Field('TokenDayData', graphql_name='tokenDayData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_day_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TokenDayData'))), graphql_name='tokenDayDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TokenDayData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TokenDayData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_hour_data = sgqlc.types.Field('TokenHourData', graphql_name='tokenHourData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_hour_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TokenHourData'))), graphql_name='tokenHourDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TokenHourData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TokenHourData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    position = sgqlc.types.Field(Position, graphql_name='position', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    positions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Position))), graphql_name='positions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Position_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Position_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    subscribe = sgqlc.types.Field(Subscribe, graphql_name='subscribe', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    subscribes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Subscribe))), graphql_name='subscribes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Subscribe_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Subscribe_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    unsubscribe = sgqlc.types.Field('Unsubscribe', graphql_name='unsubscribe', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    unsubscribes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Unsubscribe'))), graphql_name='unsubscribes', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Unsubscribe_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Unsubscribe_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfer = sgqlc.types.Field('Transfer', graphql_name='transfer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    transfers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Transfer'))), graphql_name='transfers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Transfer_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Transfer_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class Swap(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'transaction', 'timestamp', 'pool', 'token0', 'token1', 'sender', 'origin', 'amount0', 'amount1', 'amount_usd', 'sqrt_price_x96', 'tick', 'log_index')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    transaction = sgqlc.types.Field(sgqlc.types.non_null('Transaction'), graphql_name='transaction')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')
    token0 = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token0')
    token1 = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token1')
    sender = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='sender')
    origin = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='origin')
    amount0 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amount0')
    amount1 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amount1')
    amount_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amountUSD')
    sqrt_price_x96 = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='sqrtPriceX96')
    tick = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tick')
    log_index = sgqlc.types.Field(BigInt, graphql_name='logIndex')


class Tick(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_address', 'tick_idx', 'pool', 'liquidity_gross', 'liquidity_net', 'price0', 'price1', 'created_at_timestamp', 'created_at_block_number')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_address = sgqlc.types.Field(String, graphql_name='poolAddress')
    tick_idx = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tickIdx')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')
    liquidity_gross = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='liquidityGross')
    liquidity_net = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='liquidityNet')
    price0 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='price0')
    price1 = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='price1')
    created_at_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdAtTimestamp')
    created_at_block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdAtBlockNumber')


class Token(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'symbol', 'name', 'decimals', 'total_supply', 'volume', 'volume_usd', 'untracked_volume_usd', 'fees_usd', 'tx_count', 'pool_count', 'total_value_locked', 'total_value_locked_usd', 'total_value_locked_usduntracked', 'derived_eth', 'whitelist_pools', 'token_day_data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='decimals')
    total_supply = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='totalSupply')
    volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volume')
    volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeUSD')
    untracked_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='untrackedVolumeUSD')
    fees_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='feesUSD')
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='txCount')
    pool_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='poolCount')
    total_value_locked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLocked')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    total_value_locked_usduntracked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSDUntracked')
    derived_eth = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='derivedETH')
    whitelist_pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Pool))), graphql_name='whitelistPools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Pool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Pool_filter, graphql_name='where', default=None)),
))
    )
    token_day_data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TokenDayData'))), graphql_name='tokenDayData', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TokenDayData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TokenDayData_filter, graphql_name='where', default=None)),
))
    )


class TokenDayData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'date', 'token', 'volume', 'volume_usd', 'untracked_volume_usd', 'total_value_locked', 'total_value_locked_usd', 'price_usd', 'fees_usd', 'open', 'high', 'low', 'close')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    date = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='date')
    token = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='token')
    volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volume')
    volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeUSD')
    untracked_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='untrackedVolumeUSD')
    total_value_locked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLocked')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='priceUSD')
    fees_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='feesUSD')
    open = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='open')
    high = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='high')
    low = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='low')
    close = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='close')


class TokenHourData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'period_start_unix', 'token', 'volume', 'volume_usd', 'untracked_volume_usd', 'total_value_locked', 'total_value_locked_usd', 'price_usd', 'fees_usd', 'open', 'high', 'low', 'close')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    period_start_unix = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='periodStartUnix')
    token = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='token')
    volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volume')
    volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeUSD')
    untracked_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='untrackedVolumeUSD')
    total_value_locked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLocked')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    price_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='priceUSD')
    fees_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='feesUSD')
    open = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='open')
    high = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='high')
    low = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='low')
    close = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='close')


class Transaction(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'block_number', 'timestamp', 'gas_used', 'gas_price', 'modify_liquiditys', 'swaps', 'transfers', 'subscriptions', 'unsubscriptions')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    gas_used = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='gasUsed')
    gas_price = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='gasPrice')
    modify_liquiditys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ModifyLiquidity)), graphql_name='modifyLiquiditys', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ModifyLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ModifyLiquidity_filter, graphql_name='where', default=None)),
))
    )
    swaps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Swap)), graphql_name='swaps', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Swap_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Swap_filter, graphql_name='where', default=None)),
))
    )
    transfers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Transfer')), graphql_name='transfers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Transfer_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Transfer_filter, graphql_name='where', default=None)),
))
    )
    subscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Subscribe)), graphql_name='subscriptions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Subscribe_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Subscribe_filter, graphql_name='where', default=None)),
))
    )
    unsubscriptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('Unsubscribe')), graphql_name='unsubscriptions', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Unsubscribe_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Unsubscribe_filter, graphql_name='where', default=None)),
))
    )


class Transfer(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'token_id', 'from_', 'to', 'transaction', 'log_index', 'timestamp', 'origin', 'position')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    token_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tokenId')
    from_ = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='from')
    to = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='to')
    transaction = sgqlc.types.Field(sgqlc.types.non_null(Transaction), graphql_name='transaction')
    log_index = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='logIndex')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    origin = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='origin')
    position = sgqlc.types.Field(sgqlc.types.non_null(Position), graphql_name='position')


class UniswapDayData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'date', 'volume_eth', 'volume_usd', 'volume_usduntracked', 'fees_usd', 'tx_count', 'tvl_usd')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    date = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='date')
    volume_eth = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeETH')
    volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeUSD')
    volume_usduntracked = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volumeUSDUntracked')
    fees_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='feesUSD')
    tx_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='txCount')
    tvl_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='tvlUSD')


class Unsubscribe(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'token_id', 'address', 'transaction', 'log_index', 'timestamp', 'origin', 'position')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    token_id = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tokenId')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    transaction = sgqlc.types.Field(sgqlc.types.non_null(Transaction), graphql_name='transaction')
    log_index = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='logIndex')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    origin = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='origin')
    position = sgqlc.types.Field(sgqlc.types.non_null(Position), graphql_name='position')


class _Block_(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('hash', 'number', 'timestamp', 'parent_hash')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    parent_hash = sgqlc.types.Field(Bytes, graphql_name='parentHash')


class _Meta_(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('block', 'deployment', 'has_indexing_errors')
    block = sgqlc.types.Field(sgqlc.types.non_null(_Block_), graphql_name='block')
    deployment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deployment')
    has_indexing_errors = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIndexingErrors')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
graphql_schema.query_type = Query
graphql_schema.mutation_type = None
graphql_schema.subscription_type = Subscription

