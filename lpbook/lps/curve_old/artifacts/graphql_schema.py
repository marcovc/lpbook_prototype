import sgqlc.types


graphql_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class Account_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id',)


class ActiveAccount_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id',)


class Aggregation_interval(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('day', 'hour')


class BigDecimal(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = graphql_schema


Boolean = sgqlc.types.Boolean

class Bytes(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class Deposit_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('amountUSD', 'blockNumber', 'from', 'hash', 'id', 'inputTokenAmounts', 'inputTokens', 'logIndex', 'outputToken', 'outputTokenAmount', 'outputToken___largePriceChangeBuffer', 'outputToken___largeTVLImpactBuffer', 'outputToken___totalSupply', 'outputToken___totalValueLockedUSD', 'outputToken__decimals', 'outputToken__id', 'outputToken__isBasePoolLpToken', 'outputToken__lastPriceBlockNumber', 'outputToken__lastPriceUSD', 'outputToken__name', 'outputToken__oracleType', 'outputToken__symbol', 'pool', 'pool___gaugeAddress', 'pool___isMetapool', 'pool___registryAddress', 'pool___tvlUSDExcludingBasePoolLpTokens', 'pool__createdBlockNumber', 'pool__createdTimestamp', 'pool__cumulativeProtocolSideRevenueUSD', 'pool__cumulativeSupplySideRevenueUSD', 'pool__cumulativeTotalRevenueUSD', 'pool__cumulativeVolumeUSD', 'pool__id', 'pool__isSingleSided', 'pool__name', 'pool__outputTokenPriceUSD', 'pool__outputTokenSupply', 'pool__stakedOutputTokenAmount', 'pool__symbol', 'pool__totalValueLockedUSD', 'protocol', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'timestamp', 'to')


class DexAmmProtocol_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('_poolIds', 'cumulativeProtocolSideRevenueUSD', 'cumulativeSupplySideRevenueUSD', 'cumulativeTotalRevenueUSD', 'cumulativeUniqueUsers', 'cumulativeVolumeUSD', 'dailyUsageMetrics', 'financialMetrics', 'hourlyUsageMetrics', 'id', 'methodologyVersion', 'name', 'network', 'pools', 'protocolControlledValueUSD', 'schemaVersion', 'slug', 'subgraphVersion', 'totalPoolCount', 'totalValueLockedUSD', 'type')


class Event_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('blockNumber', 'from', 'hash', 'id', 'logIndex', 'protocol', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'timestamp', 'to')


class FinancialsDailySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('blockNumber', 'cumulativeProtocolSideRevenueUSD', 'cumulativeSupplySideRevenueUSD', 'cumulativeTotalRevenueUSD', 'cumulativeVolumeUSD', 'dailyProtocolSideRevenueUSD', 'dailySupplySideRevenueUSD', 'dailyTotalRevenueUSD', 'dailyVolumeUSD', 'id', 'protocol', 'protocolControlledValueUSD', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'timestamp', 'totalValueLockedUSD')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class Int8(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class LiquidityPoolDailySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('blockNumber', 'cumulativeProtocolSideRevenueUSD', 'cumulativeSupplySideRevenueUSD', 'cumulativeTotalRevenueUSD', 'cumulativeVolumeUSD', 'dailyProtocolSideRevenueUSD', 'dailySupplySideRevenueUSD', 'dailyTotalRevenueUSD', 'dailyVolumeByTokenAmount', 'dailyVolumeByTokenUSD', 'dailyVolumeUSD', 'id', 'inputTokenBalances', 'inputTokenWeights', 'outputTokenPriceUSD', 'outputTokenSupply', 'pool', 'pool___gaugeAddress', 'pool___isMetapool', 'pool___registryAddress', 'pool___tvlUSDExcludingBasePoolLpTokens', 'pool__createdBlockNumber', 'pool__createdTimestamp', 'pool__cumulativeProtocolSideRevenueUSD', 'pool__cumulativeSupplySideRevenueUSD', 'pool__cumulativeTotalRevenueUSD', 'pool__cumulativeVolumeUSD', 'pool__id', 'pool__isSingleSided', 'pool__name', 'pool__outputTokenPriceUSD', 'pool__outputTokenSupply', 'pool__stakedOutputTokenAmount', 'pool__symbol', 'pool__totalValueLockedUSD', 'protocol', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'rewardTokenEmissionsAmount', 'rewardTokenEmissionsUSD', 'stakedOutputTokenAmount', 'timestamp', 'totalValueLockedUSD')


class LiquidityPoolFeeType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('DEPOSIT_FEE', 'DYNAMIC_LP_FEE', 'DYNAMIC_PROTOCOL_FEE', 'DYNAMIC_TRADING_FEE', 'FIXED_LP_FEE', 'FIXED_PROTOCOL_FEE', 'FIXED_TRADING_FEE', 'TIERED_TRADING_FEE', 'WITHDRAWAL_FEE')


class LiquidityPoolFee_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('feePercentage', 'feeType', 'id')


class LiquidityPoolHourlySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('blockNumber', 'cumulativeProtocolSideRevenueUSD', 'cumulativeSupplySideRevenueUSD', 'cumulativeTotalRevenueUSD', 'cumulativeVolumeUSD', 'hourlyProtocolSideRevenueUSD', 'hourlySupplySideRevenueUSD', 'hourlyTotalRevenueUSD', 'hourlyVolumeByTokenAmount', 'hourlyVolumeByTokenUSD', 'hourlyVolumeUSD', 'id', 'inputTokenBalances', 'inputTokenWeights', 'outputTokenPriceUSD', 'outputTokenSupply', 'pool', 'pool___gaugeAddress', 'pool___isMetapool', 'pool___registryAddress', 'pool___tvlUSDExcludingBasePoolLpTokens', 'pool__createdBlockNumber', 'pool__createdTimestamp', 'pool__cumulativeProtocolSideRevenueUSD', 'pool__cumulativeSupplySideRevenueUSD', 'pool__cumulativeTotalRevenueUSD', 'pool__cumulativeVolumeUSD', 'pool__id', 'pool__isSingleSided', 'pool__name', 'pool__outputTokenPriceUSD', 'pool__outputTokenSupply', 'pool__stakedOutputTokenAmount', 'pool__symbol', 'pool__totalValueLockedUSD', 'protocol', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'rewardTokenEmissionsAmount', 'rewardTokenEmissionsUSD', 'stakedOutputTokenAmount', 'timestamp', 'totalValueLockedUSD')


class LiquidityPool_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('_gaugeAddress', '_inputTokensOrdered', '_isMetapool', '_registryAddress', '_tvlUSDExcludingBasePoolLpTokens', 'createdBlockNumber', 'createdTimestamp', 'cumulativeProtocolSideRevenueUSD', 'cumulativeSupplySideRevenueUSD', 'cumulativeTotalRevenueUSD', 'cumulativeVolumeUSD', 'dailySnapshots', 'deposits', 'fees', 'hourlySnapshots', 'id', 'inputTokenBalances', 'inputTokenWeights', 'inputTokens', 'isSingleSided', 'name', 'outputToken', 'outputTokenPriceUSD', 'outputTokenSupply', 'outputToken___largePriceChangeBuffer', 'outputToken___largeTVLImpactBuffer', 'outputToken___totalSupply', 'outputToken___totalValueLockedUSD', 'outputToken__decimals', 'outputToken__id', 'outputToken__isBasePoolLpToken', 'outputToken__lastPriceBlockNumber', 'outputToken__lastPriceUSD', 'outputToken__name', 'outputToken__oracleType', 'outputToken__symbol', 'protocol', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'rewardTokenEmissionsAmount', 'rewardTokenEmissionsUSD', 'rewardTokens', 'stakedOutputTokenAmount', 'swaps', 'symbol', 'totalValueLockedUSD', 'withdraws')


class Network(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('ARBITRUM_ONE', 'ARWEAVE_MAINNET', 'AURORA', 'AVALANCHE', 'BOBA', 'BSC', 'CELO', 'COSMOS', 'CRONOS', 'FANTOM', 'FUSE', 'HARMONY', 'JUNO', 'MAINNET', 'MATIC', 'MOONBEAM', 'MOONRIVER', 'NEAR_MAINNET', 'OPTIMISM', 'OSMOSIS', 'XDAI')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('asc', 'desc')


class ProtocolType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('BRIDGE', 'EXCHANGE', 'GENERIC', 'LENDING', 'YIELD')


class Protocol_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('cumulativeProtocolSideRevenueUSD', 'cumulativeSupplySideRevenueUSD', 'cumulativeTotalRevenueUSD', 'cumulativeUniqueUsers', 'dailyUsageMetrics', 'financialMetrics', 'hourlyUsageMetrics', 'id', 'methodologyVersion', 'name', 'network', 'protocolControlledValueUSD', 'schemaVersion', 'slug', 'subgraphVersion', 'totalPoolCount', 'totalValueLockedUSD', 'type')


class RewardTokenType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('BORROW', 'DEPOSIT')


class RewardToken_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'token', 'token___largePriceChangeBuffer', 'token___largeTVLImpactBuffer', 'token___totalSupply', 'token___totalValueLockedUSD', 'token__decimals', 'token__id', 'token__isBasePoolLpToken', 'token__lastPriceBlockNumber', 'token__lastPriceUSD', 'token__name', 'token__oracleType', 'token__symbol', 'type')


String = sgqlc.types.String

class Swap_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('amountIn', 'amountInUSD', 'amountOut', 'amountOutUSD', 'blockNumber', 'from', 'hash', 'id', 'logIndex', 'pool', 'pool___gaugeAddress', 'pool___isMetapool', 'pool___registryAddress', 'pool___tvlUSDExcludingBasePoolLpTokens', 'pool__createdBlockNumber', 'pool__createdTimestamp', 'pool__cumulativeProtocolSideRevenueUSD', 'pool__cumulativeSupplySideRevenueUSD', 'pool__cumulativeTotalRevenueUSD', 'pool__cumulativeVolumeUSD', 'pool__id', 'pool__isSingleSided', 'pool__name', 'pool__outputTokenPriceUSD', 'pool__outputTokenSupply', 'pool__stakedOutputTokenAmount', 'pool__symbol', 'pool__totalValueLockedUSD', 'protocol', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'timestamp', 'to', 'tokenIn', 'tokenIn___largePriceChangeBuffer', 'tokenIn___largeTVLImpactBuffer', 'tokenIn___totalSupply', 'tokenIn___totalValueLockedUSD', 'tokenIn__decimals', 'tokenIn__id', 'tokenIn__isBasePoolLpToken', 'tokenIn__lastPriceBlockNumber', 'tokenIn__lastPriceUSD', 'tokenIn__name', 'tokenIn__oracleType', 'tokenIn__symbol', 'tokenOut', 'tokenOut___largePriceChangeBuffer', 'tokenOut___largeTVLImpactBuffer', 'tokenOut___totalSupply', 'tokenOut___totalValueLockedUSD', 'tokenOut__decimals', 'tokenOut__id', 'tokenOut__isBasePoolLpToken', 'tokenOut__lastPriceBlockNumber', 'tokenOut__lastPriceUSD', 'tokenOut__name', 'tokenOut__oracleType', 'tokenOut__symbol')


class Timestamp(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class Token_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('_largePriceChangeBuffer', '_largeTVLImpactBuffer', '_totalSupply', '_totalValueLockedUSD', 'decimals', 'id', 'isBasePoolLpToken', 'lastPriceBlockNumber', 'lastPriceUSD', 'name', 'oracleType', 'symbol')


class UsageMetricsDailySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('blockNumber', 'cumulativeUniqueUsers', 'dailyActiveUsers', 'dailyDepositCount', 'dailySwapCount', 'dailyTransactionCount', 'dailyWithdrawCount', 'id', 'protocol', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'timestamp', 'totalPoolCount')


class UsageMetricsHourlySnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('blockNumber', 'cumulativeUniqueUsers', 'hourlyActiveUsers', 'hourlyDepositCount', 'hourlySwapCount', 'hourlyTransactionCount', 'hourlyWithdrawCount', 'id', 'protocol', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'timestamp')


class Withdraw_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('amountUSD', 'blockNumber', 'from', 'hash', 'id', 'inputTokenAmounts', 'inputTokens', 'logIndex', 'outputToken', 'outputTokenAmount', 'outputToken___largePriceChangeBuffer', 'outputToken___largeTVLImpactBuffer', 'outputToken___totalSupply', 'outputToken___totalValueLockedUSD', 'outputToken__decimals', 'outputToken__id', 'outputToken__isBasePoolLpToken', 'outputToken__lastPriceBlockNumber', 'outputToken__lastPriceUSD', 'outputToken__name', 'outputToken__oracleType', 'outputToken__symbol', 'pool', 'pool___gaugeAddress', 'pool___isMetapool', 'pool___registryAddress', 'pool___tvlUSDExcludingBasePoolLpTokens', 'pool__createdBlockNumber', 'pool__createdTimestamp', 'pool__cumulativeProtocolSideRevenueUSD', 'pool__cumulativeSupplySideRevenueUSD', 'pool__cumulativeTotalRevenueUSD', 'pool__cumulativeVolumeUSD', 'pool__id', 'pool__isSingleSided', 'pool__name', 'pool__outputTokenPriceUSD', 'pool__outputTokenSupply', 'pool__stakedOutputTokenAmount', 'pool__symbol', 'pool__totalValueLockedUSD', 'protocol', 'protocol__cumulativeProtocolSideRevenueUSD', 'protocol__cumulativeSupplySideRevenueUSD', 'protocol__cumulativeTotalRevenueUSD', 'protocol__cumulativeUniqueUsers', 'protocol__cumulativeVolumeUSD', 'protocol__id', 'protocol__methodologyVersion', 'protocol__name', 'protocol__network', 'protocol__protocolControlledValueUSD', 'protocol__schemaVersion', 'protocol__slug', 'protocol__subgraphVersion', 'protocol__totalPoolCount', 'protocol__totalValueLockedUSD', 'protocol__type', 'timestamp', 'to')


class _CircularBuffer_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('blocks', 'blocksPerDay', 'bufferSize', 'id', 'nextIndex', 'windowStartIndex')


class _LiquidityGauge_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'poolAddress')


class _LpToken_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'poolAddress', 'registryAddress')


class _SubgraphErrorPolicy_(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('allow', 'deny')



########################################################################
# Input Objects
########################################################################
class Account_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Account_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Account_filter'), graphql_name='or')


class ActiveAccount_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('ActiveAccount_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('ActiveAccount_filter'), graphql_name='or')


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


class Deposit_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'input_tokens', 'input_tokens_not', 'input_tokens_contains', 'input_tokens_contains_nocase', 'input_tokens_not_contains', 'input_tokens_not_contains_nocase', 'input_tokens_', 'output_token', 'output_token_not', 'output_token_gt', 'output_token_lt', 'output_token_gte', 'output_token_lte', 'output_token_in', 'output_token_not_in', 'output_token_contains', 'output_token_contains_nocase', 'output_token_not_contains', 'output_token_not_contains_nocase', 'output_token_starts_with', 'output_token_starts_with_nocase', 'output_token_not_starts_with', 'output_token_not_starts_with_nocase', 'output_token_ends_with', 'output_token_ends_with_nocase', 'output_token_not_ends_with', 'output_token_not_ends_with_nocase', 'output_token_', 'input_token_amounts', 'input_token_amounts_not', 'input_token_amounts_contains', 'input_token_amounts_contains_nocase', 'input_token_amounts_not_contains', 'input_token_amounts_not_contains_nocase', 'output_token_amount', 'output_token_amount_not', 'output_token_amount_gt', 'output_token_amount_lt', 'output_token_amount_gte', 'output_token_amount_lte', 'output_token_amount_in', 'output_token_amount_not_in', 'amount_usd', 'amount_usd_not', 'amount_usd_gt', 'amount_usd_lt', 'amount_usd_gte', 'amount_usd_lte', 'amount_usd_in', 'amount_usd_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field('DexAmmProtocol_filter', graphql_name='protocol_')
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
    input_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens')
    input_tokens_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_not')
    input_tokens_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_contains')
    input_tokens_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_contains_nocase')
    input_tokens_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_not_contains')
    input_tokens_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_not_contains_nocase')
    input_tokens_ = sgqlc.types.Field('Token_filter', graphql_name='inputTokens_')
    output_token = sgqlc.types.Field(String, graphql_name='outputToken')
    output_token_not = sgqlc.types.Field(String, graphql_name='outputToken_not')
    output_token_gt = sgqlc.types.Field(String, graphql_name='outputToken_gt')
    output_token_lt = sgqlc.types.Field(String, graphql_name='outputToken_lt')
    output_token_gte = sgqlc.types.Field(String, graphql_name='outputToken_gte')
    output_token_lte = sgqlc.types.Field(String, graphql_name='outputToken_lte')
    output_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='outputToken_in')
    output_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='outputToken_not_in')
    output_token_contains = sgqlc.types.Field(String, graphql_name='outputToken_contains')
    output_token_contains_nocase = sgqlc.types.Field(String, graphql_name='outputToken_contains_nocase')
    output_token_not_contains = sgqlc.types.Field(String, graphql_name='outputToken_not_contains')
    output_token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_contains_nocase')
    output_token_starts_with = sgqlc.types.Field(String, graphql_name='outputToken_starts_with')
    output_token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_starts_with_nocase')
    output_token_not_starts_with = sgqlc.types.Field(String, graphql_name='outputToken_not_starts_with')
    output_token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_starts_with_nocase')
    output_token_ends_with = sgqlc.types.Field(String, graphql_name='outputToken_ends_with')
    output_token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_ends_with_nocase')
    output_token_not_ends_with = sgqlc.types.Field(String, graphql_name='outputToken_not_ends_with')
    output_token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_ends_with_nocase')
    output_token_ = sgqlc.types.Field('Token_filter', graphql_name='outputToken_')
    input_token_amounts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts')
    input_token_amounts_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_not')
    input_token_amounts_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_contains')
    input_token_amounts_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_contains_nocase')
    input_token_amounts_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_not_contains')
    input_token_amounts_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_not_contains_nocase')
    output_token_amount = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount')
    output_token_amount_not = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_not')
    output_token_amount_gt = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_gt')
    output_token_amount_lt = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_lt')
    output_token_amount_gte = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_gte')
    output_token_amount_lte = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_lte')
    output_token_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenAmount_in')
    output_token_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenAmount_not_in')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_not')
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gt')
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lt')
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gte')
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lte')
    amount_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_in')
    amount_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_not_in')
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
    pool_ = sgqlc.types.Field('LiquidityPool_filter', graphql_name='pool_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Deposit_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Deposit_filter'), graphql_name='or')


class DexAmmProtocol_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'slug', 'slug_not', 'slug_gt', 'slug_lt', 'slug_gte', 'slug_lte', 'slug_in', 'slug_not_in', 'slug_contains', 'slug_contains_nocase', 'slug_not_contains', 'slug_not_contains_nocase', 'slug_starts_with', 'slug_starts_with_nocase', 'slug_not_starts_with', 'slug_not_starts_with_nocase', 'slug_ends_with', 'slug_ends_with_nocase', 'slug_not_ends_with', 'slug_not_ends_with_nocase', 'schema_version', 'schema_version_not', 'schema_version_gt', 'schema_version_lt', 'schema_version_gte', 'schema_version_lte', 'schema_version_in', 'schema_version_not_in', 'schema_version_contains', 'schema_version_contains_nocase', 'schema_version_not_contains', 'schema_version_not_contains_nocase', 'schema_version_starts_with', 'schema_version_starts_with_nocase', 'schema_version_not_starts_with', 'schema_version_not_starts_with_nocase', 'schema_version_ends_with', 'schema_version_ends_with_nocase', 'schema_version_not_ends_with', 'schema_version_not_ends_with_nocase', 'subgraph_version', 'subgraph_version_not', 'subgraph_version_gt', 'subgraph_version_lt', 'subgraph_version_gte', 'subgraph_version_lte', 'subgraph_version_in', 'subgraph_version_not_in', 'subgraph_version_contains', 'subgraph_version_contains_nocase', 'subgraph_version_not_contains', 'subgraph_version_not_contains_nocase', 'subgraph_version_starts_with', 'subgraph_version_starts_with_nocase', 'subgraph_version_not_starts_with', 'subgraph_version_not_starts_with_nocase', 'subgraph_version_ends_with', 'subgraph_version_ends_with_nocase', 'subgraph_version_not_ends_with', 'subgraph_version_not_ends_with_nocase', 'methodology_version', 'methodology_version_not', 'methodology_version_gt', 'methodology_version_lt', 'methodology_version_gte', 'methodology_version_lte', 'methodology_version_in', 'methodology_version_not_in', 'methodology_version_contains', 'methodology_version_contains_nocase', 'methodology_version_not_contains', 'methodology_version_not_contains_nocase', 'methodology_version_starts_with', 'methodology_version_starts_with_nocase', 'methodology_version_not_starts_with', 'methodology_version_not_starts_with_nocase', 'methodology_version_ends_with', 'methodology_version_ends_with_nocase', 'methodology_version_not_ends_with', 'methodology_version_not_ends_with_nocase', 'network', 'network_not', 'network_in', 'network_not_in', 'type', 'type_not', 'type_in', 'type_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'protocol_controlled_value_usd', 'protocol_controlled_value_usd_not', 'protocol_controlled_value_usd_gt', 'protocol_controlled_value_usd_lt', 'protocol_controlled_value_usd_gte', 'protocol_controlled_value_usd_lte', 'protocol_controlled_value_usd_in', 'protocol_controlled_value_usd_not_in', 'cumulative_volume_usd', 'cumulative_volume_usd_not', 'cumulative_volume_usd_gt', 'cumulative_volume_usd_lt', 'cumulative_volume_usd_gte', 'cumulative_volume_usd_lte', 'cumulative_volume_usd_in', 'cumulative_volume_usd_not_in', 'cumulative_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd_not', 'cumulative_supply_side_revenue_usd_gt', 'cumulative_supply_side_revenue_usd_lt', 'cumulative_supply_side_revenue_usd_gte', 'cumulative_supply_side_revenue_usd_lte', 'cumulative_supply_side_revenue_usd_in', 'cumulative_supply_side_revenue_usd_not_in', 'cumulative_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd_not', 'cumulative_protocol_side_revenue_usd_gt', 'cumulative_protocol_side_revenue_usd_lt', 'cumulative_protocol_side_revenue_usd_gte', 'cumulative_protocol_side_revenue_usd_lte', 'cumulative_protocol_side_revenue_usd_in', 'cumulative_protocol_side_revenue_usd_not_in', 'cumulative_total_revenue_usd', 'cumulative_total_revenue_usd_not', 'cumulative_total_revenue_usd_gt', 'cumulative_total_revenue_usd_lt', 'cumulative_total_revenue_usd_gte', 'cumulative_total_revenue_usd_lte', 'cumulative_total_revenue_usd_in', 'cumulative_total_revenue_usd_not_in', 'cumulative_unique_users', 'cumulative_unique_users_not', 'cumulative_unique_users_gt', 'cumulative_unique_users_lt', 'cumulative_unique_users_gte', 'cumulative_unique_users_lte', 'cumulative_unique_users_in', 'cumulative_unique_users_not_in', 'total_pool_count', 'total_pool_count_not', 'total_pool_count_gt', 'total_pool_count_lt', 'total_pool_count_gte', 'total_pool_count_lte', 'total_pool_count_in', 'total_pool_count_not_in', 'daily_usage_metrics_', 'hourly_usage_metrics_', 'financial_metrics_', 'pools_', '_pool_ids', '_pool_ids_not', '_pool_ids_contains', '_pool_ids_contains_nocase', '_pool_ids_not_contains', '_pool_ids_not_contains_nocase', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
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
    slug = sgqlc.types.Field(String, graphql_name='slug')
    slug_not = sgqlc.types.Field(String, graphql_name='slug_not')
    slug_gt = sgqlc.types.Field(String, graphql_name='slug_gt')
    slug_lt = sgqlc.types.Field(String, graphql_name='slug_lt')
    slug_gte = sgqlc.types.Field(String, graphql_name='slug_gte')
    slug_lte = sgqlc.types.Field(String, graphql_name='slug_lte')
    slug_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='slug_in')
    slug_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='slug_not_in')
    slug_contains = sgqlc.types.Field(String, graphql_name='slug_contains')
    slug_contains_nocase = sgqlc.types.Field(String, graphql_name='slug_contains_nocase')
    slug_not_contains = sgqlc.types.Field(String, graphql_name='slug_not_contains')
    slug_not_contains_nocase = sgqlc.types.Field(String, graphql_name='slug_not_contains_nocase')
    slug_starts_with = sgqlc.types.Field(String, graphql_name='slug_starts_with')
    slug_starts_with_nocase = sgqlc.types.Field(String, graphql_name='slug_starts_with_nocase')
    slug_not_starts_with = sgqlc.types.Field(String, graphql_name='slug_not_starts_with')
    slug_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='slug_not_starts_with_nocase')
    slug_ends_with = sgqlc.types.Field(String, graphql_name='slug_ends_with')
    slug_ends_with_nocase = sgqlc.types.Field(String, graphql_name='slug_ends_with_nocase')
    slug_not_ends_with = sgqlc.types.Field(String, graphql_name='slug_not_ends_with')
    slug_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='slug_not_ends_with_nocase')
    schema_version = sgqlc.types.Field(String, graphql_name='schemaVersion')
    schema_version_not = sgqlc.types.Field(String, graphql_name='schemaVersion_not')
    schema_version_gt = sgqlc.types.Field(String, graphql_name='schemaVersion_gt')
    schema_version_lt = sgqlc.types.Field(String, graphql_name='schemaVersion_lt')
    schema_version_gte = sgqlc.types.Field(String, graphql_name='schemaVersion_gte')
    schema_version_lte = sgqlc.types.Field(String, graphql_name='schemaVersion_lte')
    schema_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='schemaVersion_in')
    schema_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='schemaVersion_not_in')
    schema_version_contains = sgqlc.types.Field(String, graphql_name='schemaVersion_contains')
    schema_version_contains_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_contains_nocase')
    schema_version_not_contains = sgqlc.types.Field(String, graphql_name='schemaVersion_not_contains')
    schema_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_contains_nocase')
    schema_version_starts_with = sgqlc.types.Field(String, graphql_name='schemaVersion_starts_with')
    schema_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_starts_with_nocase')
    schema_version_not_starts_with = sgqlc.types.Field(String, graphql_name='schemaVersion_not_starts_with')
    schema_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_starts_with_nocase')
    schema_version_ends_with = sgqlc.types.Field(String, graphql_name='schemaVersion_ends_with')
    schema_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_ends_with_nocase')
    schema_version_not_ends_with = sgqlc.types.Field(String, graphql_name='schemaVersion_not_ends_with')
    schema_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_ends_with_nocase')
    subgraph_version = sgqlc.types.Field(String, graphql_name='subgraphVersion')
    subgraph_version_not = sgqlc.types.Field(String, graphql_name='subgraphVersion_not')
    subgraph_version_gt = sgqlc.types.Field(String, graphql_name='subgraphVersion_gt')
    subgraph_version_lt = sgqlc.types.Field(String, graphql_name='subgraphVersion_lt')
    subgraph_version_gte = sgqlc.types.Field(String, graphql_name='subgraphVersion_gte')
    subgraph_version_lte = sgqlc.types.Field(String, graphql_name='subgraphVersion_lte')
    subgraph_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subgraphVersion_in')
    subgraph_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subgraphVersion_not_in')
    subgraph_version_contains = sgqlc.types.Field(String, graphql_name='subgraphVersion_contains')
    subgraph_version_contains_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_contains_nocase')
    subgraph_version_not_contains = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_contains')
    subgraph_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_contains_nocase')
    subgraph_version_starts_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_starts_with')
    subgraph_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_starts_with_nocase')
    subgraph_version_not_starts_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_starts_with')
    subgraph_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_starts_with_nocase')
    subgraph_version_ends_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_ends_with')
    subgraph_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_ends_with_nocase')
    subgraph_version_not_ends_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_ends_with')
    subgraph_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_ends_with_nocase')
    methodology_version = sgqlc.types.Field(String, graphql_name='methodologyVersion')
    methodology_version_not = sgqlc.types.Field(String, graphql_name='methodologyVersion_not')
    methodology_version_gt = sgqlc.types.Field(String, graphql_name='methodologyVersion_gt')
    methodology_version_lt = sgqlc.types.Field(String, graphql_name='methodologyVersion_lt')
    methodology_version_gte = sgqlc.types.Field(String, graphql_name='methodologyVersion_gte')
    methodology_version_lte = sgqlc.types.Field(String, graphql_name='methodologyVersion_lte')
    methodology_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='methodologyVersion_in')
    methodology_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='methodologyVersion_not_in')
    methodology_version_contains = sgqlc.types.Field(String, graphql_name='methodologyVersion_contains')
    methodology_version_contains_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_contains_nocase')
    methodology_version_not_contains = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_contains')
    methodology_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_contains_nocase')
    methodology_version_starts_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_starts_with')
    methodology_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_starts_with_nocase')
    methodology_version_not_starts_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_starts_with')
    methodology_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_starts_with_nocase')
    methodology_version_ends_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_ends_with')
    methodology_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_ends_with_nocase')
    methodology_version_not_ends_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_ends_with')
    methodology_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_ends_with_nocase')
    network = sgqlc.types.Field(Network, graphql_name='network')
    network_not = sgqlc.types.Field(Network, graphql_name='network_not')
    network_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Network)), graphql_name='network_in')
    network_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Network)), graphql_name='network_not_in')
    type = sgqlc.types.Field(ProtocolType, graphql_name='type')
    type_not = sgqlc.types.Field(ProtocolType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolType)), graphql_name='type_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    protocol_controlled_value_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_not')
    protocol_controlled_value_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gt')
    protocol_controlled_value_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lt')
    protocol_controlled_value_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gte')
    protocol_controlled_value_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lte')
    protocol_controlled_value_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_in')
    protocol_controlled_value_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_not_in')
    cumulative_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD')
    cumulative_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_not')
    cumulative_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gt')
    cumulative_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lt')
    cumulative_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gte')
    cumulative_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lte')
    cumulative_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_in')
    cumulative_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_not_in')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_not')
    cumulative_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gt')
    cumulative_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lt')
    cumulative_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gte')
    cumulative_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lte')
    cumulative_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_in')
    cumulative_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_not_in')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_not')
    cumulative_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gt')
    cumulative_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lt')
    cumulative_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gte')
    cumulative_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lte')
    cumulative_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_in')
    cumulative_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_not_in')
    cumulative_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD')
    cumulative_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_not')
    cumulative_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gt')
    cumulative_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lt')
    cumulative_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gte')
    cumulative_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lte')
    cumulative_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_in')
    cumulative_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_not_in')
    cumulative_unique_users = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers')
    cumulative_unique_users_not = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_not')
    cumulative_unique_users_gt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gt')
    cumulative_unique_users_lt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lt')
    cumulative_unique_users_gte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gte')
    cumulative_unique_users_lte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lte')
    cumulative_unique_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_in')
    cumulative_unique_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_not_in')
    total_pool_count = sgqlc.types.Field(Int, graphql_name='totalPoolCount')
    total_pool_count_not = sgqlc.types.Field(Int, graphql_name='totalPoolCount_not')
    total_pool_count_gt = sgqlc.types.Field(Int, graphql_name='totalPoolCount_gt')
    total_pool_count_lt = sgqlc.types.Field(Int, graphql_name='totalPoolCount_lt')
    total_pool_count_gte = sgqlc.types.Field(Int, graphql_name='totalPoolCount_gte')
    total_pool_count_lte = sgqlc.types.Field(Int, graphql_name='totalPoolCount_lte')
    total_pool_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='totalPoolCount_in')
    total_pool_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='totalPoolCount_not_in')
    daily_usage_metrics_ = sgqlc.types.Field('UsageMetricsDailySnapshot_filter', graphql_name='dailyUsageMetrics_')
    hourly_usage_metrics_ = sgqlc.types.Field('UsageMetricsHourlySnapshot_filter', graphql_name='hourlyUsageMetrics_')
    financial_metrics_ = sgqlc.types.Field('FinancialsDailySnapshot_filter', graphql_name='financialMetrics_')
    pools_ = sgqlc.types.Field('LiquidityPool_filter', graphql_name='pools_')
    _pool_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_poolIds')
    _pool_ids_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_poolIds_not')
    _pool_ids_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_poolIds_contains')
    _pool_ids_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_poolIds_contains_nocase')
    _pool_ids_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_poolIds_not_contains')
    _pool_ids_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_poolIds_not_contains_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('DexAmmProtocol_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('DexAmmProtocol_filter'), graphql_name='or')


class Event_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field(DexAmmProtocol_filter, graphql_name='protocol_')
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
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Event_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Event_filter'), graphql_name='or')


class FinancialsDailySnapshot_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'protocol_controlled_value_usd', 'protocol_controlled_value_usd_not', 'protocol_controlled_value_usd_gt', 'protocol_controlled_value_usd_lt', 'protocol_controlled_value_usd_gte', 'protocol_controlled_value_usd_lte', 'protocol_controlled_value_usd_in', 'protocol_controlled_value_usd_not_in', 'daily_volume_usd', 'daily_volume_usd_not', 'daily_volume_usd_gt', 'daily_volume_usd_lt', 'daily_volume_usd_gte', 'daily_volume_usd_lte', 'daily_volume_usd_in', 'daily_volume_usd_not_in', 'cumulative_volume_usd', 'cumulative_volume_usd_not', 'cumulative_volume_usd_gt', 'cumulative_volume_usd_lt', 'cumulative_volume_usd_gte', 'cumulative_volume_usd_lte', 'cumulative_volume_usd_in', 'cumulative_volume_usd_not_in', 'daily_supply_side_revenue_usd', 'daily_supply_side_revenue_usd_not', 'daily_supply_side_revenue_usd_gt', 'daily_supply_side_revenue_usd_lt', 'daily_supply_side_revenue_usd_gte', 'daily_supply_side_revenue_usd_lte', 'daily_supply_side_revenue_usd_in', 'daily_supply_side_revenue_usd_not_in', 'cumulative_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd_not', 'cumulative_supply_side_revenue_usd_gt', 'cumulative_supply_side_revenue_usd_lt', 'cumulative_supply_side_revenue_usd_gte', 'cumulative_supply_side_revenue_usd_lte', 'cumulative_supply_side_revenue_usd_in', 'cumulative_supply_side_revenue_usd_not_in', 'daily_protocol_side_revenue_usd', 'daily_protocol_side_revenue_usd_not', 'daily_protocol_side_revenue_usd_gt', 'daily_protocol_side_revenue_usd_lt', 'daily_protocol_side_revenue_usd_gte', 'daily_protocol_side_revenue_usd_lte', 'daily_protocol_side_revenue_usd_in', 'daily_protocol_side_revenue_usd_not_in', 'cumulative_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd_not', 'cumulative_protocol_side_revenue_usd_gt', 'cumulative_protocol_side_revenue_usd_lt', 'cumulative_protocol_side_revenue_usd_gte', 'cumulative_protocol_side_revenue_usd_lte', 'cumulative_protocol_side_revenue_usd_in', 'cumulative_protocol_side_revenue_usd_not_in', 'daily_total_revenue_usd', 'daily_total_revenue_usd_not', 'daily_total_revenue_usd_gt', 'daily_total_revenue_usd_lt', 'daily_total_revenue_usd_gte', 'daily_total_revenue_usd_lte', 'daily_total_revenue_usd_in', 'daily_total_revenue_usd_not_in', 'cumulative_total_revenue_usd', 'cumulative_total_revenue_usd_not', 'cumulative_total_revenue_usd_gt', 'cumulative_total_revenue_usd_lt', 'cumulative_total_revenue_usd_gte', 'cumulative_total_revenue_usd_lte', 'cumulative_total_revenue_usd_in', 'cumulative_total_revenue_usd_not_in', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field(DexAmmProtocol_filter, graphql_name='protocol_')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    protocol_controlled_value_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_not')
    protocol_controlled_value_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gt')
    protocol_controlled_value_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lt')
    protocol_controlled_value_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gte')
    protocol_controlled_value_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lte')
    protocol_controlled_value_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_in')
    protocol_controlled_value_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_not_in')
    daily_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD')
    daily_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_not')
    daily_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_gt')
    daily_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_lt')
    daily_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_gte')
    daily_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_lte')
    daily_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeUSD_in')
    daily_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeUSD_not_in')
    cumulative_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD')
    cumulative_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_not')
    cumulative_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gt')
    cumulative_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lt')
    cumulative_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gte')
    cumulative_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lte')
    cumulative_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_in')
    cumulative_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_not_in')
    daily_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD')
    daily_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_not')
    daily_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_gt')
    daily_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_lt')
    daily_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_gte')
    daily_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_lte')
    daily_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailySupplySideRevenueUSD_in')
    daily_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailySupplySideRevenueUSD_not_in')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_not')
    cumulative_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gt')
    cumulative_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lt')
    cumulative_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gte')
    cumulative_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lte')
    cumulative_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_in')
    cumulative_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_not_in')
    daily_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD')
    daily_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_not')
    daily_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_gt')
    daily_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_lt')
    daily_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_gte')
    daily_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_lte')
    daily_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyProtocolSideRevenueUSD_in')
    daily_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyProtocolSideRevenueUSD_not_in')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_not')
    cumulative_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gt')
    cumulative_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lt')
    cumulative_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gte')
    cumulative_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lte')
    cumulative_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_in')
    cumulative_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_not_in')
    daily_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD')
    daily_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_not')
    daily_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_gt')
    daily_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_lt')
    daily_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_gte')
    daily_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_lte')
    daily_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyTotalRevenueUSD_in')
    daily_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyTotalRevenueUSD_not_in')
    cumulative_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD')
    cumulative_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_not')
    cumulative_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gt')
    cumulative_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lt')
    cumulative_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gte')
    cumulative_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lte')
    cumulative_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_in')
    cumulative_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_not_in')
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
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('FinancialsDailySnapshot_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('FinancialsDailySnapshot_filter'), graphql_name='or')


class LiquidityPoolDailySnapshot_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'cumulative_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd_not', 'cumulative_supply_side_revenue_usd_gt', 'cumulative_supply_side_revenue_usd_lt', 'cumulative_supply_side_revenue_usd_gte', 'cumulative_supply_side_revenue_usd_lte', 'cumulative_supply_side_revenue_usd_in', 'cumulative_supply_side_revenue_usd_not_in', 'daily_supply_side_revenue_usd', 'daily_supply_side_revenue_usd_not', 'daily_supply_side_revenue_usd_gt', 'daily_supply_side_revenue_usd_lt', 'daily_supply_side_revenue_usd_gte', 'daily_supply_side_revenue_usd_lte', 'daily_supply_side_revenue_usd_in', 'daily_supply_side_revenue_usd_not_in', 'cumulative_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd_not', 'cumulative_protocol_side_revenue_usd_gt', 'cumulative_protocol_side_revenue_usd_lt', 'cumulative_protocol_side_revenue_usd_gte', 'cumulative_protocol_side_revenue_usd_lte', 'cumulative_protocol_side_revenue_usd_in', 'cumulative_protocol_side_revenue_usd_not_in', 'daily_protocol_side_revenue_usd', 'daily_protocol_side_revenue_usd_not', 'daily_protocol_side_revenue_usd_gt', 'daily_protocol_side_revenue_usd_lt', 'daily_protocol_side_revenue_usd_gte', 'daily_protocol_side_revenue_usd_lte', 'daily_protocol_side_revenue_usd_in', 'daily_protocol_side_revenue_usd_not_in', 'cumulative_total_revenue_usd', 'cumulative_total_revenue_usd_not', 'cumulative_total_revenue_usd_gt', 'cumulative_total_revenue_usd_lt', 'cumulative_total_revenue_usd_gte', 'cumulative_total_revenue_usd_lte', 'cumulative_total_revenue_usd_in', 'cumulative_total_revenue_usd_not_in', 'daily_total_revenue_usd', 'daily_total_revenue_usd_not', 'daily_total_revenue_usd_gt', 'daily_total_revenue_usd_lt', 'daily_total_revenue_usd_gte', 'daily_total_revenue_usd_lte', 'daily_total_revenue_usd_in', 'daily_total_revenue_usd_not_in', 'daily_volume_usd', 'daily_volume_usd_not', 'daily_volume_usd_gt', 'daily_volume_usd_lt', 'daily_volume_usd_gte', 'daily_volume_usd_lte', 'daily_volume_usd_in', 'daily_volume_usd_not_in', 'daily_volume_by_token_amount', 'daily_volume_by_token_amount_not', 'daily_volume_by_token_amount_contains', 'daily_volume_by_token_amount_contains_nocase', 'daily_volume_by_token_amount_not_contains', 'daily_volume_by_token_amount_not_contains_nocase', 'daily_volume_by_token_usd', 'daily_volume_by_token_usd_not', 'daily_volume_by_token_usd_contains', 'daily_volume_by_token_usd_contains_nocase', 'daily_volume_by_token_usd_not_contains', 'daily_volume_by_token_usd_not_contains_nocase', 'cumulative_volume_usd', 'cumulative_volume_usd_not', 'cumulative_volume_usd_gt', 'cumulative_volume_usd_lt', 'cumulative_volume_usd_gte', 'cumulative_volume_usd_lte', 'cumulative_volume_usd_in', 'cumulative_volume_usd_not_in', 'input_token_balances', 'input_token_balances_not', 'input_token_balances_contains', 'input_token_balances_contains_nocase', 'input_token_balances_not_contains', 'input_token_balances_not_contains_nocase', 'input_token_weights', 'input_token_weights_not', 'input_token_weights_contains', 'input_token_weights_contains_nocase', 'input_token_weights_not_contains', 'input_token_weights_not_contains_nocase', 'output_token_supply', 'output_token_supply_not', 'output_token_supply_gt', 'output_token_supply_lt', 'output_token_supply_gte', 'output_token_supply_lte', 'output_token_supply_in', 'output_token_supply_not_in', 'output_token_price_usd', 'output_token_price_usd_not', 'output_token_price_usd_gt', 'output_token_price_usd_lt', 'output_token_price_usd_gte', 'output_token_price_usd_lte', 'output_token_price_usd_in', 'output_token_price_usd_not_in', 'staked_output_token_amount', 'staked_output_token_amount_not', 'staked_output_token_amount_gt', 'staked_output_token_amount_lt', 'staked_output_token_amount_gte', 'staked_output_token_amount_lte', 'staked_output_token_amount_in', 'staked_output_token_amount_not_in', 'reward_token_emissions_amount', 'reward_token_emissions_amount_not', 'reward_token_emissions_amount_contains', 'reward_token_emissions_amount_contains_nocase', 'reward_token_emissions_amount_not_contains', 'reward_token_emissions_amount_not_contains_nocase', 'reward_token_emissions_usd', 'reward_token_emissions_usd_not', 'reward_token_emissions_usd_contains', 'reward_token_emissions_usd_contains_nocase', 'reward_token_emissions_usd_not_contains', 'reward_token_emissions_usd_not_contains_nocase', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field(DexAmmProtocol_filter, graphql_name='protocol_')
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
    pool_ = sgqlc.types.Field('LiquidityPool_filter', graphql_name='pool_')
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
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_not')
    cumulative_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gt')
    cumulative_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lt')
    cumulative_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gte')
    cumulative_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lte')
    cumulative_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_in')
    cumulative_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_not_in')
    daily_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD')
    daily_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_not')
    daily_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_gt')
    daily_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_lt')
    daily_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_gte')
    daily_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailySupplySideRevenueUSD_lte')
    daily_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailySupplySideRevenueUSD_in')
    daily_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailySupplySideRevenueUSD_not_in')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_not')
    cumulative_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gt')
    cumulative_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lt')
    cumulative_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gte')
    cumulative_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lte')
    cumulative_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_in')
    cumulative_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_not_in')
    daily_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD')
    daily_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_not')
    daily_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_gt')
    daily_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_lt')
    daily_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_gte')
    daily_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyProtocolSideRevenueUSD_lte')
    daily_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyProtocolSideRevenueUSD_in')
    daily_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyProtocolSideRevenueUSD_not_in')
    cumulative_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD')
    cumulative_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_not')
    cumulative_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gt')
    cumulative_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lt')
    cumulative_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gte')
    cumulative_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lte')
    cumulative_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_in')
    cumulative_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_not_in')
    daily_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD')
    daily_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_not')
    daily_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_gt')
    daily_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_lt')
    daily_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_gte')
    daily_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyTotalRevenueUSD_lte')
    daily_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyTotalRevenueUSD_in')
    daily_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyTotalRevenueUSD_not_in')
    daily_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD')
    daily_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_not')
    daily_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_gt')
    daily_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_lt')
    daily_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_gte')
    daily_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='dailyVolumeUSD_lte')
    daily_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeUSD_in')
    daily_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeUSD_not_in')
    daily_volume_by_token_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='dailyVolumeByTokenAmount')
    daily_volume_by_token_amount_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='dailyVolumeByTokenAmount_not')
    daily_volume_by_token_amount_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='dailyVolumeByTokenAmount_contains')
    daily_volume_by_token_amount_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='dailyVolumeByTokenAmount_contains_nocase')
    daily_volume_by_token_amount_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='dailyVolumeByTokenAmount_not_contains')
    daily_volume_by_token_amount_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='dailyVolumeByTokenAmount_not_contains_nocase')
    daily_volume_by_token_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeByTokenUSD')
    daily_volume_by_token_usd_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeByTokenUSD_not')
    daily_volume_by_token_usd_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeByTokenUSD_contains')
    daily_volume_by_token_usd_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeByTokenUSD_contains_nocase')
    daily_volume_by_token_usd_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeByTokenUSD_not_contains')
    daily_volume_by_token_usd_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dailyVolumeByTokenUSD_not_contains_nocase')
    cumulative_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD')
    cumulative_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_not')
    cumulative_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gt')
    cumulative_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lt')
    cumulative_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gte')
    cumulative_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lte')
    cumulative_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_in')
    cumulative_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_not_in')
    input_token_balances = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances')
    input_token_balances_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_not')
    input_token_balances_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_contains')
    input_token_balances_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_contains_nocase')
    input_token_balances_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_not_contains')
    input_token_balances_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_not_contains_nocase')
    input_token_weights = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights')
    input_token_weights_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_not')
    input_token_weights_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_contains')
    input_token_weights_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_contains_nocase')
    input_token_weights_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_not_contains')
    input_token_weights_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_not_contains_nocase')
    output_token_supply = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply')
    output_token_supply_not = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_not')
    output_token_supply_gt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gt')
    output_token_supply_lt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lt')
    output_token_supply_gte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gte')
    output_token_supply_lte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lte')
    output_token_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_in')
    output_token_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_not_in')
    output_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD')
    output_token_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_not')
    output_token_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gt')
    output_token_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lt')
    output_token_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gte')
    output_token_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lte')
    output_token_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_in')
    output_token_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_not_in')
    staked_output_token_amount = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount')
    staked_output_token_amount_not = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_not')
    staked_output_token_amount_gt = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_gt')
    staked_output_token_amount_lt = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_lt')
    staked_output_token_amount_gte = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_gte')
    staked_output_token_amount_lte = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_lte')
    staked_output_token_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='stakedOutputTokenAmount_in')
    staked_output_token_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='stakedOutputTokenAmount_not_in')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_amount_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not')
    reward_token_emissions_amount_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains')
    reward_token_emissions_amount_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains_nocase')
    reward_token_emissions_amount_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains')
    reward_token_emissions_amount_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains_nocase')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')
    reward_token_emissions_usd_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not')
    reward_token_emissions_usd_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains')
    reward_token_emissions_usd_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains_nocase')
    reward_token_emissions_usd_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains')
    reward_token_emissions_usd_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('LiquidityPoolDailySnapshot_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('LiquidityPoolDailySnapshot_filter'), graphql_name='or')


class LiquidityPoolFee_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'fee_percentage', 'fee_percentage_not', 'fee_percentage_gt', 'fee_percentage_lt', 'fee_percentage_gte', 'fee_percentage_lte', 'fee_percentage_in', 'fee_percentage_not_in', 'fee_type', 'fee_type_not', 'fee_type_in', 'fee_type_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    fee_percentage = sgqlc.types.Field(BigDecimal, graphql_name='feePercentage')
    fee_percentage_not = sgqlc.types.Field(BigDecimal, graphql_name='feePercentage_not')
    fee_percentage_gt = sgqlc.types.Field(BigDecimal, graphql_name='feePercentage_gt')
    fee_percentage_lt = sgqlc.types.Field(BigDecimal, graphql_name='feePercentage_lt')
    fee_percentage_gte = sgqlc.types.Field(BigDecimal, graphql_name='feePercentage_gte')
    fee_percentage_lte = sgqlc.types.Field(BigDecimal, graphql_name='feePercentage_lte')
    fee_percentage_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feePercentage_in')
    fee_percentage_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='feePercentage_not_in')
    fee_type = sgqlc.types.Field(LiquidityPoolFeeType, graphql_name='feeType')
    fee_type_not = sgqlc.types.Field(LiquidityPoolFeeType, graphql_name='feeType_not')
    fee_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPoolFeeType)), graphql_name='feeType_in')
    fee_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPoolFeeType)), graphql_name='feeType_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('LiquidityPoolFee_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('LiquidityPoolFee_filter'), graphql_name='or')


class LiquidityPoolHourlySnapshot_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'cumulative_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd_not', 'cumulative_supply_side_revenue_usd_gt', 'cumulative_supply_side_revenue_usd_lt', 'cumulative_supply_side_revenue_usd_gte', 'cumulative_supply_side_revenue_usd_lte', 'cumulative_supply_side_revenue_usd_in', 'cumulative_supply_side_revenue_usd_not_in', 'hourly_supply_side_revenue_usd', 'hourly_supply_side_revenue_usd_not', 'hourly_supply_side_revenue_usd_gt', 'hourly_supply_side_revenue_usd_lt', 'hourly_supply_side_revenue_usd_gte', 'hourly_supply_side_revenue_usd_lte', 'hourly_supply_side_revenue_usd_in', 'hourly_supply_side_revenue_usd_not_in', 'cumulative_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd_not', 'cumulative_protocol_side_revenue_usd_gt', 'cumulative_protocol_side_revenue_usd_lt', 'cumulative_protocol_side_revenue_usd_gte', 'cumulative_protocol_side_revenue_usd_lte', 'cumulative_protocol_side_revenue_usd_in', 'cumulative_protocol_side_revenue_usd_not_in', 'hourly_protocol_side_revenue_usd', 'hourly_protocol_side_revenue_usd_not', 'hourly_protocol_side_revenue_usd_gt', 'hourly_protocol_side_revenue_usd_lt', 'hourly_protocol_side_revenue_usd_gte', 'hourly_protocol_side_revenue_usd_lte', 'hourly_protocol_side_revenue_usd_in', 'hourly_protocol_side_revenue_usd_not_in', 'cumulative_total_revenue_usd', 'cumulative_total_revenue_usd_not', 'cumulative_total_revenue_usd_gt', 'cumulative_total_revenue_usd_lt', 'cumulative_total_revenue_usd_gte', 'cumulative_total_revenue_usd_lte', 'cumulative_total_revenue_usd_in', 'cumulative_total_revenue_usd_not_in', 'hourly_total_revenue_usd', 'hourly_total_revenue_usd_not', 'hourly_total_revenue_usd_gt', 'hourly_total_revenue_usd_lt', 'hourly_total_revenue_usd_gte', 'hourly_total_revenue_usd_lte', 'hourly_total_revenue_usd_in', 'hourly_total_revenue_usd_not_in', 'hourly_volume_usd', 'hourly_volume_usd_not', 'hourly_volume_usd_gt', 'hourly_volume_usd_lt', 'hourly_volume_usd_gte', 'hourly_volume_usd_lte', 'hourly_volume_usd_in', 'hourly_volume_usd_not_in', 'hourly_volume_by_token_amount', 'hourly_volume_by_token_amount_not', 'hourly_volume_by_token_amount_contains', 'hourly_volume_by_token_amount_contains_nocase', 'hourly_volume_by_token_amount_not_contains', 'hourly_volume_by_token_amount_not_contains_nocase', 'hourly_volume_by_token_usd', 'hourly_volume_by_token_usd_not', 'hourly_volume_by_token_usd_contains', 'hourly_volume_by_token_usd_contains_nocase', 'hourly_volume_by_token_usd_not_contains', 'hourly_volume_by_token_usd_not_contains_nocase', 'cumulative_volume_usd', 'cumulative_volume_usd_not', 'cumulative_volume_usd_gt', 'cumulative_volume_usd_lt', 'cumulative_volume_usd_gte', 'cumulative_volume_usd_lte', 'cumulative_volume_usd_in', 'cumulative_volume_usd_not_in', 'input_token_balances', 'input_token_balances_not', 'input_token_balances_contains', 'input_token_balances_contains_nocase', 'input_token_balances_not_contains', 'input_token_balances_not_contains_nocase', 'input_token_weights', 'input_token_weights_not', 'input_token_weights_contains', 'input_token_weights_contains_nocase', 'input_token_weights_not_contains', 'input_token_weights_not_contains_nocase', 'output_token_supply', 'output_token_supply_not', 'output_token_supply_gt', 'output_token_supply_lt', 'output_token_supply_gte', 'output_token_supply_lte', 'output_token_supply_in', 'output_token_supply_not_in', 'output_token_price_usd', 'output_token_price_usd_not', 'output_token_price_usd_gt', 'output_token_price_usd_lt', 'output_token_price_usd_gte', 'output_token_price_usd_lte', 'output_token_price_usd_in', 'output_token_price_usd_not_in', 'staked_output_token_amount', 'staked_output_token_amount_not', 'staked_output_token_amount_gt', 'staked_output_token_amount_lt', 'staked_output_token_amount_gte', 'staked_output_token_amount_lte', 'staked_output_token_amount_in', 'staked_output_token_amount_not_in', 'reward_token_emissions_amount', 'reward_token_emissions_amount_not', 'reward_token_emissions_amount_contains', 'reward_token_emissions_amount_contains_nocase', 'reward_token_emissions_amount_not_contains', 'reward_token_emissions_amount_not_contains_nocase', 'reward_token_emissions_usd', 'reward_token_emissions_usd_not', 'reward_token_emissions_usd_contains', 'reward_token_emissions_usd_contains_nocase', 'reward_token_emissions_usd_not_contains', 'reward_token_emissions_usd_not_contains_nocase', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field(DexAmmProtocol_filter, graphql_name='protocol_')
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
    pool_ = sgqlc.types.Field('LiquidityPool_filter', graphql_name='pool_')
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
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_not')
    cumulative_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gt')
    cumulative_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lt')
    cumulative_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gte')
    cumulative_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lte')
    cumulative_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_in')
    cumulative_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_not_in')
    hourly_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='hourlySupplySideRevenueUSD')
    hourly_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='hourlySupplySideRevenueUSD_not')
    hourly_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='hourlySupplySideRevenueUSD_gt')
    hourly_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='hourlySupplySideRevenueUSD_lt')
    hourly_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='hourlySupplySideRevenueUSD_gte')
    hourly_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='hourlySupplySideRevenueUSD_lte')
    hourly_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlySupplySideRevenueUSD_in')
    hourly_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlySupplySideRevenueUSD_not_in')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_not')
    cumulative_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gt')
    cumulative_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lt')
    cumulative_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gte')
    cumulative_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lte')
    cumulative_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_in')
    cumulative_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_not_in')
    hourly_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='hourlyProtocolSideRevenueUSD')
    hourly_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='hourlyProtocolSideRevenueUSD_not')
    hourly_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyProtocolSideRevenueUSD_gt')
    hourly_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyProtocolSideRevenueUSD_lt')
    hourly_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyProtocolSideRevenueUSD_gte')
    hourly_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyProtocolSideRevenueUSD_lte')
    hourly_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyProtocolSideRevenueUSD_in')
    hourly_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyProtocolSideRevenueUSD_not_in')
    cumulative_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD')
    cumulative_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_not')
    cumulative_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gt')
    cumulative_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lt')
    cumulative_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gte')
    cumulative_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lte')
    cumulative_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_in')
    cumulative_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_not_in')
    hourly_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='hourlyTotalRevenueUSD')
    hourly_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='hourlyTotalRevenueUSD_not')
    hourly_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyTotalRevenueUSD_gt')
    hourly_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyTotalRevenueUSD_lt')
    hourly_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyTotalRevenueUSD_gte')
    hourly_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyTotalRevenueUSD_lte')
    hourly_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyTotalRevenueUSD_in')
    hourly_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyTotalRevenueUSD_not_in')
    hourly_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='hourlyVolumeUSD')
    hourly_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='hourlyVolumeUSD_not')
    hourly_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyVolumeUSD_gt')
    hourly_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='hourlyVolumeUSD_lt')
    hourly_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyVolumeUSD_gte')
    hourly_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='hourlyVolumeUSD_lte')
    hourly_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyVolumeUSD_in')
    hourly_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyVolumeUSD_not_in')
    hourly_volume_by_token_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='hourlyVolumeByTokenAmount')
    hourly_volume_by_token_amount_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='hourlyVolumeByTokenAmount_not')
    hourly_volume_by_token_amount_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='hourlyVolumeByTokenAmount_contains')
    hourly_volume_by_token_amount_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='hourlyVolumeByTokenAmount_contains_nocase')
    hourly_volume_by_token_amount_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='hourlyVolumeByTokenAmount_not_contains')
    hourly_volume_by_token_amount_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='hourlyVolumeByTokenAmount_not_contains_nocase')
    hourly_volume_by_token_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyVolumeByTokenUSD')
    hourly_volume_by_token_usd_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyVolumeByTokenUSD_not')
    hourly_volume_by_token_usd_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyVolumeByTokenUSD_contains')
    hourly_volume_by_token_usd_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyVolumeByTokenUSD_contains_nocase')
    hourly_volume_by_token_usd_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyVolumeByTokenUSD_not_contains')
    hourly_volume_by_token_usd_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='hourlyVolumeByTokenUSD_not_contains_nocase')
    cumulative_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD')
    cumulative_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_not')
    cumulative_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gt')
    cumulative_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lt')
    cumulative_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gte')
    cumulative_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lte')
    cumulative_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_in')
    cumulative_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_not_in')
    input_token_balances = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances')
    input_token_balances_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_not')
    input_token_balances_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_contains')
    input_token_balances_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_contains_nocase')
    input_token_balances_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_not_contains')
    input_token_balances_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_not_contains_nocase')
    input_token_weights = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights')
    input_token_weights_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_not')
    input_token_weights_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_contains')
    input_token_weights_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_contains_nocase')
    input_token_weights_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_not_contains')
    input_token_weights_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_not_contains_nocase')
    output_token_supply = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply')
    output_token_supply_not = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_not')
    output_token_supply_gt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gt')
    output_token_supply_lt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lt')
    output_token_supply_gte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gte')
    output_token_supply_lte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lte')
    output_token_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_in')
    output_token_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_not_in')
    output_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD')
    output_token_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_not')
    output_token_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gt')
    output_token_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lt')
    output_token_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gte')
    output_token_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lte')
    output_token_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_in')
    output_token_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_not_in')
    staked_output_token_amount = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount')
    staked_output_token_amount_not = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_not')
    staked_output_token_amount_gt = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_gt')
    staked_output_token_amount_lt = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_lt')
    staked_output_token_amount_gte = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_gte')
    staked_output_token_amount_lte = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_lte')
    staked_output_token_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='stakedOutputTokenAmount_in')
    staked_output_token_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='stakedOutputTokenAmount_not_in')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_amount_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not')
    reward_token_emissions_amount_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains')
    reward_token_emissions_amount_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains_nocase')
    reward_token_emissions_amount_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains')
    reward_token_emissions_amount_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains_nocase')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')
    reward_token_emissions_usd_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not')
    reward_token_emissions_usd_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains')
    reward_token_emissions_usd_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains_nocase')
    reward_token_emissions_usd_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains')
    reward_token_emissions_usd_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('LiquidityPoolHourlySnapshot_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('LiquidityPoolHourlySnapshot_filter'), graphql_name='or')


class LiquidityPool_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_contains_nocase', 'symbol_not_contains', 'symbol_not_contains_nocase', 'symbol_starts_with', 'symbol_starts_with_nocase', 'symbol_not_starts_with', 'symbol_not_starts_with_nocase', 'symbol_ends_with', 'symbol_ends_with_nocase', 'symbol_not_ends_with', 'symbol_not_ends_with_nocase', 'input_tokens', 'input_tokens_not', 'input_tokens_contains', 'input_tokens_contains_nocase', 'input_tokens_not_contains', 'input_tokens_not_contains_nocase', 'input_tokens_', '_input_tokens_ordered', '_input_tokens_ordered_not', '_input_tokens_ordered_contains', '_input_tokens_ordered_contains_nocase', '_input_tokens_ordered_not_contains', '_input_tokens_ordered_not_contains_nocase', 'output_token', 'output_token_not', 'output_token_gt', 'output_token_lt', 'output_token_gte', 'output_token_lte', 'output_token_in', 'output_token_not_in', 'output_token_contains', 'output_token_contains_nocase', 'output_token_not_contains', 'output_token_not_contains_nocase', 'output_token_starts_with', 'output_token_starts_with_nocase', 'output_token_not_starts_with', 'output_token_not_starts_with_nocase', 'output_token_ends_with', 'output_token_ends_with_nocase', 'output_token_not_ends_with', 'output_token_not_ends_with_nocase', 'output_token_', 'reward_tokens', 'reward_tokens_not', 'reward_tokens_contains', 'reward_tokens_contains_nocase', 'reward_tokens_not_contains', 'reward_tokens_not_contains_nocase', 'reward_tokens_', 'fees', 'fees_not', 'fees_contains', 'fees_contains_nocase', 'fees_not_contains', 'fees_not_contains_nocase', 'fees_', 'is_single_sided', 'is_single_sided_not', 'is_single_sided_in', 'is_single_sided_not_in', 'created_timestamp', 'created_timestamp_not', 'created_timestamp_gt', 'created_timestamp_lt', 'created_timestamp_gte', 'created_timestamp_lte', 'created_timestamp_in', 'created_timestamp_not_in', 'created_block_number', 'created_block_number_not', 'created_block_number_gt', 'created_block_number_lt', 'created_block_number_gte', 'created_block_number_lte', 'created_block_number_in', 'created_block_number_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', '_tvl_usdexcluding_base_pool_lp_tokens', '_tvl_usdexcluding_base_pool_lp_tokens_not', '_tvl_usdexcluding_base_pool_lp_tokens_gt', '_tvl_usdexcluding_base_pool_lp_tokens_lt', '_tvl_usdexcluding_base_pool_lp_tokens_gte', '_tvl_usdexcluding_base_pool_lp_tokens_lte', '_tvl_usdexcluding_base_pool_lp_tokens_in', '_tvl_usdexcluding_base_pool_lp_tokens_not_in', 'cumulative_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd_not', 'cumulative_supply_side_revenue_usd_gt', 'cumulative_supply_side_revenue_usd_lt', 'cumulative_supply_side_revenue_usd_gte', 'cumulative_supply_side_revenue_usd_lte', 'cumulative_supply_side_revenue_usd_in', 'cumulative_supply_side_revenue_usd_not_in', 'cumulative_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd_not', 'cumulative_protocol_side_revenue_usd_gt', 'cumulative_protocol_side_revenue_usd_lt', 'cumulative_protocol_side_revenue_usd_gte', 'cumulative_protocol_side_revenue_usd_lte', 'cumulative_protocol_side_revenue_usd_in', 'cumulative_protocol_side_revenue_usd_not_in', 'cumulative_total_revenue_usd', 'cumulative_total_revenue_usd_not', 'cumulative_total_revenue_usd_gt', 'cumulative_total_revenue_usd_lt', 'cumulative_total_revenue_usd_gte', 'cumulative_total_revenue_usd_lte', 'cumulative_total_revenue_usd_in', 'cumulative_total_revenue_usd_not_in', 'cumulative_volume_usd', 'cumulative_volume_usd_not', 'cumulative_volume_usd_gt', 'cumulative_volume_usd_lt', 'cumulative_volume_usd_gte', 'cumulative_volume_usd_lte', 'cumulative_volume_usd_in', 'cumulative_volume_usd_not_in', 'input_token_balances', 'input_token_balances_not', 'input_token_balances_contains', 'input_token_balances_contains_nocase', 'input_token_balances_not_contains', 'input_token_balances_not_contains_nocase', 'input_token_weights', 'input_token_weights_not', 'input_token_weights_contains', 'input_token_weights_contains_nocase', 'input_token_weights_not_contains', 'input_token_weights_not_contains_nocase', 'output_token_supply', 'output_token_supply_not', 'output_token_supply_gt', 'output_token_supply_lt', 'output_token_supply_gte', 'output_token_supply_lte', 'output_token_supply_in', 'output_token_supply_not_in', 'output_token_price_usd', 'output_token_price_usd_not', 'output_token_price_usd_gt', 'output_token_price_usd_lt', 'output_token_price_usd_gte', 'output_token_price_usd_lte', 'output_token_price_usd_in', 'output_token_price_usd_not_in', 'staked_output_token_amount', 'staked_output_token_amount_not', 'staked_output_token_amount_gt', 'staked_output_token_amount_lt', 'staked_output_token_amount_gte', 'staked_output_token_amount_lte', 'staked_output_token_amount_in', 'staked_output_token_amount_not_in', 'reward_token_emissions_amount', 'reward_token_emissions_amount_not', 'reward_token_emissions_amount_contains', 'reward_token_emissions_amount_contains_nocase', 'reward_token_emissions_amount_not_contains', 'reward_token_emissions_amount_not_contains_nocase', 'reward_token_emissions_usd', 'reward_token_emissions_usd_not', 'reward_token_emissions_usd_contains', 'reward_token_emissions_usd_contains_nocase', 'reward_token_emissions_usd_not_contains', 'reward_token_emissions_usd_not_contains_nocase', 'daily_snapshots_', 'hourly_snapshots_', 'deposits_', 'withdraws_', 'swaps_', '_registry_address', '_registry_address_not', '_registry_address_gt', '_registry_address_lt', '_registry_address_gte', '_registry_address_lte', '_registry_address_in', '_registry_address_not_in', '_registry_address_contains', '_registry_address_contains_nocase', '_registry_address_not_contains', '_registry_address_not_contains_nocase', '_registry_address_starts_with', '_registry_address_starts_with_nocase', '_registry_address_not_starts_with', '_registry_address_not_starts_with_nocase', '_registry_address_ends_with', '_registry_address_ends_with_nocase', '_registry_address_not_ends_with', '_registry_address_not_ends_with_nocase', '_gauge_address', '_gauge_address_not', '_gauge_address_gt', '_gauge_address_lt', '_gauge_address_gte', '_gauge_address_lte', '_gauge_address_in', '_gauge_address_not_in', '_gauge_address_contains', '_gauge_address_contains_nocase', '_gauge_address_not_contains', '_gauge_address_not_contains_nocase', '_gauge_address_starts_with', '_gauge_address_starts_with_nocase', '_gauge_address_not_starts_with', '_gauge_address_not_starts_with_nocase', '_gauge_address_ends_with', '_gauge_address_ends_with_nocase', '_gauge_address_not_ends_with', '_gauge_address_not_ends_with_nocase', '_is_metapool', '_is_metapool_not', '_is_metapool_in', '_is_metapool_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field(DexAmmProtocol_filter, graphql_name='protocol_')
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
    input_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens')
    input_tokens_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_not')
    input_tokens_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_contains')
    input_tokens_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_contains_nocase')
    input_tokens_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_not_contains')
    input_tokens_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_not_contains_nocase')
    input_tokens_ = sgqlc.types.Field('Token_filter', graphql_name='inputTokens_')
    _input_tokens_ordered = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_inputTokensOrdered')
    _input_tokens_ordered_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_inputTokensOrdered_not')
    _input_tokens_ordered_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_inputTokensOrdered_contains')
    _input_tokens_ordered_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_inputTokensOrdered_contains_nocase')
    _input_tokens_ordered_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_inputTokensOrdered_not_contains')
    _input_tokens_ordered_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_inputTokensOrdered_not_contains_nocase')
    output_token = sgqlc.types.Field(String, graphql_name='outputToken')
    output_token_not = sgqlc.types.Field(String, graphql_name='outputToken_not')
    output_token_gt = sgqlc.types.Field(String, graphql_name='outputToken_gt')
    output_token_lt = sgqlc.types.Field(String, graphql_name='outputToken_lt')
    output_token_gte = sgqlc.types.Field(String, graphql_name='outputToken_gte')
    output_token_lte = sgqlc.types.Field(String, graphql_name='outputToken_lte')
    output_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='outputToken_in')
    output_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='outputToken_not_in')
    output_token_contains = sgqlc.types.Field(String, graphql_name='outputToken_contains')
    output_token_contains_nocase = sgqlc.types.Field(String, graphql_name='outputToken_contains_nocase')
    output_token_not_contains = sgqlc.types.Field(String, graphql_name='outputToken_not_contains')
    output_token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_contains_nocase')
    output_token_starts_with = sgqlc.types.Field(String, graphql_name='outputToken_starts_with')
    output_token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_starts_with_nocase')
    output_token_not_starts_with = sgqlc.types.Field(String, graphql_name='outputToken_not_starts_with')
    output_token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_starts_with_nocase')
    output_token_ends_with = sgqlc.types.Field(String, graphql_name='outputToken_ends_with')
    output_token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_ends_with_nocase')
    output_token_not_ends_with = sgqlc.types.Field(String, graphql_name='outputToken_not_ends_with')
    output_token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_ends_with_nocase')
    output_token_ = sgqlc.types.Field('Token_filter', graphql_name='outputToken_')
    reward_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens')
    reward_tokens_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_not')
    reward_tokens_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_contains')
    reward_tokens_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_contains_nocase')
    reward_tokens_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_not_contains')
    reward_tokens_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='rewardTokens_not_contains_nocase')
    reward_tokens_ = sgqlc.types.Field('RewardToken_filter', graphql_name='rewardTokens_')
    fees = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fees')
    fees_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fees_not')
    fees_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fees_contains')
    fees_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fees_contains_nocase')
    fees_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fees_not_contains')
    fees_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fees_not_contains_nocase')
    fees_ = sgqlc.types.Field(LiquidityPoolFee_filter, graphql_name='fees_')
    is_single_sided = sgqlc.types.Field(Boolean, graphql_name='isSingleSided')
    is_single_sided_not = sgqlc.types.Field(Boolean, graphql_name='isSingleSided_not')
    is_single_sided_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isSingleSided_in')
    is_single_sided_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isSingleSided_not_in')
    created_timestamp = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp')
    created_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_not')
    created_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_gt')
    created_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_lt')
    created_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_gte')
    created_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='createdTimestamp_lte')
    created_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdTimestamp_in')
    created_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdTimestamp_not_in')
    created_block_number = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber')
    created_block_number_not = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_not')
    created_block_number_gt = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_gt')
    created_block_number_lt = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_lt')
    created_block_number_gte = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_gte')
    created_block_number_lte = sgqlc.types.Field(BigInt, graphql_name='createdBlockNumber_lte')
    created_block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdBlockNumber_in')
    created_block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='createdBlockNumber_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    _tvl_usdexcluding_base_pool_lp_tokens = sgqlc.types.Field(BigDecimal, graphql_name='_tvlUSDExcludingBasePoolLpTokens')
    _tvl_usdexcluding_base_pool_lp_tokens_not = sgqlc.types.Field(BigDecimal, graphql_name='_tvlUSDExcludingBasePoolLpTokens_not')
    _tvl_usdexcluding_base_pool_lp_tokens_gt = sgqlc.types.Field(BigDecimal, graphql_name='_tvlUSDExcludingBasePoolLpTokens_gt')
    _tvl_usdexcluding_base_pool_lp_tokens_lt = sgqlc.types.Field(BigDecimal, graphql_name='_tvlUSDExcludingBasePoolLpTokens_lt')
    _tvl_usdexcluding_base_pool_lp_tokens_gte = sgqlc.types.Field(BigDecimal, graphql_name='_tvlUSDExcludingBasePoolLpTokens_gte')
    _tvl_usdexcluding_base_pool_lp_tokens_lte = sgqlc.types.Field(BigDecimal, graphql_name='_tvlUSDExcludingBasePoolLpTokens_lte')
    _tvl_usdexcluding_base_pool_lp_tokens_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='_tvlUSDExcludingBasePoolLpTokens_in')
    _tvl_usdexcluding_base_pool_lp_tokens_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='_tvlUSDExcludingBasePoolLpTokens_not_in')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_not')
    cumulative_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gt')
    cumulative_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lt')
    cumulative_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gte')
    cumulative_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lte')
    cumulative_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_in')
    cumulative_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_not_in')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_not')
    cumulative_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gt')
    cumulative_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lt')
    cumulative_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gte')
    cumulative_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lte')
    cumulative_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_in')
    cumulative_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_not_in')
    cumulative_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD')
    cumulative_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_not')
    cumulative_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gt')
    cumulative_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lt')
    cumulative_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gte')
    cumulative_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lte')
    cumulative_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_in')
    cumulative_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_not_in')
    cumulative_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD')
    cumulative_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_not')
    cumulative_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gt')
    cumulative_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lt')
    cumulative_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_gte')
    cumulative_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeVolumeUSD_lte')
    cumulative_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_in')
    cumulative_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeVolumeUSD_not_in')
    input_token_balances = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances')
    input_token_balances_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_not')
    input_token_balances_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_contains')
    input_token_balances_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_contains_nocase')
    input_token_balances_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_not_contains')
    input_token_balances_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenBalances_not_contains_nocase')
    input_token_weights = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights')
    input_token_weights_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_not')
    input_token_weights_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_contains')
    input_token_weights_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_contains_nocase')
    input_token_weights_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_not_contains')
    input_token_weights_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='inputTokenWeights_not_contains_nocase')
    output_token_supply = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply')
    output_token_supply_not = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_not')
    output_token_supply_gt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gt')
    output_token_supply_lt = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lt')
    output_token_supply_gte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_gte')
    output_token_supply_lte = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply_lte')
    output_token_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_in')
    output_token_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenSupply_not_in')
    output_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD')
    output_token_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_not')
    output_token_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gt')
    output_token_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lt')
    output_token_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_gte')
    output_token_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD_lte')
    output_token_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_in')
    output_token_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='outputTokenPriceUSD_not_in')
    staked_output_token_amount = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount')
    staked_output_token_amount_not = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_not')
    staked_output_token_amount_gt = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_gt')
    staked_output_token_amount_lt = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_lt')
    staked_output_token_amount_gte = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_gte')
    staked_output_token_amount_lte = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount_lte')
    staked_output_token_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='stakedOutputTokenAmount_in')
    staked_output_token_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='stakedOutputTokenAmount_not_in')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_amount_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not')
    reward_token_emissions_amount_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains')
    reward_token_emissions_amount_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_contains_nocase')
    reward_token_emissions_amount_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains')
    reward_token_emissions_amount_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount_not_contains_nocase')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')
    reward_token_emissions_usd_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not')
    reward_token_emissions_usd_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains')
    reward_token_emissions_usd_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_contains_nocase')
    reward_token_emissions_usd_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains')
    reward_token_emissions_usd_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD_not_contains_nocase')
    daily_snapshots_ = sgqlc.types.Field(LiquidityPoolDailySnapshot_filter, graphql_name='dailySnapshots_')
    hourly_snapshots_ = sgqlc.types.Field(LiquidityPoolHourlySnapshot_filter, graphql_name='hourlySnapshots_')
    deposits_ = sgqlc.types.Field(Deposit_filter, graphql_name='deposits_')
    withdraws_ = sgqlc.types.Field('Withdraw_filter', graphql_name='withdraws_')
    swaps_ = sgqlc.types.Field('Swap_filter', graphql_name='swaps_')
    _registry_address = sgqlc.types.Field(String, graphql_name='_registryAddress')
    _registry_address_not = sgqlc.types.Field(String, graphql_name='_registryAddress_not')
    _registry_address_gt = sgqlc.types.Field(String, graphql_name='_registryAddress_gt')
    _registry_address_lt = sgqlc.types.Field(String, graphql_name='_registryAddress_lt')
    _registry_address_gte = sgqlc.types.Field(String, graphql_name='_registryAddress_gte')
    _registry_address_lte = sgqlc.types.Field(String, graphql_name='_registryAddress_lte')
    _registry_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_registryAddress_in')
    _registry_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_registryAddress_not_in')
    _registry_address_contains = sgqlc.types.Field(String, graphql_name='_registryAddress_contains')
    _registry_address_contains_nocase = sgqlc.types.Field(String, graphql_name='_registryAddress_contains_nocase')
    _registry_address_not_contains = sgqlc.types.Field(String, graphql_name='_registryAddress_not_contains')
    _registry_address_not_contains_nocase = sgqlc.types.Field(String, graphql_name='_registryAddress_not_contains_nocase')
    _registry_address_starts_with = sgqlc.types.Field(String, graphql_name='_registryAddress_starts_with')
    _registry_address_starts_with_nocase = sgqlc.types.Field(String, graphql_name='_registryAddress_starts_with_nocase')
    _registry_address_not_starts_with = sgqlc.types.Field(String, graphql_name='_registryAddress_not_starts_with')
    _registry_address_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='_registryAddress_not_starts_with_nocase')
    _registry_address_ends_with = sgqlc.types.Field(String, graphql_name='_registryAddress_ends_with')
    _registry_address_ends_with_nocase = sgqlc.types.Field(String, graphql_name='_registryAddress_ends_with_nocase')
    _registry_address_not_ends_with = sgqlc.types.Field(String, graphql_name='_registryAddress_not_ends_with')
    _registry_address_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='_registryAddress_not_ends_with_nocase')
    _gauge_address = sgqlc.types.Field(String, graphql_name='_gaugeAddress')
    _gauge_address_not = sgqlc.types.Field(String, graphql_name='_gaugeAddress_not')
    _gauge_address_gt = sgqlc.types.Field(String, graphql_name='_gaugeAddress_gt')
    _gauge_address_lt = sgqlc.types.Field(String, graphql_name='_gaugeAddress_lt')
    _gauge_address_gte = sgqlc.types.Field(String, graphql_name='_gaugeAddress_gte')
    _gauge_address_lte = sgqlc.types.Field(String, graphql_name='_gaugeAddress_lte')
    _gauge_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_gaugeAddress_in')
    _gauge_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='_gaugeAddress_not_in')
    _gauge_address_contains = sgqlc.types.Field(String, graphql_name='_gaugeAddress_contains')
    _gauge_address_contains_nocase = sgqlc.types.Field(String, graphql_name='_gaugeAddress_contains_nocase')
    _gauge_address_not_contains = sgqlc.types.Field(String, graphql_name='_gaugeAddress_not_contains')
    _gauge_address_not_contains_nocase = sgqlc.types.Field(String, graphql_name='_gaugeAddress_not_contains_nocase')
    _gauge_address_starts_with = sgqlc.types.Field(String, graphql_name='_gaugeAddress_starts_with')
    _gauge_address_starts_with_nocase = sgqlc.types.Field(String, graphql_name='_gaugeAddress_starts_with_nocase')
    _gauge_address_not_starts_with = sgqlc.types.Field(String, graphql_name='_gaugeAddress_not_starts_with')
    _gauge_address_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='_gaugeAddress_not_starts_with_nocase')
    _gauge_address_ends_with = sgqlc.types.Field(String, graphql_name='_gaugeAddress_ends_with')
    _gauge_address_ends_with_nocase = sgqlc.types.Field(String, graphql_name='_gaugeAddress_ends_with_nocase')
    _gauge_address_not_ends_with = sgqlc.types.Field(String, graphql_name='_gaugeAddress_not_ends_with')
    _gauge_address_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='_gaugeAddress_not_ends_with_nocase')
    _is_metapool = sgqlc.types.Field(Boolean, graphql_name='_isMetapool')
    _is_metapool_not = sgqlc.types.Field(Boolean, graphql_name='_isMetapool_not')
    _is_metapool_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='_isMetapool_in')
    _is_metapool_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='_isMetapool_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('LiquidityPool_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('LiquidityPool_filter'), graphql_name='or')


class Protocol_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'slug', 'slug_not', 'slug_gt', 'slug_lt', 'slug_gte', 'slug_lte', 'slug_in', 'slug_not_in', 'slug_contains', 'slug_contains_nocase', 'slug_not_contains', 'slug_not_contains_nocase', 'slug_starts_with', 'slug_starts_with_nocase', 'slug_not_starts_with', 'slug_not_starts_with_nocase', 'slug_ends_with', 'slug_ends_with_nocase', 'slug_not_ends_with', 'slug_not_ends_with_nocase', 'schema_version', 'schema_version_not', 'schema_version_gt', 'schema_version_lt', 'schema_version_gte', 'schema_version_lte', 'schema_version_in', 'schema_version_not_in', 'schema_version_contains', 'schema_version_contains_nocase', 'schema_version_not_contains', 'schema_version_not_contains_nocase', 'schema_version_starts_with', 'schema_version_starts_with_nocase', 'schema_version_not_starts_with', 'schema_version_not_starts_with_nocase', 'schema_version_ends_with', 'schema_version_ends_with_nocase', 'schema_version_not_ends_with', 'schema_version_not_ends_with_nocase', 'subgraph_version', 'subgraph_version_not', 'subgraph_version_gt', 'subgraph_version_lt', 'subgraph_version_gte', 'subgraph_version_lte', 'subgraph_version_in', 'subgraph_version_not_in', 'subgraph_version_contains', 'subgraph_version_contains_nocase', 'subgraph_version_not_contains', 'subgraph_version_not_contains_nocase', 'subgraph_version_starts_with', 'subgraph_version_starts_with_nocase', 'subgraph_version_not_starts_with', 'subgraph_version_not_starts_with_nocase', 'subgraph_version_ends_with', 'subgraph_version_ends_with_nocase', 'subgraph_version_not_ends_with', 'subgraph_version_not_ends_with_nocase', 'methodology_version', 'methodology_version_not', 'methodology_version_gt', 'methodology_version_lt', 'methodology_version_gte', 'methodology_version_lte', 'methodology_version_in', 'methodology_version_not_in', 'methodology_version_contains', 'methodology_version_contains_nocase', 'methodology_version_not_contains', 'methodology_version_not_contains_nocase', 'methodology_version_starts_with', 'methodology_version_starts_with_nocase', 'methodology_version_not_starts_with', 'methodology_version_not_starts_with_nocase', 'methodology_version_ends_with', 'methodology_version_ends_with_nocase', 'methodology_version_not_ends_with', 'methodology_version_not_ends_with_nocase', 'network', 'network_not', 'network_in', 'network_not_in', 'type', 'type_not', 'type_in', 'type_not_in', 'total_value_locked_usd', 'total_value_locked_usd_not', 'total_value_locked_usd_gt', 'total_value_locked_usd_lt', 'total_value_locked_usd_gte', 'total_value_locked_usd_lte', 'total_value_locked_usd_in', 'total_value_locked_usd_not_in', 'protocol_controlled_value_usd', 'protocol_controlled_value_usd_not', 'protocol_controlled_value_usd_gt', 'protocol_controlled_value_usd_lt', 'protocol_controlled_value_usd_gte', 'protocol_controlled_value_usd_lte', 'protocol_controlled_value_usd_in', 'protocol_controlled_value_usd_not_in', 'cumulative_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd_not', 'cumulative_supply_side_revenue_usd_gt', 'cumulative_supply_side_revenue_usd_lt', 'cumulative_supply_side_revenue_usd_gte', 'cumulative_supply_side_revenue_usd_lte', 'cumulative_supply_side_revenue_usd_in', 'cumulative_supply_side_revenue_usd_not_in', 'cumulative_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd_not', 'cumulative_protocol_side_revenue_usd_gt', 'cumulative_protocol_side_revenue_usd_lt', 'cumulative_protocol_side_revenue_usd_gte', 'cumulative_protocol_side_revenue_usd_lte', 'cumulative_protocol_side_revenue_usd_in', 'cumulative_protocol_side_revenue_usd_not_in', 'cumulative_total_revenue_usd', 'cumulative_total_revenue_usd_not', 'cumulative_total_revenue_usd_gt', 'cumulative_total_revenue_usd_lt', 'cumulative_total_revenue_usd_gte', 'cumulative_total_revenue_usd_lte', 'cumulative_total_revenue_usd_in', 'cumulative_total_revenue_usd_not_in', 'cumulative_unique_users', 'cumulative_unique_users_not', 'cumulative_unique_users_gt', 'cumulative_unique_users_lt', 'cumulative_unique_users_gte', 'cumulative_unique_users_lte', 'cumulative_unique_users_in', 'cumulative_unique_users_not_in', 'total_pool_count', 'total_pool_count_not', 'total_pool_count_gt', 'total_pool_count_lt', 'total_pool_count_gte', 'total_pool_count_lte', 'total_pool_count_in', 'total_pool_count_not_in', 'daily_usage_metrics_', 'hourly_usage_metrics_', 'financial_metrics_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
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
    slug = sgqlc.types.Field(String, graphql_name='slug')
    slug_not = sgqlc.types.Field(String, graphql_name='slug_not')
    slug_gt = sgqlc.types.Field(String, graphql_name='slug_gt')
    slug_lt = sgqlc.types.Field(String, graphql_name='slug_lt')
    slug_gte = sgqlc.types.Field(String, graphql_name='slug_gte')
    slug_lte = sgqlc.types.Field(String, graphql_name='slug_lte')
    slug_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='slug_in')
    slug_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='slug_not_in')
    slug_contains = sgqlc.types.Field(String, graphql_name='slug_contains')
    slug_contains_nocase = sgqlc.types.Field(String, graphql_name='slug_contains_nocase')
    slug_not_contains = sgqlc.types.Field(String, graphql_name='slug_not_contains')
    slug_not_contains_nocase = sgqlc.types.Field(String, graphql_name='slug_not_contains_nocase')
    slug_starts_with = sgqlc.types.Field(String, graphql_name='slug_starts_with')
    slug_starts_with_nocase = sgqlc.types.Field(String, graphql_name='slug_starts_with_nocase')
    slug_not_starts_with = sgqlc.types.Field(String, graphql_name='slug_not_starts_with')
    slug_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='slug_not_starts_with_nocase')
    slug_ends_with = sgqlc.types.Field(String, graphql_name='slug_ends_with')
    slug_ends_with_nocase = sgqlc.types.Field(String, graphql_name='slug_ends_with_nocase')
    slug_not_ends_with = sgqlc.types.Field(String, graphql_name='slug_not_ends_with')
    slug_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='slug_not_ends_with_nocase')
    schema_version = sgqlc.types.Field(String, graphql_name='schemaVersion')
    schema_version_not = sgqlc.types.Field(String, graphql_name='schemaVersion_not')
    schema_version_gt = sgqlc.types.Field(String, graphql_name='schemaVersion_gt')
    schema_version_lt = sgqlc.types.Field(String, graphql_name='schemaVersion_lt')
    schema_version_gte = sgqlc.types.Field(String, graphql_name='schemaVersion_gte')
    schema_version_lte = sgqlc.types.Field(String, graphql_name='schemaVersion_lte')
    schema_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='schemaVersion_in')
    schema_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='schemaVersion_not_in')
    schema_version_contains = sgqlc.types.Field(String, graphql_name='schemaVersion_contains')
    schema_version_contains_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_contains_nocase')
    schema_version_not_contains = sgqlc.types.Field(String, graphql_name='schemaVersion_not_contains')
    schema_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_contains_nocase')
    schema_version_starts_with = sgqlc.types.Field(String, graphql_name='schemaVersion_starts_with')
    schema_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_starts_with_nocase')
    schema_version_not_starts_with = sgqlc.types.Field(String, graphql_name='schemaVersion_not_starts_with')
    schema_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_starts_with_nocase')
    schema_version_ends_with = sgqlc.types.Field(String, graphql_name='schemaVersion_ends_with')
    schema_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_ends_with_nocase')
    schema_version_not_ends_with = sgqlc.types.Field(String, graphql_name='schemaVersion_not_ends_with')
    schema_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='schemaVersion_not_ends_with_nocase')
    subgraph_version = sgqlc.types.Field(String, graphql_name='subgraphVersion')
    subgraph_version_not = sgqlc.types.Field(String, graphql_name='subgraphVersion_not')
    subgraph_version_gt = sgqlc.types.Field(String, graphql_name='subgraphVersion_gt')
    subgraph_version_lt = sgqlc.types.Field(String, graphql_name='subgraphVersion_lt')
    subgraph_version_gte = sgqlc.types.Field(String, graphql_name='subgraphVersion_gte')
    subgraph_version_lte = sgqlc.types.Field(String, graphql_name='subgraphVersion_lte')
    subgraph_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subgraphVersion_in')
    subgraph_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='subgraphVersion_not_in')
    subgraph_version_contains = sgqlc.types.Field(String, graphql_name='subgraphVersion_contains')
    subgraph_version_contains_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_contains_nocase')
    subgraph_version_not_contains = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_contains')
    subgraph_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_contains_nocase')
    subgraph_version_starts_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_starts_with')
    subgraph_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_starts_with_nocase')
    subgraph_version_not_starts_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_starts_with')
    subgraph_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_starts_with_nocase')
    subgraph_version_ends_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_ends_with')
    subgraph_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_ends_with_nocase')
    subgraph_version_not_ends_with = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_ends_with')
    subgraph_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='subgraphVersion_not_ends_with_nocase')
    methodology_version = sgqlc.types.Field(String, graphql_name='methodologyVersion')
    methodology_version_not = sgqlc.types.Field(String, graphql_name='methodologyVersion_not')
    methodology_version_gt = sgqlc.types.Field(String, graphql_name='methodologyVersion_gt')
    methodology_version_lt = sgqlc.types.Field(String, graphql_name='methodologyVersion_lt')
    methodology_version_gte = sgqlc.types.Field(String, graphql_name='methodologyVersion_gte')
    methodology_version_lte = sgqlc.types.Field(String, graphql_name='methodologyVersion_lte')
    methodology_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='methodologyVersion_in')
    methodology_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='methodologyVersion_not_in')
    methodology_version_contains = sgqlc.types.Field(String, graphql_name='methodologyVersion_contains')
    methodology_version_contains_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_contains_nocase')
    methodology_version_not_contains = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_contains')
    methodology_version_not_contains_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_contains_nocase')
    methodology_version_starts_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_starts_with')
    methodology_version_starts_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_starts_with_nocase')
    methodology_version_not_starts_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_starts_with')
    methodology_version_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_starts_with_nocase')
    methodology_version_ends_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_ends_with')
    methodology_version_ends_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_ends_with_nocase')
    methodology_version_not_ends_with = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_ends_with')
    methodology_version_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='methodologyVersion_not_ends_with_nocase')
    network = sgqlc.types.Field(Network, graphql_name='network')
    network_not = sgqlc.types.Field(Network, graphql_name='network_not')
    network_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Network)), graphql_name='network_in')
    network_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Network)), graphql_name='network_not_in')
    type = sgqlc.types.Field(ProtocolType, graphql_name='type')
    type_not = sgqlc.types.Field(ProtocolType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolType)), graphql_name='type_not_in')
    total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD')
    total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_not')
    total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gt')
    total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lt')
    total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_gte')
    total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalValueLockedUSD_lte')
    total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_in')
    total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalValueLockedUSD_not_in')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    protocol_controlled_value_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_not')
    protocol_controlled_value_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gt')
    protocol_controlled_value_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lt')
    protocol_controlled_value_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_gte')
    protocol_controlled_value_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD_lte')
    protocol_controlled_value_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_in')
    protocol_controlled_value_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolControlledValueUSD_not_in')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_not')
    cumulative_supply_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gt')
    cumulative_supply_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lt')
    cumulative_supply_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_gte')
    cumulative_supply_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeSupplySideRevenueUSD_lte')
    cumulative_supply_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_in')
    cumulative_supply_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeSupplySideRevenueUSD_not_in')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_not')
    cumulative_protocol_side_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gt')
    cumulative_protocol_side_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lt')
    cumulative_protocol_side_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_gte')
    cumulative_protocol_side_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeProtocolSideRevenueUSD_lte')
    cumulative_protocol_side_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_in')
    cumulative_protocol_side_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeProtocolSideRevenueUSD_not_in')
    cumulative_total_revenue_usd = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD')
    cumulative_total_revenue_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_not')
    cumulative_total_revenue_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gt')
    cumulative_total_revenue_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lt')
    cumulative_total_revenue_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_gte')
    cumulative_total_revenue_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='cumulativeTotalRevenueUSD_lte')
    cumulative_total_revenue_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_in')
    cumulative_total_revenue_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cumulativeTotalRevenueUSD_not_in')
    cumulative_unique_users = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers')
    cumulative_unique_users_not = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_not')
    cumulative_unique_users_gt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gt')
    cumulative_unique_users_lt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lt')
    cumulative_unique_users_gte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gte')
    cumulative_unique_users_lte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lte')
    cumulative_unique_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_in')
    cumulative_unique_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_not_in')
    total_pool_count = sgqlc.types.Field(Int, graphql_name='totalPoolCount')
    total_pool_count_not = sgqlc.types.Field(Int, graphql_name='totalPoolCount_not')
    total_pool_count_gt = sgqlc.types.Field(Int, graphql_name='totalPoolCount_gt')
    total_pool_count_lt = sgqlc.types.Field(Int, graphql_name='totalPoolCount_lt')
    total_pool_count_gte = sgqlc.types.Field(Int, graphql_name='totalPoolCount_gte')
    total_pool_count_lte = sgqlc.types.Field(Int, graphql_name='totalPoolCount_lte')
    total_pool_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='totalPoolCount_in')
    total_pool_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='totalPoolCount_not_in')
    daily_usage_metrics_ = sgqlc.types.Field('UsageMetricsDailySnapshot_filter', graphql_name='dailyUsageMetrics_')
    hourly_usage_metrics_ = sgqlc.types.Field('UsageMetricsHourlySnapshot_filter', graphql_name='hourlyUsageMetrics_')
    financial_metrics_ = sgqlc.types.Field(FinancialsDailySnapshot_filter, graphql_name='financialMetrics_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Protocol_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Protocol_filter'), graphql_name='or')


class RewardToken_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'token_', 'type', 'type_not', 'type_in', 'type_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
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
    type = sgqlc.types.Field(RewardTokenType, graphql_name='type')
    type_not = sgqlc.types.Field(RewardTokenType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RewardTokenType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RewardTokenType)), graphql_name='type_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('RewardToken_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('RewardToken_filter'), graphql_name='or')


class Swap_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'token_in', 'token_in_not', 'token_in_gt', 'token_in_lt', 'token_in_gte', 'token_in_lte', 'token_in_in', 'token_in_not_in', 'token_in_contains', 'token_in_contains_nocase', 'token_in_not_contains', 'token_in_not_contains_nocase', 'token_in_starts_with', 'token_in_starts_with_nocase', 'token_in_not_starts_with', 'token_in_not_starts_with_nocase', 'token_in_ends_with', 'token_in_ends_with_nocase', 'token_in_not_ends_with', 'token_in_not_ends_with_nocase', 'token_in_', 'amount_in', 'amount_in_not', 'amount_in_gt', 'amount_in_lt', 'amount_in_gte', 'amount_in_lte', 'amount_in_in', 'amount_in_not_in', 'amount_in_usd', 'amount_in_usd_not', 'amount_in_usd_gt', 'amount_in_usd_lt', 'amount_in_usd_gte', 'amount_in_usd_lte', 'amount_in_usd_in', 'amount_in_usd_not_in', 'token_out', 'token_out_not', 'token_out_gt', 'token_out_lt', 'token_out_gte', 'token_out_lte', 'token_out_in', 'token_out_not_in', 'token_out_contains', 'token_out_contains_nocase', 'token_out_not_contains', 'token_out_not_contains_nocase', 'token_out_starts_with', 'token_out_starts_with_nocase', 'token_out_not_starts_with', 'token_out_not_starts_with_nocase', 'token_out_ends_with', 'token_out_ends_with_nocase', 'token_out_not_ends_with', 'token_out_not_ends_with_nocase', 'token_out_', 'amount_out', 'amount_out_not', 'amount_out_gt', 'amount_out_lt', 'amount_out_gte', 'amount_out_lte', 'amount_out_in', 'amount_out_not_in', 'amount_out_usd', 'amount_out_usd_not', 'amount_out_usd_gt', 'amount_out_usd_lt', 'amount_out_usd_gte', 'amount_out_usd_lte', 'amount_out_usd_in', 'amount_out_usd_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field(DexAmmProtocol_filter, graphql_name='protocol_')
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
    token_in = sgqlc.types.Field(String, graphql_name='tokenIn')
    token_in_not = sgqlc.types.Field(String, graphql_name='tokenIn_not')
    token_in_gt = sgqlc.types.Field(String, graphql_name='tokenIn_gt')
    token_in_lt = sgqlc.types.Field(String, graphql_name='tokenIn_lt')
    token_in_gte = sgqlc.types.Field(String, graphql_name='tokenIn_gte')
    token_in_lte = sgqlc.types.Field(String, graphql_name='tokenIn_lte')
    token_in_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenIn_in')
    token_in_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenIn_not_in')
    token_in_contains = sgqlc.types.Field(String, graphql_name='tokenIn_contains')
    token_in_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenIn_contains_nocase')
    token_in_not_contains = sgqlc.types.Field(String, graphql_name='tokenIn_not_contains')
    token_in_not_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenIn_not_contains_nocase')
    token_in_starts_with = sgqlc.types.Field(String, graphql_name='tokenIn_starts_with')
    token_in_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenIn_starts_with_nocase')
    token_in_not_starts_with = sgqlc.types.Field(String, graphql_name='tokenIn_not_starts_with')
    token_in_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenIn_not_starts_with_nocase')
    token_in_ends_with = sgqlc.types.Field(String, graphql_name='tokenIn_ends_with')
    token_in_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenIn_ends_with_nocase')
    token_in_not_ends_with = sgqlc.types.Field(String, graphql_name='tokenIn_not_ends_with')
    token_in_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenIn_not_ends_with_nocase')
    token_in_ = sgqlc.types.Field('Token_filter', graphql_name='tokenIn_')
    amount_in = sgqlc.types.Field(BigInt, graphql_name='amountIn')
    amount_in_not = sgqlc.types.Field(BigInt, graphql_name='amountIn_not')
    amount_in_gt = sgqlc.types.Field(BigInt, graphql_name='amountIn_gt')
    amount_in_lt = sgqlc.types.Field(BigInt, graphql_name='amountIn_lt')
    amount_in_gte = sgqlc.types.Field(BigInt, graphql_name='amountIn_gte')
    amount_in_lte = sgqlc.types.Field(BigInt, graphql_name='amountIn_lte')
    amount_in_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amountIn_in')
    amount_in_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amountIn_not_in')
    amount_in_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountInUSD')
    amount_in_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountInUSD_not')
    amount_in_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountInUSD_gt')
    amount_in_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountInUSD_lt')
    amount_in_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountInUSD_gte')
    amount_in_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountInUSD_lte')
    amount_in_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountInUSD_in')
    amount_in_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountInUSD_not_in')
    token_out = sgqlc.types.Field(String, graphql_name='tokenOut')
    token_out_not = sgqlc.types.Field(String, graphql_name='tokenOut_not')
    token_out_gt = sgqlc.types.Field(String, graphql_name='tokenOut_gt')
    token_out_lt = sgqlc.types.Field(String, graphql_name='tokenOut_lt')
    token_out_gte = sgqlc.types.Field(String, graphql_name='tokenOut_gte')
    token_out_lte = sgqlc.types.Field(String, graphql_name='tokenOut_lte')
    token_out_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenOut_in')
    token_out_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenOut_not_in')
    token_out_contains = sgqlc.types.Field(String, graphql_name='tokenOut_contains')
    token_out_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenOut_contains_nocase')
    token_out_not_contains = sgqlc.types.Field(String, graphql_name='tokenOut_not_contains')
    token_out_not_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenOut_not_contains_nocase')
    token_out_starts_with = sgqlc.types.Field(String, graphql_name='tokenOut_starts_with')
    token_out_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenOut_starts_with_nocase')
    token_out_not_starts_with = sgqlc.types.Field(String, graphql_name='tokenOut_not_starts_with')
    token_out_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenOut_not_starts_with_nocase')
    token_out_ends_with = sgqlc.types.Field(String, graphql_name='tokenOut_ends_with')
    token_out_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenOut_ends_with_nocase')
    token_out_not_ends_with = sgqlc.types.Field(String, graphql_name='tokenOut_not_ends_with')
    token_out_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenOut_not_ends_with_nocase')
    token_out_ = sgqlc.types.Field('Token_filter', graphql_name='tokenOut_')
    amount_out = sgqlc.types.Field(BigInt, graphql_name='amountOut')
    amount_out_not = sgqlc.types.Field(BigInt, graphql_name='amountOut_not')
    amount_out_gt = sgqlc.types.Field(BigInt, graphql_name='amountOut_gt')
    amount_out_lt = sgqlc.types.Field(BigInt, graphql_name='amountOut_lt')
    amount_out_gte = sgqlc.types.Field(BigInt, graphql_name='amountOut_gte')
    amount_out_lte = sgqlc.types.Field(BigInt, graphql_name='amountOut_lte')
    amount_out_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amountOut_in')
    amount_out_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amountOut_not_in')
    amount_out_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountOutUSD')
    amount_out_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountOutUSD_not')
    amount_out_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountOutUSD_gt')
    amount_out_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountOutUSD_lt')
    amount_out_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountOutUSD_gte')
    amount_out_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountOutUSD_lte')
    amount_out_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountOutUSD_in')
    amount_out_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountOutUSD_not_in')
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
    pool_ = sgqlc.types.Field(LiquidityPool_filter, graphql_name='pool_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Swap_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Swap_filter'), graphql_name='or')


class Token_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_contains_nocase', 'symbol_not_contains', 'symbol_not_contains_nocase', 'symbol_starts_with', 'symbol_starts_with_nocase', 'symbol_not_starts_with', 'symbol_not_starts_with_nocase', 'symbol_ends_with', 'symbol_ends_with_nocase', 'symbol_not_ends_with', 'symbol_not_ends_with_nocase', 'decimals', 'decimals_not', 'decimals_gt', 'decimals_lt', 'decimals_gte', 'decimals_lte', 'decimals_in', 'decimals_not_in', 'is_base_pool_lp_token', 'is_base_pool_lp_token_not', 'is_base_pool_lp_token_in', 'is_base_pool_lp_token_not_in', 'last_price_usd', 'last_price_usd_not', 'last_price_usd_gt', 'last_price_usd_lt', 'last_price_usd_gte', 'last_price_usd_lte', 'last_price_usd_in', 'last_price_usd_not_in', 'last_price_block_number', 'last_price_block_number_not', 'last_price_block_number_gt', 'last_price_block_number_lt', 'last_price_block_number_gte', 'last_price_block_number_lte', 'last_price_block_number_in', 'last_price_block_number_not_in', 'oracle_type', 'oracle_type_not', 'oracle_type_gt', 'oracle_type_lt', 'oracle_type_gte', 'oracle_type_lte', 'oracle_type_in', 'oracle_type_not_in', 'oracle_type_contains', 'oracle_type_contains_nocase', 'oracle_type_not_contains', 'oracle_type_not_contains_nocase', 'oracle_type_starts_with', 'oracle_type_starts_with_nocase', 'oracle_type_not_starts_with', 'oracle_type_not_starts_with_nocase', 'oracle_type_ends_with', 'oracle_type_ends_with_nocase', 'oracle_type_not_ends_with', 'oracle_type_not_ends_with_nocase', '_total_supply', '_total_supply_not', '_total_supply_gt', '_total_supply_lt', '_total_supply_gte', '_total_supply_lte', '_total_supply_in', '_total_supply_not_in', '_total_value_locked_usd', '_total_value_locked_usd_not', '_total_value_locked_usd_gt', '_total_value_locked_usd_lt', '_total_value_locked_usd_gte', '_total_value_locked_usd_lte', '_total_value_locked_usd_in', '_total_value_locked_usd_not_in', '_large_price_change_buffer', '_large_price_change_buffer_not', '_large_price_change_buffer_gt', '_large_price_change_buffer_lt', '_large_price_change_buffer_gte', '_large_price_change_buffer_lte', '_large_price_change_buffer_in', '_large_price_change_buffer_not_in', '_large_tvlimpact_buffer', '_large_tvlimpact_buffer_not', '_large_tvlimpact_buffer_gt', '_large_tvlimpact_buffer_lt', '_large_tvlimpact_buffer_gte', '_large_tvlimpact_buffer_lte', '_large_tvlimpact_buffer_in', '_large_tvlimpact_buffer_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
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
    decimals = sgqlc.types.Field(Int, graphql_name='decimals')
    decimals_not = sgqlc.types.Field(Int, graphql_name='decimals_not')
    decimals_gt = sgqlc.types.Field(Int, graphql_name='decimals_gt')
    decimals_lt = sgqlc.types.Field(Int, graphql_name='decimals_lt')
    decimals_gte = sgqlc.types.Field(Int, graphql_name='decimals_gte')
    decimals_lte = sgqlc.types.Field(Int, graphql_name='decimals_lte')
    decimals_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='decimals_in')
    decimals_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='decimals_not_in')
    is_base_pool_lp_token = sgqlc.types.Field(Boolean, graphql_name='isBasePoolLpToken')
    is_base_pool_lp_token_not = sgqlc.types.Field(Boolean, graphql_name='isBasePoolLpToken_not')
    is_base_pool_lp_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isBasePoolLpToken_in')
    is_base_pool_lp_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isBasePoolLpToken_not_in')
    last_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD')
    last_price_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_not')
    last_price_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_gt')
    last_price_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_lt')
    last_price_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_gte')
    last_price_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD_lte')
    last_price_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lastPriceUSD_in')
    last_price_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lastPriceUSD_not_in')
    last_price_block_number = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber')
    last_price_block_number_not = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_not')
    last_price_block_number_gt = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_gt')
    last_price_block_number_lt = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_lt')
    last_price_block_number_gte = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_gte')
    last_price_block_number_lte = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber_lte')
    last_price_block_number_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='lastPriceBlockNumber_in')
    last_price_block_number_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='lastPriceBlockNumber_not_in')
    oracle_type = sgqlc.types.Field(String, graphql_name='oracleType')
    oracle_type_not = sgqlc.types.Field(String, graphql_name='oracleType_not')
    oracle_type_gt = sgqlc.types.Field(String, graphql_name='oracleType_gt')
    oracle_type_lt = sgqlc.types.Field(String, graphql_name='oracleType_lt')
    oracle_type_gte = sgqlc.types.Field(String, graphql_name='oracleType_gte')
    oracle_type_lte = sgqlc.types.Field(String, graphql_name='oracleType_lte')
    oracle_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='oracleType_in')
    oracle_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='oracleType_not_in')
    oracle_type_contains = sgqlc.types.Field(String, graphql_name='oracleType_contains')
    oracle_type_contains_nocase = sgqlc.types.Field(String, graphql_name='oracleType_contains_nocase')
    oracle_type_not_contains = sgqlc.types.Field(String, graphql_name='oracleType_not_contains')
    oracle_type_not_contains_nocase = sgqlc.types.Field(String, graphql_name='oracleType_not_contains_nocase')
    oracle_type_starts_with = sgqlc.types.Field(String, graphql_name='oracleType_starts_with')
    oracle_type_starts_with_nocase = sgqlc.types.Field(String, graphql_name='oracleType_starts_with_nocase')
    oracle_type_not_starts_with = sgqlc.types.Field(String, graphql_name='oracleType_not_starts_with')
    oracle_type_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='oracleType_not_starts_with_nocase')
    oracle_type_ends_with = sgqlc.types.Field(String, graphql_name='oracleType_ends_with')
    oracle_type_ends_with_nocase = sgqlc.types.Field(String, graphql_name='oracleType_ends_with_nocase')
    oracle_type_not_ends_with = sgqlc.types.Field(String, graphql_name='oracleType_not_ends_with')
    oracle_type_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='oracleType_not_ends_with_nocase')
    _total_supply = sgqlc.types.Field(BigInt, graphql_name='_totalSupply')
    _total_supply_not = sgqlc.types.Field(BigInt, graphql_name='_totalSupply_not')
    _total_supply_gt = sgqlc.types.Field(BigInt, graphql_name='_totalSupply_gt')
    _total_supply_lt = sgqlc.types.Field(BigInt, graphql_name='_totalSupply_lt')
    _total_supply_gte = sgqlc.types.Field(BigInt, graphql_name='_totalSupply_gte')
    _total_supply_lte = sgqlc.types.Field(BigInt, graphql_name='_totalSupply_lte')
    _total_supply_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='_totalSupply_in')
    _total_supply_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='_totalSupply_not_in')
    _total_value_locked_usd = sgqlc.types.Field(BigDecimal, graphql_name='_totalValueLockedUSD')
    _total_value_locked_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='_totalValueLockedUSD_not')
    _total_value_locked_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='_totalValueLockedUSD_gt')
    _total_value_locked_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='_totalValueLockedUSD_lt')
    _total_value_locked_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='_totalValueLockedUSD_gte')
    _total_value_locked_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='_totalValueLockedUSD_lte')
    _total_value_locked_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='_totalValueLockedUSD_in')
    _total_value_locked_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='_totalValueLockedUSD_not_in')
    _large_price_change_buffer = sgqlc.types.Field(Int, graphql_name='_largePriceChangeBuffer')
    _large_price_change_buffer_not = sgqlc.types.Field(Int, graphql_name='_largePriceChangeBuffer_not')
    _large_price_change_buffer_gt = sgqlc.types.Field(Int, graphql_name='_largePriceChangeBuffer_gt')
    _large_price_change_buffer_lt = sgqlc.types.Field(Int, graphql_name='_largePriceChangeBuffer_lt')
    _large_price_change_buffer_gte = sgqlc.types.Field(Int, graphql_name='_largePriceChangeBuffer_gte')
    _large_price_change_buffer_lte = sgqlc.types.Field(Int, graphql_name='_largePriceChangeBuffer_lte')
    _large_price_change_buffer_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='_largePriceChangeBuffer_in')
    _large_price_change_buffer_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='_largePriceChangeBuffer_not_in')
    _large_tvlimpact_buffer = sgqlc.types.Field(Int, graphql_name='_largeTVLImpactBuffer')
    _large_tvlimpact_buffer_not = sgqlc.types.Field(Int, graphql_name='_largeTVLImpactBuffer_not')
    _large_tvlimpact_buffer_gt = sgqlc.types.Field(Int, graphql_name='_largeTVLImpactBuffer_gt')
    _large_tvlimpact_buffer_lt = sgqlc.types.Field(Int, graphql_name='_largeTVLImpactBuffer_lt')
    _large_tvlimpact_buffer_gte = sgqlc.types.Field(Int, graphql_name='_largeTVLImpactBuffer_gte')
    _large_tvlimpact_buffer_lte = sgqlc.types.Field(Int, graphql_name='_largeTVLImpactBuffer_lte')
    _large_tvlimpact_buffer_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='_largeTVLImpactBuffer_in')
    _large_tvlimpact_buffer_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='_largeTVLImpactBuffer_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Token_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Token_filter'), graphql_name='or')


class UsageMetricsDailySnapshot_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'daily_active_users', 'daily_active_users_not', 'daily_active_users_gt', 'daily_active_users_lt', 'daily_active_users_gte', 'daily_active_users_lte', 'daily_active_users_in', 'daily_active_users_not_in', 'cumulative_unique_users', 'cumulative_unique_users_not', 'cumulative_unique_users_gt', 'cumulative_unique_users_lt', 'cumulative_unique_users_gte', 'cumulative_unique_users_lte', 'cumulative_unique_users_in', 'cumulative_unique_users_not_in', 'daily_transaction_count', 'daily_transaction_count_not', 'daily_transaction_count_gt', 'daily_transaction_count_lt', 'daily_transaction_count_gte', 'daily_transaction_count_lte', 'daily_transaction_count_in', 'daily_transaction_count_not_in', 'daily_deposit_count', 'daily_deposit_count_not', 'daily_deposit_count_gt', 'daily_deposit_count_lt', 'daily_deposit_count_gte', 'daily_deposit_count_lte', 'daily_deposit_count_in', 'daily_deposit_count_not_in', 'daily_withdraw_count', 'daily_withdraw_count_not', 'daily_withdraw_count_gt', 'daily_withdraw_count_lt', 'daily_withdraw_count_gte', 'daily_withdraw_count_lte', 'daily_withdraw_count_in', 'daily_withdraw_count_not_in', 'daily_swap_count', 'daily_swap_count_not', 'daily_swap_count_gt', 'daily_swap_count_lt', 'daily_swap_count_gte', 'daily_swap_count_lte', 'daily_swap_count_in', 'daily_swap_count_not_in', 'total_pool_count', 'total_pool_count_not', 'total_pool_count_gt', 'total_pool_count_lt', 'total_pool_count_gte', 'total_pool_count_lte', 'total_pool_count_in', 'total_pool_count_not_in', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field(DexAmmProtocol_filter, graphql_name='protocol_')
    daily_active_users = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers')
    daily_active_users_not = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_not')
    daily_active_users_gt = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_gt')
    daily_active_users_lt = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_lt')
    daily_active_users_gte = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_gte')
    daily_active_users_lte = sgqlc.types.Field(Int, graphql_name='dailyActiveUsers_lte')
    daily_active_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyActiveUsers_in')
    daily_active_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyActiveUsers_not_in')
    cumulative_unique_users = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers')
    cumulative_unique_users_not = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_not')
    cumulative_unique_users_gt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gt')
    cumulative_unique_users_lt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lt')
    cumulative_unique_users_gte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gte')
    cumulative_unique_users_lte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lte')
    cumulative_unique_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_in')
    cumulative_unique_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_not_in')
    daily_transaction_count = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount')
    daily_transaction_count_not = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_not')
    daily_transaction_count_gt = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_gt')
    daily_transaction_count_lt = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_lt')
    daily_transaction_count_gte = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_gte')
    daily_transaction_count_lte = sgqlc.types.Field(Int, graphql_name='dailyTransactionCount_lte')
    daily_transaction_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyTransactionCount_in')
    daily_transaction_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyTransactionCount_not_in')
    daily_deposit_count = sgqlc.types.Field(Int, graphql_name='dailyDepositCount')
    daily_deposit_count_not = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_not')
    daily_deposit_count_gt = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_gt')
    daily_deposit_count_lt = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_lt')
    daily_deposit_count_gte = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_gte')
    daily_deposit_count_lte = sgqlc.types.Field(Int, graphql_name='dailyDepositCount_lte')
    daily_deposit_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyDepositCount_in')
    daily_deposit_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyDepositCount_not_in')
    daily_withdraw_count = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount')
    daily_withdraw_count_not = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_not')
    daily_withdraw_count_gt = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_gt')
    daily_withdraw_count_lt = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_lt')
    daily_withdraw_count_gte = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_gte')
    daily_withdraw_count_lte = sgqlc.types.Field(Int, graphql_name='dailyWithdrawCount_lte')
    daily_withdraw_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyWithdrawCount_in')
    daily_withdraw_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailyWithdrawCount_not_in')
    daily_swap_count = sgqlc.types.Field(Int, graphql_name='dailySwapCount')
    daily_swap_count_not = sgqlc.types.Field(Int, graphql_name='dailySwapCount_not')
    daily_swap_count_gt = sgqlc.types.Field(Int, graphql_name='dailySwapCount_gt')
    daily_swap_count_lt = sgqlc.types.Field(Int, graphql_name='dailySwapCount_lt')
    daily_swap_count_gte = sgqlc.types.Field(Int, graphql_name='dailySwapCount_gte')
    daily_swap_count_lte = sgqlc.types.Field(Int, graphql_name='dailySwapCount_lte')
    daily_swap_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailySwapCount_in')
    daily_swap_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dailySwapCount_not_in')
    total_pool_count = sgqlc.types.Field(Int, graphql_name='totalPoolCount')
    total_pool_count_not = sgqlc.types.Field(Int, graphql_name='totalPoolCount_not')
    total_pool_count_gt = sgqlc.types.Field(Int, graphql_name='totalPoolCount_gt')
    total_pool_count_lt = sgqlc.types.Field(Int, graphql_name='totalPoolCount_lt')
    total_pool_count_gte = sgqlc.types.Field(Int, graphql_name='totalPoolCount_gte')
    total_pool_count_lte = sgqlc.types.Field(Int, graphql_name='totalPoolCount_lte')
    total_pool_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='totalPoolCount_in')
    total_pool_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='totalPoolCount_not_in')
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
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('UsageMetricsDailySnapshot_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('UsageMetricsDailySnapshot_filter'), graphql_name='or')


class UsageMetricsHourlySnapshot_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'hourly_active_users', 'hourly_active_users_not', 'hourly_active_users_gt', 'hourly_active_users_lt', 'hourly_active_users_gte', 'hourly_active_users_lte', 'hourly_active_users_in', 'hourly_active_users_not_in', 'cumulative_unique_users', 'cumulative_unique_users_not', 'cumulative_unique_users_gt', 'cumulative_unique_users_lt', 'cumulative_unique_users_gte', 'cumulative_unique_users_lte', 'cumulative_unique_users_in', 'cumulative_unique_users_not_in', 'hourly_transaction_count', 'hourly_transaction_count_not', 'hourly_transaction_count_gt', 'hourly_transaction_count_lt', 'hourly_transaction_count_gte', 'hourly_transaction_count_lte', 'hourly_transaction_count_in', 'hourly_transaction_count_not_in', 'hourly_deposit_count', 'hourly_deposit_count_not', 'hourly_deposit_count_gt', 'hourly_deposit_count_lt', 'hourly_deposit_count_gte', 'hourly_deposit_count_lte', 'hourly_deposit_count_in', 'hourly_deposit_count_not_in', 'hourly_withdraw_count', 'hourly_withdraw_count_not', 'hourly_withdraw_count_gt', 'hourly_withdraw_count_lt', 'hourly_withdraw_count_gte', 'hourly_withdraw_count_lte', 'hourly_withdraw_count_in', 'hourly_withdraw_count_not_in', 'hourly_swap_count', 'hourly_swap_count_not', 'hourly_swap_count_gt', 'hourly_swap_count_lt', 'hourly_swap_count_gte', 'hourly_swap_count_lte', 'hourly_swap_count_in', 'hourly_swap_count_not_in', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field(DexAmmProtocol_filter, graphql_name='protocol_')
    hourly_active_users = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers')
    hourly_active_users_not = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_not')
    hourly_active_users_gt = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_gt')
    hourly_active_users_lt = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_lt')
    hourly_active_users_gte = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_gte')
    hourly_active_users_lte = sgqlc.types.Field(Int, graphql_name='hourlyActiveUsers_lte')
    hourly_active_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyActiveUsers_in')
    hourly_active_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyActiveUsers_not_in')
    cumulative_unique_users = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers')
    cumulative_unique_users_not = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_not')
    cumulative_unique_users_gt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gt')
    cumulative_unique_users_lt = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lt')
    cumulative_unique_users_gte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_gte')
    cumulative_unique_users_lte = sgqlc.types.Field(Int, graphql_name='cumulativeUniqueUsers_lte')
    cumulative_unique_users_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_in')
    cumulative_unique_users_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cumulativeUniqueUsers_not_in')
    hourly_transaction_count = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount')
    hourly_transaction_count_not = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_not')
    hourly_transaction_count_gt = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_gt')
    hourly_transaction_count_lt = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_lt')
    hourly_transaction_count_gte = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_gte')
    hourly_transaction_count_lte = sgqlc.types.Field(Int, graphql_name='hourlyTransactionCount_lte')
    hourly_transaction_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyTransactionCount_in')
    hourly_transaction_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyTransactionCount_not_in')
    hourly_deposit_count = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount')
    hourly_deposit_count_not = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_not')
    hourly_deposit_count_gt = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_gt')
    hourly_deposit_count_lt = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_lt')
    hourly_deposit_count_gte = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_gte')
    hourly_deposit_count_lte = sgqlc.types.Field(Int, graphql_name='hourlyDepositCount_lte')
    hourly_deposit_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyDepositCount_in')
    hourly_deposit_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyDepositCount_not_in')
    hourly_withdraw_count = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount')
    hourly_withdraw_count_not = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_not')
    hourly_withdraw_count_gt = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_gt')
    hourly_withdraw_count_lt = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_lt')
    hourly_withdraw_count_gte = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_gte')
    hourly_withdraw_count_lte = sgqlc.types.Field(Int, graphql_name='hourlyWithdrawCount_lte')
    hourly_withdraw_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyWithdrawCount_in')
    hourly_withdraw_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlyWithdrawCount_not_in')
    hourly_swap_count = sgqlc.types.Field(Int, graphql_name='hourlySwapCount')
    hourly_swap_count_not = sgqlc.types.Field(Int, graphql_name='hourlySwapCount_not')
    hourly_swap_count_gt = sgqlc.types.Field(Int, graphql_name='hourlySwapCount_gt')
    hourly_swap_count_lt = sgqlc.types.Field(Int, graphql_name='hourlySwapCount_lt')
    hourly_swap_count_gte = sgqlc.types.Field(Int, graphql_name='hourlySwapCount_gte')
    hourly_swap_count_lte = sgqlc.types.Field(Int, graphql_name='hourlySwapCount_lte')
    hourly_swap_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlySwapCount_in')
    hourly_swap_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='hourlySwapCount_not_in')
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
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('UsageMetricsHourlySnapshot_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('UsageMetricsHourlySnapshot_filter'), graphql_name='or')


class Withdraw_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'hash', 'hash_not', 'hash_gt', 'hash_lt', 'hash_gte', 'hash_lte', 'hash_in', 'hash_not_in', 'hash_contains', 'hash_contains_nocase', 'hash_not_contains', 'hash_not_contains_nocase', 'hash_starts_with', 'hash_starts_with_nocase', 'hash_not_starts_with', 'hash_not_starts_with_nocase', 'hash_ends_with', 'hash_ends_with_nocase', 'hash_not_ends_with', 'hash_not_ends_with_nocase', 'log_index', 'log_index_not', 'log_index_gt', 'log_index_lt', 'log_index_gte', 'log_index_lte', 'log_index_in', 'log_index_not_in', 'protocol', 'protocol_not', 'protocol_gt', 'protocol_lt', 'protocol_gte', 'protocol_lte', 'protocol_in', 'protocol_not_in', 'protocol_contains', 'protocol_contains_nocase', 'protocol_not_contains', 'protocol_not_contains_nocase', 'protocol_starts_with', 'protocol_starts_with_nocase', 'protocol_not_starts_with', 'protocol_not_starts_with_nocase', 'protocol_ends_with', 'protocol_ends_with_nocase', 'protocol_not_ends_with', 'protocol_not_ends_with_nocase', 'protocol_', 'to', 'to_not', 'to_gt', 'to_lt', 'to_gte', 'to_lte', 'to_in', 'to_not_in', 'to_contains', 'to_contains_nocase', 'to_not_contains', 'to_not_contains_nocase', 'to_starts_with', 'to_starts_with_nocase', 'to_not_starts_with', 'to_not_starts_with_nocase', 'to_ends_with', 'to_ends_with_nocase', 'to_not_ends_with', 'to_not_ends_with_nocase', 'from_', 'from_not', 'from_gt', 'from_lt', 'from_gte', 'from_lte', 'from_in', 'from_not_in', 'from_contains', 'from_contains_nocase', 'from_not_contains', 'from_not_contains_nocase', 'from_starts_with', 'from_starts_with_nocase', 'from_not_starts_with', 'from_not_starts_with_nocase', 'from_ends_with', 'from_ends_with_nocase', 'from_not_ends_with', 'from_not_ends_with_nocase', 'block_number', 'block_number_not', 'block_number_gt', 'block_number_lt', 'block_number_gte', 'block_number_lte', 'block_number_in', 'block_number_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'input_tokens', 'input_tokens_not', 'input_tokens_contains', 'input_tokens_contains_nocase', 'input_tokens_not_contains', 'input_tokens_not_contains_nocase', 'input_tokens_', 'output_token', 'output_token_not', 'output_token_gt', 'output_token_lt', 'output_token_gte', 'output_token_lte', 'output_token_in', 'output_token_not_in', 'output_token_contains', 'output_token_contains_nocase', 'output_token_not_contains', 'output_token_not_contains_nocase', 'output_token_starts_with', 'output_token_starts_with_nocase', 'output_token_not_starts_with', 'output_token_not_starts_with_nocase', 'output_token_ends_with', 'output_token_ends_with_nocase', 'output_token_not_ends_with', 'output_token_not_ends_with_nocase', 'output_token_', 'input_token_amounts', 'input_token_amounts_not', 'input_token_amounts_contains', 'input_token_amounts_contains_nocase', 'input_token_amounts_not_contains', 'input_token_amounts_not_contains_nocase', 'output_token_amount', 'output_token_amount_not', 'output_token_amount_gt', 'output_token_amount_lt', 'output_token_amount_gte', 'output_token_amount_lte', 'output_token_amount_in', 'output_token_amount_not_in', 'amount_usd', 'amount_usd_not', 'amount_usd_gt', 'amount_usd_lt', 'amount_usd_gte', 'amount_usd_lte', 'amount_usd_in', 'amount_usd_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    hash = sgqlc.types.Field(String, graphql_name='hash')
    hash_not = sgqlc.types.Field(String, graphql_name='hash_not')
    hash_gt = sgqlc.types.Field(String, graphql_name='hash_gt')
    hash_lt = sgqlc.types.Field(String, graphql_name='hash_lt')
    hash_gte = sgqlc.types.Field(String, graphql_name='hash_gte')
    hash_lte = sgqlc.types.Field(String, graphql_name='hash_lte')
    hash_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_in')
    hash_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hash_not_in')
    hash_contains = sgqlc.types.Field(String, graphql_name='hash_contains')
    hash_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_contains_nocase')
    hash_not_contains = sgqlc.types.Field(String, graphql_name='hash_not_contains')
    hash_not_contains_nocase = sgqlc.types.Field(String, graphql_name='hash_not_contains_nocase')
    hash_starts_with = sgqlc.types.Field(String, graphql_name='hash_starts_with')
    hash_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_starts_with_nocase')
    hash_not_starts_with = sgqlc.types.Field(String, graphql_name='hash_not_starts_with')
    hash_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_starts_with_nocase')
    hash_ends_with = sgqlc.types.Field(String, graphql_name='hash_ends_with')
    hash_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_ends_with_nocase')
    hash_not_ends_with = sgqlc.types.Field(String, graphql_name='hash_not_ends_with')
    hash_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='hash_not_ends_with_nocase')
    log_index = sgqlc.types.Field(Int, graphql_name='logIndex')
    log_index_not = sgqlc.types.Field(Int, graphql_name='logIndex_not')
    log_index_gt = sgqlc.types.Field(Int, graphql_name='logIndex_gt')
    log_index_lt = sgqlc.types.Field(Int, graphql_name='logIndex_lt')
    log_index_gte = sgqlc.types.Field(Int, graphql_name='logIndex_gte')
    log_index_lte = sgqlc.types.Field(Int, graphql_name='logIndex_lte')
    log_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_in')
    log_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='logIndex_not_in')
    protocol = sgqlc.types.Field(String, graphql_name='protocol')
    protocol_not = sgqlc.types.Field(String, graphql_name='protocol_not')
    protocol_gt = sgqlc.types.Field(String, graphql_name='protocol_gt')
    protocol_lt = sgqlc.types.Field(String, graphql_name='protocol_lt')
    protocol_gte = sgqlc.types.Field(String, graphql_name='protocol_gte')
    protocol_lte = sgqlc.types.Field(String, graphql_name='protocol_lte')
    protocol_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_in')
    protocol_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocol_not_in')
    protocol_contains = sgqlc.types.Field(String, graphql_name='protocol_contains')
    protocol_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_contains_nocase')
    protocol_not_contains = sgqlc.types.Field(String, graphql_name='protocol_not_contains')
    protocol_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_contains_nocase')
    protocol_starts_with = sgqlc.types.Field(String, graphql_name='protocol_starts_with')
    protocol_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_starts_with_nocase')
    protocol_not_starts_with = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with')
    protocol_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_starts_with_nocase')
    protocol_ends_with = sgqlc.types.Field(String, graphql_name='protocol_ends_with')
    protocol_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_ends_with_nocase')
    protocol_not_ends_with = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with')
    protocol_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocol_not_ends_with_nocase')
    protocol_ = sgqlc.types.Field(DexAmmProtocol_filter, graphql_name='protocol_')
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
    input_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens')
    input_tokens_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_not')
    input_tokens_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_contains')
    input_tokens_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_contains_nocase')
    input_tokens_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_not_contains')
    input_tokens_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='inputTokens_not_contains_nocase')
    input_tokens_ = sgqlc.types.Field(Token_filter, graphql_name='inputTokens_')
    output_token = sgqlc.types.Field(String, graphql_name='outputToken')
    output_token_not = sgqlc.types.Field(String, graphql_name='outputToken_not')
    output_token_gt = sgqlc.types.Field(String, graphql_name='outputToken_gt')
    output_token_lt = sgqlc.types.Field(String, graphql_name='outputToken_lt')
    output_token_gte = sgqlc.types.Field(String, graphql_name='outputToken_gte')
    output_token_lte = sgqlc.types.Field(String, graphql_name='outputToken_lte')
    output_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='outputToken_in')
    output_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='outputToken_not_in')
    output_token_contains = sgqlc.types.Field(String, graphql_name='outputToken_contains')
    output_token_contains_nocase = sgqlc.types.Field(String, graphql_name='outputToken_contains_nocase')
    output_token_not_contains = sgqlc.types.Field(String, graphql_name='outputToken_not_contains')
    output_token_not_contains_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_contains_nocase')
    output_token_starts_with = sgqlc.types.Field(String, graphql_name='outputToken_starts_with')
    output_token_starts_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_starts_with_nocase')
    output_token_not_starts_with = sgqlc.types.Field(String, graphql_name='outputToken_not_starts_with')
    output_token_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_starts_with_nocase')
    output_token_ends_with = sgqlc.types.Field(String, graphql_name='outputToken_ends_with')
    output_token_ends_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_ends_with_nocase')
    output_token_not_ends_with = sgqlc.types.Field(String, graphql_name='outputToken_not_ends_with')
    output_token_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='outputToken_not_ends_with_nocase')
    output_token_ = sgqlc.types.Field(Token_filter, graphql_name='outputToken_')
    input_token_amounts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts')
    input_token_amounts_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_not')
    input_token_amounts_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_contains')
    input_token_amounts_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_contains_nocase')
    input_token_amounts_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_not_contains')
    input_token_amounts_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='inputTokenAmounts_not_contains_nocase')
    output_token_amount = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount')
    output_token_amount_not = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_not')
    output_token_amount_gt = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_gt')
    output_token_amount_lt = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_lt')
    output_token_amount_gte = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_gte')
    output_token_amount_lte = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount_lte')
    output_token_amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenAmount_in')
    output_token_amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='outputTokenAmount_not_in')
    amount_usd = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD')
    amount_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_not')
    amount_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gt')
    amount_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lt')
    amount_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_gte')
    amount_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='amountUSD_lte')
    amount_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_in')
    amount_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amountUSD_not_in')
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
    pool_ = sgqlc.types.Field(LiquidityPool_filter, graphql_name='pool_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Withdraw_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Withdraw_filter'), graphql_name='or')


class _CircularBuffer_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'blocks', 'blocks_not', 'blocks_contains', 'blocks_contains_nocase', 'blocks_not_contains', 'blocks_not_contains_nocase', 'window_start_index', 'window_start_index_not', 'window_start_index_gt', 'window_start_index_lt', 'window_start_index_gte', 'window_start_index_lte', 'window_start_index_in', 'window_start_index_not_in', 'next_index', 'next_index_not', 'next_index_gt', 'next_index_lt', 'next_index_gte', 'next_index_lte', 'next_index_in', 'next_index_not_in', 'buffer_size', 'buffer_size_not', 'buffer_size_gt', 'buffer_size_lt', 'buffer_size_gte', 'buffer_size_lte', 'buffer_size_in', 'buffer_size_not_in', 'blocks_per_day', 'blocks_per_day_not', 'blocks_per_day_gt', 'blocks_per_day_lt', 'blocks_per_day_gte', 'blocks_per_day_lte', 'blocks_per_day_in', 'blocks_per_day_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    blocks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='blocks')
    blocks_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='blocks_not')
    blocks_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='blocks_contains')
    blocks_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='blocks_contains_nocase')
    blocks_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='blocks_not_contains')
    blocks_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='blocks_not_contains_nocase')
    window_start_index = sgqlc.types.Field(Int, graphql_name='windowStartIndex')
    window_start_index_not = sgqlc.types.Field(Int, graphql_name='windowStartIndex_not')
    window_start_index_gt = sgqlc.types.Field(Int, graphql_name='windowStartIndex_gt')
    window_start_index_lt = sgqlc.types.Field(Int, graphql_name='windowStartIndex_lt')
    window_start_index_gte = sgqlc.types.Field(Int, graphql_name='windowStartIndex_gte')
    window_start_index_lte = sgqlc.types.Field(Int, graphql_name='windowStartIndex_lte')
    window_start_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='windowStartIndex_in')
    window_start_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='windowStartIndex_not_in')
    next_index = sgqlc.types.Field(Int, graphql_name='nextIndex')
    next_index_not = sgqlc.types.Field(Int, graphql_name='nextIndex_not')
    next_index_gt = sgqlc.types.Field(Int, graphql_name='nextIndex_gt')
    next_index_lt = sgqlc.types.Field(Int, graphql_name='nextIndex_lt')
    next_index_gte = sgqlc.types.Field(Int, graphql_name='nextIndex_gte')
    next_index_lte = sgqlc.types.Field(Int, graphql_name='nextIndex_lte')
    next_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='nextIndex_in')
    next_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='nextIndex_not_in')
    buffer_size = sgqlc.types.Field(Int, graphql_name='bufferSize')
    buffer_size_not = sgqlc.types.Field(Int, graphql_name='bufferSize_not')
    buffer_size_gt = sgqlc.types.Field(Int, graphql_name='bufferSize_gt')
    buffer_size_lt = sgqlc.types.Field(Int, graphql_name='bufferSize_lt')
    buffer_size_gte = sgqlc.types.Field(Int, graphql_name='bufferSize_gte')
    buffer_size_lte = sgqlc.types.Field(Int, graphql_name='bufferSize_lte')
    buffer_size_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='bufferSize_in')
    buffer_size_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='bufferSize_not_in')
    blocks_per_day = sgqlc.types.Field(BigDecimal, graphql_name='blocksPerDay')
    blocks_per_day_not = sgqlc.types.Field(BigDecimal, graphql_name='blocksPerDay_not')
    blocks_per_day_gt = sgqlc.types.Field(BigDecimal, graphql_name='blocksPerDay_gt')
    blocks_per_day_lt = sgqlc.types.Field(BigDecimal, graphql_name='blocksPerDay_lt')
    blocks_per_day_gte = sgqlc.types.Field(BigDecimal, graphql_name='blocksPerDay_gte')
    blocks_per_day_lte = sgqlc.types.Field(BigDecimal, graphql_name='blocksPerDay_lte')
    blocks_per_day_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='blocksPerDay_in')
    blocks_per_day_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='blocksPerDay_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('_CircularBuffer_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('_CircularBuffer_filter'), graphql_name='or')


class _LiquidityGauge_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_address', 'pool_address_not', 'pool_address_gt', 'pool_address_lt', 'pool_address_gte', 'pool_address_lte', 'pool_address_in', 'pool_address_not_in', 'pool_address_contains', 'pool_address_contains_nocase', 'pool_address_not_contains', 'pool_address_not_contains_nocase', 'pool_address_starts_with', 'pool_address_starts_with_nocase', 'pool_address_not_starts_with', 'pool_address_not_starts_with_nocase', 'pool_address_ends_with', 'pool_address_ends_with_nocase', 'pool_address_not_ends_with', 'pool_address_not_ends_with_nocase', '_change_block', 'and_', 'or_')
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
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('_LiquidityGauge_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('_LiquidityGauge_filter'), graphql_name='or')


class _LpToken_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_address', 'pool_address_not', 'pool_address_gt', 'pool_address_lt', 'pool_address_gte', 'pool_address_lte', 'pool_address_in', 'pool_address_not_in', 'pool_address_contains', 'pool_address_contains_nocase', 'pool_address_not_contains', 'pool_address_not_contains_nocase', 'pool_address_starts_with', 'pool_address_starts_with_nocase', 'pool_address_not_starts_with', 'pool_address_not_starts_with_nocase', 'pool_address_ends_with', 'pool_address_ends_with_nocase', 'pool_address_not_ends_with', 'pool_address_not_ends_with_nocase', 'registry_address', 'registry_address_not', 'registry_address_gt', 'registry_address_lt', 'registry_address_gte', 'registry_address_lte', 'registry_address_in', 'registry_address_not_in', 'registry_address_contains', 'registry_address_contains_nocase', 'registry_address_not_contains', 'registry_address_not_contains_nocase', 'registry_address_starts_with', 'registry_address_starts_with_nocase', 'registry_address_not_starts_with', 'registry_address_not_starts_with_nocase', 'registry_address_ends_with', 'registry_address_ends_with_nocase', 'registry_address_not_ends_with', 'registry_address_not_ends_with_nocase', '_change_block', 'and_', 'or_')
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
    registry_address = sgqlc.types.Field(String, graphql_name='registryAddress')
    registry_address_not = sgqlc.types.Field(String, graphql_name='registryAddress_not')
    registry_address_gt = sgqlc.types.Field(String, graphql_name='registryAddress_gt')
    registry_address_lt = sgqlc.types.Field(String, graphql_name='registryAddress_lt')
    registry_address_gte = sgqlc.types.Field(String, graphql_name='registryAddress_gte')
    registry_address_lte = sgqlc.types.Field(String, graphql_name='registryAddress_lte')
    registry_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='registryAddress_in')
    registry_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='registryAddress_not_in')
    registry_address_contains = sgqlc.types.Field(String, graphql_name='registryAddress_contains')
    registry_address_contains_nocase = sgqlc.types.Field(String, graphql_name='registryAddress_contains_nocase')
    registry_address_not_contains = sgqlc.types.Field(String, graphql_name='registryAddress_not_contains')
    registry_address_not_contains_nocase = sgqlc.types.Field(String, graphql_name='registryAddress_not_contains_nocase')
    registry_address_starts_with = sgqlc.types.Field(String, graphql_name='registryAddress_starts_with')
    registry_address_starts_with_nocase = sgqlc.types.Field(String, graphql_name='registryAddress_starts_with_nocase')
    registry_address_not_starts_with = sgqlc.types.Field(String, graphql_name='registryAddress_not_starts_with')
    registry_address_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='registryAddress_not_starts_with_nocase')
    registry_address_ends_with = sgqlc.types.Field(String, graphql_name='registryAddress_ends_with')
    registry_address_ends_with_nocase = sgqlc.types.Field(String, graphql_name='registryAddress_ends_with_nocase')
    registry_address_not_ends_with = sgqlc.types.Field(String, graphql_name='registryAddress_not_ends_with')
    registry_address_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='registryAddress_not_ends_with_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('_LpToken_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('_LpToken_filter'), graphql_name='or')



########################################################################
# Output Objects and Interfaces
########################################################################
class Event(sgqlc.types.Interface):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'hash', 'log_index', 'protocol', 'to', 'from_', 'block_number', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    hash = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='hash')
    log_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='logIndex')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('DexAmmProtocol'), graphql_name='protocol')
    to = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='to')
    from_ = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='from')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')


class Protocol(sgqlc.types.Interface):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'name', 'slug', 'schema_version', 'subgraph_version', 'methodology_version', 'network', 'type', 'total_value_locked_usd', 'protocol_controlled_value_usd', 'cumulative_supply_side_revenue_usd', 'cumulative_protocol_side_revenue_usd', 'cumulative_total_revenue_usd', 'cumulative_unique_users', 'total_pool_count', 'daily_usage_metrics', 'hourly_usage_metrics', 'financial_metrics')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    schema_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='schemaVersion')
    subgraph_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='subgraphVersion')
    methodology_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='methodologyVersion')
    network = sgqlc.types.Field(sgqlc.types.non_null(Network), graphql_name='network')
    type = sgqlc.types.Field(sgqlc.types.non_null(ProtocolType), graphql_name='type')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeTotalRevenueUSD')
    cumulative_unique_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cumulativeUniqueUsers')
    total_pool_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalPoolCount')
    daily_usage_metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsDailySnapshot'))), graphql_name='dailyUsageMetrics', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsDailySnapshot_filter, graphql_name='where', default=None)),
))
    )
    hourly_usage_metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsHourlySnapshot'))), graphql_name='hourlyUsageMetrics', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsHourlySnapshot_filter, graphql_name='where', default=None)),
))
    )
    financial_metrics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('FinancialsDailySnapshot'))), graphql_name='financialMetrics', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FinancialsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FinancialsDailySnapshot_filter, graphql_name='where', default=None)),
))
    )


class Account(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ActiveAccount(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class FinancialsDailySnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'protocol', 'total_value_locked_usd', 'protocol_controlled_value_usd', 'daily_volume_usd', 'cumulative_volume_usd', 'daily_supply_side_revenue_usd', 'cumulative_supply_side_revenue_usd', 'daily_protocol_side_revenue_usd', 'cumulative_protocol_side_revenue_usd', 'daily_total_revenue_usd', 'cumulative_total_revenue_usd', 'block_number', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('DexAmmProtocol'), graphql_name='protocol')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    protocol_controlled_value_usd = sgqlc.types.Field(BigDecimal, graphql_name='protocolControlledValueUSD')
    daily_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyVolumeUSD')
    cumulative_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeVolumeUSD')
    daily_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailySupplySideRevenueUSD')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeSupplySideRevenueUSD')
    daily_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyProtocolSideRevenueUSD')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeProtocolSideRevenueUSD')
    daily_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyTotalRevenueUSD')
    cumulative_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeTotalRevenueUSD')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')


class LiquidityPool(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'protocol', 'name', 'symbol', 'input_tokens', '_input_tokens_ordered', 'output_token', 'reward_tokens', 'fees', 'is_single_sided', 'created_timestamp', 'created_block_number', 'total_value_locked_usd', '_tvl_usdexcluding_base_pool_lp_tokens', 'cumulative_supply_side_revenue_usd', 'cumulative_protocol_side_revenue_usd', 'cumulative_total_revenue_usd', 'cumulative_volume_usd', 'input_token_balances', 'input_token_weights', 'output_token_supply', 'output_token_price_usd', 'staked_output_token_amount', 'reward_token_emissions_amount', 'reward_token_emissions_usd', 'daily_snapshots', 'hourly_snapshots', 'deposits', 'withdraws', 'swaps', '_registry_address', '_gauge_address', '_is_metapool')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('DexAmmProtocol'), graphql_name='protocol')
    name = sgqlc.types.Field(String, graphql_name='name')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    input_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='inputTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
))
    )
    _input_tokens_ordered = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='_inputTokensOrdered')
    output_token = sgqlc.types.Field('Token', graphql_name='outputToken')
    reward_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RewardToken')), graphql_name='rewardTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RewardToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RewardToken_filter, graphql_name='where', default=None)),
))
    )
    fees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LiquidityPoolFee'))), graphql_name='fees', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPoolFee_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPoolFee_filter, graphql_name='where', default=None)),
))
    )
    is_single_sided = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSingleSided')
    created_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdTimestamp')
    created_block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='createdBlockNumber')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    _tvl_usdexcluding_base_pool_lp_tokens = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='_tvlUSDExcludingBasePoolLpTokens')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeSupplySideRevenueUSD')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeProtocolSideRevenueUSD')
    cumulative_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeTotalRevenueUSD')
    cumulative_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeVolumeUSD')
    input_token_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='inputTokenBalances')
    input_token_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal))), graphql_name='inputTokenWeights')
    output_token_supply = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply')
    output_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD')
    staked_output_token_amount = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')
    daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LiquidityPoolDailySnapshot'))), graphql_name='dailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPoolDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPoolDailySnapshot_filter, graphql_name='where', default=None)),
))
    )
    hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LiquidityPoolHourlySnapshot'))), graphql_name='hourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPoolHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPoolHourlySnapshot_filter, graphql_name='where', default=None)),
))
    )
    deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Deposit'))), graphql_name='deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Deposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Deposit_filter, graphql_name='where', default=None)),
))
    )
    withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Withdraw'))), graphql_name='withdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Withdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Withdraw_filter, graphql_name='where', default=None)),
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
    _registry_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='_registryAddress')
    _gauge_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='_gaugeAddress')
    _is_metapool = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='_isMetapool')


class LiquidityPoolDailySnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'protocol', 'pool', 'block_number', 'timestamp', 'total_value_locked_usd', 'cumulative_supply_side_revenue_usd', 'daily_supply_side_revenue_usd', 'cumulative_protocol_side_revenue_usd', 'daily_protocol_side_revenue_usd', 'cumulative_total_revenue_usd', 'daily_total_revenue_usd', 'daily_volume_usd', 'daily_volume_by_token_amount', 'daily_volume_by_token_usd', 'cumulative_volume_usd', 'input_token_balances', 'input_token_weights', 'output_token_supply', 'output_token_price_usd', 'staked_output_token_amount', 'reward_token_emissions_amount', 'reward_token_emissions_usd')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('DexAmmProtocol'), graphql_name='protocol')
    pool = sgqlc.types.Field(sgqlc.types.non_null(LiquidityPool), graphql_name='pool')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeSupplySideRevenueUSD')
    daily_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailySupplySideRevenueUSD')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeProtocolSideRevenueUSD')
    daily_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyProtocolSideRevenueUSD')
    cumulative_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeTotalRevenueUSD')
    daily_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyTotalRevenueUSD')
    daily_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='dailyVolumeUSD')
    daily_volume_by_token_amount = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='dailyVolumeByTokenAmount')
    daily_volume_by_token_usd = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal))), graphql_name='dailyVolumeByTokenUSD')
    cumulative_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeVolumeUSD')
    input_token_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='inputTokenBalances')
    input_token_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal))), graphql_name='inputTokenWeights')
    output_token_supply = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply')
    output_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD')
    staked_output_token_amount = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')


class LiquidityPoolFee(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'fee_percentage', 'fee_type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    fee_percentage = sgqlc.types.Field(BigDecimal, graphql_name='feePercentage')
    fee_type = sgqlc.types.Field(sgqlc.types.non_null(LiquidityPoolFeeType), graphql_name='feeType')


class LiquidityPoolHourlySnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'protocol', 'pool', 'block_number', 'timestamp', 'total_value_locked_usd', 'cumulative_supply_side_revenue_usd', 'hourly_supply_side_revenue_usd', 'cumulative_protocol_side_revenue_usd', 'hourly_protocol_side_revenue_usd', 'cumulative_total_revenue_usd', 'hourly_total_revenue_usd', 'hourly_volume_usd', 'hourly_volume_by_token_amount', 'hourly_volume_by_token_usd', 'cumulative_volume_usd', 'input_token_balances', 'input_token_weights', 'output_token_supply', 'output_token_price_usd', 'staked_output_token_amount', 'reward_token_emissions_amount', 'reward_token_emissions_usd')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('DexAmmProtocol'), graphql_name='protocol')
    pool = sgqlc.types.Field(sgqlc.types.non_null(LiquidityPool), graphql_name='pool')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')
    total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalValueLockedUSD')
    cumulative_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeSupplySideRevenueUSD')
    hourly_supply_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='hourlySupplySideRevenueUSD')
    cumulative_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeProtocolSideRevenueUSD')
    hourly_protocol_side_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='hourlyProtocolSideRevenueUSD')
    cumulative_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeTotalRevenueUSD')
    hourly_total_revenue_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='hourlyTotalRevenueUSD')
    hourly_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='hourlyVolumeUSD')
    hourly_volume_by_token_amount = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='hourlyVolumeByTokenAmount')
    hourly_volume_by_token_usd = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal))), graphql_name='hourlyVolumeByTokenUSD')
    cumulative_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeVolumeUSD')
    input_token_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='inputTokenBalances')
    input_token_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal))), graphql_name='inputTokenWeights')
    output_token_supply = sgqlc.types.Field(BigInt, graphql_name='outputTokenSupply')
    output_token_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='outputTokenPriceUSD')
    staked_output_token_amount = sgqlc.types.Field(BigInt, graphql_name='stakedOutputTokenAmount')
    reward_token_emissions_amount = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='rewardTokenEmissionsAmount')
    reward_token_emissions_usd = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rewardTokenEmissionsUSD')


class Query(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('token', 'tokens', 'reward_token', 'reward_tokens', 'liquidity_pool_fee', 'liquidity_pool_fees', 'dex_amm_protocol', 'dex_amm_protocols', 'usage_metrics_daily_snapshot', 'usage_metrics_daily_snapshots', 'usage_metrics_hourly_snapshot', 'usage_metrics_hourly_snapshots', 'financials_daily_snapshot', 'financials_daily_snapshots', 'liquidity_pool', 'liquidity_pools', 'liquidity_pool_daily_snapshot', 'liquidity_pool_daily_snapshots', 'liquidity_pool_hourly_snapshot', 'liquidity_pool_hourly_snapshots', 'deposit', 'deposits', 'withdraw', 'withdraws', 'swap', 'swaps', 'account', 'accounts', 'active_account', 'active_accounts', 'liquidity_gauge', 'liquidity_gauges', 'lp_token', 'lp_tokens', 'circular_buffer', 'circular_buffers', 'protocol', 'protocols', 'event', 'events', '_meta')
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
    reward_token = sgqlc.types.Field('RewardToken', graphql_name='rewardToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    reward_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('RewardToken'))), graphql_name='rewardTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RewardToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RewardToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_fee = sgqlc.types.Field(LiquidityPoolFee, graphql_name='liquidityPoolFee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_fees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPoolFee))), graphql_name='liquidityPoolFees', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPoolFee_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPoolFee_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    dex_amm_protocol = sgqlc.types.Field('DexAmmProtocol', graphql_name='dexAmmProtocol', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    dex_amm_protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DexAmmProtocol'))), graphql_name='dexAmmProtocols', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DexAmmProtocol_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DexAmmProtocol_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_daily_snapshot = sgqlc.types.Field('UsageMetricsDailySnapshot', graphql_name='usageMetricsDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsDailySnapshot'))), graphql_name='usageMetricsDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_hourly_snapshot = sgqlc.types.Field('UsageMetricsHourlySnapshot', graphql_name='usageMetricsHourlySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsHourlySnapshot'))), graphql_name='usageMetricsHourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsHourlySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    financials_daily_snapshot = sgqlc.types.Field(FinancialsDailySnapshot, graphql_name='financialsDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    financials_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FinancialsDailySnapshot))), graphql_name='financialsDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FinancialsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FinancialsDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool = sgqlc.types.Field(LiquidityPool, graphql_name='liquidityPool', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPool))), graphql_name='liquidityPools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPool_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_daily_snapshot = sgqlc.types.Field(LiquidityPoolDailySnapshot, graphql_name='liquidityPoolDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPoolDailySnapshot))), graphql_name='liquidityPoolDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPoolDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPoolDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_hourly_snapshot = sgqlc.types.Field(LiquidityPoolHourlySnapshot, graphql_name='liquidityPoolHourlySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPoolHourlySnapshot))), graphql_name='liquidityPoolHourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPoolHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPoolHourlySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposit = sgqlc.types.Field('Deposit', graphql_name='deposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Deposit'))), graphql_name='deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Deposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Deposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdraw = sgqlc.types.Field('Withdraw', graphql_name='withdraw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Withdraw'))), graphql_name='withdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Withdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Withdraw_filter, graphql_name='where', default=None)),
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
    account = sgqlc.types.Field(Account, graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))), graphql_name='accounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Account_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Account_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    active_account = sgqlc.types.Field(ActiveAccount, graphql_name='activeAccount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    active_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ActiveAccount))), graphql_name='activeAccounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ActiveAccount_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ActiveAccount_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_gauge = sgqlc.types.Field('_LiquidityGauge', graphql_name='liquidityGauge', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_gauges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('_LiquidityGauge'))), graphql_name='liquidityGauges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(_LiquidityGauge_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(_LiquidityGauge_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lp_token = sgqlc.types.Field('_LpToken', graphql_name='lpToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lp_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('_LpToken'))), graphql_name='lpTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(_LpToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(_LpToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    circular_buffer = sgqlc.types.Field('_CircularBuffer', graphql_name='circularBuffer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    circular_buffers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('_CircularBuffer'))), graphql_name='circularBuffers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(_CircularBuffer_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(_CircularBuffer_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocol = sgqlc.types.Field(Protocol, graphql_name='protocol', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Protocol))), graphql_name='protocols', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Protocol_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Protocol_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    event = sgqlc.types.Field(Event, graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Event))), graphql_name='events', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Event_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Event_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class RewardToken(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'token', 'type')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    token = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token')
    type = sgqlc.types.Field(sgqlc.types.non_null(RewardTokenType), graphql_name='type')


class Subscription(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('token', 'tokens', 'reward_token', 'reward_tokens', 'liquidity_pool_fee', 'liquidity_pool_fees', 'dex_amm_protocol', 'dex_amm_protocols', 'usage_metrics_daily_snapshot', 'usage_metrics_daily_snapshots', 'usage_metrics_hourly_snapshot', 'usage_metrics_hourly_snapshots', 'financials_daily_snapshot', 'financials_daily_snapshots', 'liquidity_pool', 'liquidity_pools', 'liquidity_pool_daily_snapshot', 'liquidity_pool_daily_snapshots', 'liquidity_pool_hourly_snapshot', 'liquidity_pool_hourly_snapshots', 'deposit', 'deposits', 'withdraw', 'withdraws', 'swap', 'swaps', 'account', 'accounts', 'active_account', 'active_accounts', 'liquidity_gauge', 'liquidity_gauges', 'lp_token', 'lp_tokens', 'circular_buffer', 'circular_buffers', 'protocol', 'protocols', 'event', 'events', '_meta')
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
    reward_token = sgqlc.types.Field(RewardToken, graphql_name='rewardToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    reward_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RewardToken))), graphql_name='rewardTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(RewardToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(RewardToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_fee = sgqlc.types.Field(LiquidityPoolFee, graphql_name='liquidityPoolFee', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_fees = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPoolFee))), graphql_name='liquidityPoolFees', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPoolFee_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPoolFee_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    dex_amm_protocol = sgqlc.types.Field('DexAmmProtocol', graphql_name='dexAmmProtocol', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    dex_amm_protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('DexAmmProtocol'))), graphql_name='dexAmmProtocols', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(DexAmmProtocol_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(DexAmmProtocol_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_daily_snapshot = sgqlc.types.Field('UsageMetricsDailySnapshot', graphql_name='usageMetricsDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsDailySnapshot'))), graphql_name='usageMetricsDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_hourly_snapshot = sgqlc.types.Field('UsageMetricsHourlySnapshot', graphql_name='usageMetricsHourlySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    usage_metrics_hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsageMetricsHourlySnapshot'))), graphql_name='usageMetricsHourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UsageMetricsHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UsageMetricsHourlySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    financials_daily_snapshot = sgqlc.types.Field(FinancialsDailySnapshot, graphql_name='financialsDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    financials_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FinancialsDailySnapshot))), graphql_name='financialsDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FinancialsDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FinancialsDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool = sgqlc.types.Field(LiquidityPool, graphql_name='liquidityPool', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPool))), graphql_name='liquidityPools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPool_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_daily_snapshot = sgqlc.types.Field(LiquidityPoolDailySnapshot, graphql_name='liquidityPoolDailySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_daily_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPoolDailySnapshot))), graphql_name='liquidityPoolDailySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPoolDailySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPoolDailySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_hourly_snapshot = sgqlc.types.Field(LiquidityPoolHourlySnapshot, graphql_name='liquidityPoolHourlySnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_pool_hourly_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPoolHourlySnapshot))), graphql_name='liquidityPoolHourlySnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPoolHourlySnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPoolHourlySnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposit = sgqlc.types.Field('Deposit', graphql_name='deposit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    deposits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Deposit'))), graphql_name='deposits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Deposit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Deposit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdraw = sgqlc.types.Field('Withdraw', graphql_name='withdraw', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    withdraws = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Withdraw'))), graphql_name='withdraws', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Withdraw_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Withdraw_filter, graphql_name='where', default=None)),
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
    account = sgqlc.types.Field(Account, graphql_name='account', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Account))), graphql_name='accounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Account_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Account_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    active_account = sgqlc.types.Field(ActiveAccount, graphql_name='activeAccount', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    active_accounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ActiveAccount))), graphql_name='activeAccounts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ActiveAccount_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ActiveAccount_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_gauge = sgqlc.types.Field('_LiquidityGauge', graphql_name='liquidityGauge', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    liquidity_gauges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('_LiquidityGauge'))), graphql_name='liquidityGauges', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(_LiquidityGauge_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(_LiquidityGauge_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lp_token = sgqlc.types.Field('_LpToken', graphql_name='lpToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    lp_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('_LpToken'))), graphql_name='lpTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(_LpToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(_LpToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    circular_buffer = sgqlc.types.Field('_CircularBuffer', graphql_name='circularBuffer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    circular_buffers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('_CircularBuffer'))), graphql_name='circularBuffers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(_CircularBuffer_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(_CircularBuffer_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocol = sgqlc.types.Field(Protocol, graphql_name='protocol', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocols = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Protocol))), graphql_name='protocols', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Protocol_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Protocol_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    event = sgqlc.types.Field(Event, graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Event))), graphql_name='events', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Event_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Event_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class Token(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'name', 'symbol', 'decimals', 'is_base_pool_lp_token', 'last_price_usd', 'last_price_block_number', 'oracle_type', '_total_supply', '_total_value_locked_usd', '_large_price_change_buffer', '_large_tvlimpact_buffer')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    is_base_pool_lp_token = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBasePoolLpToken')
    last_price_usd = sgqlc.types.Field(BigDecimal, graphql_name='lastPriceUSD')
    last_price_block_number = sgqlc.types.Field(BigInt, graphql_name='lastPriceBlockNumber')
    oracle_type = sgqlc.types.Field(String, graphql_name='oracleType')
    _total_supply = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='_totalSupply')
    _total_value_locked_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='_totalValueLockedUSD')
    _large_price_change_buffer = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='_largePriceChangeBuffer')
    _large_tvlimpact_buffer = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='_largeTVLImpactBuffer')


class UsageMetricsDailySnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'protocol', 'daily_active_users', 'cumulative_unique_users', 'daily_transaction_count', 'daily_deposit_count', 'daily_withdraw_count', 'daily_swap_count', 'total_pool_count', 'block_number', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('DexAmmProtocol'), graphql_name='protocol')
    daily_active_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyActiveUsers')
    cumulative_unique_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cumulativeUniqueUsers')
    daily_transaction_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyTransactionCount')
    daily_deposit_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyDepositCount')
    daily_withdraw_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailyWithdrawCount')
    daily_swap_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dailySwapCount')
    total_pool_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalPoolCount')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')


class UsageMetricsHourlySnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'protocol', 'hourly_active_users', 'cumulative_unique_users', 'hourly_transaction_count', 'hourly_deposit_count', 'hourly_withdraw_count', 'hourly_swap_count', 'block_number', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol = sgqlc.types.Field(sgqlc.types.non_null('DexAmmProtocol'), graphql_name='protocol')
    hourly_active_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyActiveUsers')
    cumulative_unique_users = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cumulativeUniqueUsers')
    hourly_transaction_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyTransactionCount')
    hourly_deposit_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyDepositCount')
    hourly_withdraw_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlyWithdrawCount')
    hourly_swap_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hourlySwapCount')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='blockNumber')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='timestamp')


class _Block_(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('hash', 'number', 'timestamp', 'parent_hash')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    parent_hash = sgqlc.types.Field(Bytes, graphql_name='parentHash')


class _CircularBuffer(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'blocks', 'window_start_index', 'next_index', 'buffer_size', 'blocks_per_day')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    blocks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='blocks')
    window_start_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='windowStartIndex')
    next_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nextIndex')
    buffer_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bufferSize')
    blocks_per_day = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='blocksPerDay')


class _LiquidityGauge(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_address')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolAddress')


class _LpToken(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_address', 'registry_address')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolAddress')
    registry_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='registryAddress')


class _Meta_(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('block', 'deployment', 'has_indexing_errors')
    block = sgqlc.types.Field(sgqlc.types.non_null(_Block_), graphql_name='block')
    deployment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='deployment')
    has_indexing_errors = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIndexingErrors')


class Deposit(sgqlc.types.Type, Event):
    __schema__ = graphql_schema
    __field_names__ = ('input_tokens', 'output_token', 'input_token_amounts', 'output_token_amount', 'amount_usd', 'pool')
    input_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Token))), graphql_name='inputTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
))
    )
    output_token = sgqlc.types.Field(Token, graphql_name='outputToken')
    input_token_amounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='inputTokenAmounts')
    output_token_amount = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount')
    amount_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amountUSD')
    pool = sgqlc.types.Field(sgqlc.types.non_null(LiquidityPool), graphql_name='pool')


class DexAmmProtocol(sgqlc.types.Type, Protocol):
    __schema__ = graphql_schema
    __field_names__ = ('cumulative_volume_usd', 'pools', '_pool_ids')
    cumulative_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cumulativeVolumeUSD')
    pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LiquidityPool))), graphql_name='pools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LiquidityPool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LiquidityPool_filter, graphql_name='where', default=None)),
))
    )
    _pool_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='_poolIds')


class Swap(sgqlc.types.Type, Event):
    __schema__ = graphql_schema
    __field_names__ = ('token_in', 'amount_in', 'amount_in_usd', 'token_out', 'amount_out', 'amount_out_usd', 'pool')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='tokenIn')
    amount_in = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amountIn')
    amount_in_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amountInUSD')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='tokenOut')
    amount_out = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amountOut')
    amount_out_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amountOutUSD')
    pool = sgqlc.types.Field(sgqlc.types.non_null(LiquidityPool), graphql_name='pool')


class Withdraw(sgqlc.types.Type, Event):
    __schema__ = graphql_schema
    __field_names__ = ('input_tokens', 'output_token', 'input_token_amounts', 'output_token_amount', 'amount_usd', 'pool')
    input_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Token))), graphql_name='inputTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Token_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Token_filter, graphql_name='where', default=None)),
))
    )
    output_token = sgqlc.types.Field(Token, graphql_name='outputToken')
    input_token_amounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='inputTokenAmounts')
    output_token_amount = sgqlc.types.Field(BigInt, graphql_name='outputTokenAmount')
    amount_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amountUSD')
    pool = sgqlc.types.Field(sgqlc.types.non_null(LiquidityPool), graphql_name='pool')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
graphql_schema.query_type = Query
graphql_schema.mutation_type = None
graphql_schema.subscription_type = Subscription

