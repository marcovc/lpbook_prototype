import sgqlc.types


graphql_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AmpUpdate_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('endAmp', 'endTimestamp', 'id', 'poolId', 'poolId__address', 'poolId__alpha', 'poolId__amp', 'poolId__baseToken', 'poolId__beta', 'poolId__c', 'poolId__createTime', 'poolId__dSq', 'poolId__delta', 'poolId__epsilon', 'poolId__expiryTime', 'poolId__factory', 'poolId__holdersCount', 'poolId__id', 'poolId__isInRecoveryMode', 'poolId__isPaused', 'poolId__joinExitEnabled', 'poolId__lambda', 'poolId__lastJoinExitAmp', 'poolId__lastPostJoinExitInvariant', 'poolId__lowerTarget', 'poolId__mainIndex', 'poolId__managementAumFee', 'poolId__managementFee', 'poolId__mustAllowlistLPs', 'poolId__name', 'poolId__oracleEnabled', 'poolId__owner', 'poolId__poolType', 'poolId__poolTypeVersion', 'poolId__principalToken', 'poolId__protocolAumFeeCache', 'poolId__protocolId', 'poolId__protocolSwapFeeCache', 'poolId__protocolYieldFeeCache', 'poolId__root3Alpha', 'poolId__s', 'poolId__sqrtAlpha', 'poolId__sqrtBeta', 'poolId__strategyType', 'poolId__swapEnabled', 'poolId__swapEnabledCurationSignal', 'poolId__swapEnabledInternal', 'poolId__swapFee', 'poolId__swapsCount', 'poolId__symbol', 'poolId__tauAlphaX', 'poolId__tauAlphaY', 'poolId__tauBetaX', 'poolId__tauBetaY', 'poolId__totalAumFeeCollectedInBPT', 'poolId__totalLiquidity', 'poolId__totalLiquiditySansBPT', 'poolId__totalProtocolFee', 'poolId__totalProtocolFeePaidInBPT', 'poolId__totalShares', 'poolId__totalSwapFee', 'poolId__totalSwapVolume', 'poolId__totalWeight', 'poolId__tx', 'poolId__u', 'poolId__unitSeconds', 'poolId__upperTarget', 'poolId__v', 'poolId__w', 'poolId__wrappedIndex', 'poolId__z', 'scheduledTimestamp', 'startAmp', 'startTimestamp')


class BalancerSnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'poolCount', 'timestamp', 'totalLiquidity', 'totalProtocolFee', 'totalSwapCount', 'totalSwapFee', 'totalSwapVolume', 'vault', 'vault__id', 'vault__poolCount', 'vault__protocolFeesCollector', 'vault__totalLiquidity', 'vault__totalProtocolFee', 'vault__totalSwapCount', 'vault__totalSwapFee', 'vault__totalSwapVolume')


class Balancer_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'poolCount', 'pools', 'protocolFeesCollector', 'snapshots', 'totalLiquidity', 'totalProtocolFee', 'totalSwapCount', 'totalSwapFee', 'totalSwapVolume')


class BigDecimal(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = graphql_schema


Boolean = sgqlc.types.Boolean

class Bytes(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class CircuitBreaker_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('bptPrice', 'id', 'lowerBoundPercentage', 'pool', 'pool__address', 'pool__alpha', 'pool__amp', 'pool__baseToken', 'pool__beta', 'pool__c', 'pool__createTime', 'pool__dSq', 'pool__delta', 'pool__epsilon', 'pool__expiryTime', 'pool__factory', 'pool__holdersCount', 'pool__id', 'pool__isInRecoveryMode', 'pool__isPaused', 'pool__joinExitEnabled', 'pool__lambda', 'pool__lastJoinExitAmp', 'pool__lastPostJoinExitInvariant', 'pool__lowerTarget', 'pool__mainIndex', 'pool__managementAumFee', 'pool__managementFee', 'pool__mustAllowlistLPs', 'pool__name', 'pool__oracleEnabled', 'pool__owner', 'pool__poolType', 'pool__poolTypeVersion', 'pool__principalToken', 'pool__protocolAumFeeCache', 'pool__protocolId', 'pool__protocolSwapFeeCache', 'pool__protocolYieldFeeCache', 'pool__root3Alpha', 'pool__s', 'pool__sqrtAlpha', 'pool__sqrtBeta', 'pool__strategyType', 'pool__swapEnabled', 'pool__swapEnabledCurationSignal', 'pool__swapEnabledInternal', 'pool__swapFee', 'pool__swapsCount', 'pool__symbol', 'pool__tauAlphaX', 'pool__tauAlphaY', 'pool__tauBetaX', 'pool__tauBetaY', 'pool__totalAumFeeCollectedInBPT', 'pool__totalLiquidity', 'pool__totalLiquiditySansBPT', 'pool__totalProtocolFee', 'pool__totalProtocolFeePaidInBPT', 'pool__totalShares', 'pool__totalSwapFee', 'pool__totalSwapVolume', 'pool__totalWeight', 'pool__tx', 'pool__u', 'pool__unitSeconds', 'pool__upperTarget', 'pool__v', 'pool__w', 'pool__wrappedIndex', 'pool__z', 'token', 'token__address', 'token__assetManager', 'token__balance', 'token__cashBalance', 'token__decimals', 'token__id', 'token__index', 'token__isExemptFromYieldProtocolFee', 'token__managedBalance', 'token__name', 'token__oldPriceRate', 'token__paidProtocolFees', 'token__priceRate', 'token__symbol', 'token__weight', 'upperBoundPercentage')


class FXOracle_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'tokens')


Float = sgqlc.types.Float

class GradualWeightUpdate_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('endTimestamp', 'endWeights', 'id', 'poolId', 'poolId__address', 'poolId__alpha', 'poolId__amp', 'poolId__baseToken', 'poolId__beta', 'poolId__c', 'poolId__createTime', 'poolId__dSq', 'poolId__delta', 'poolId__epsilon', 'poolId__expiryTime', 'poolId__factory', 'poolId__holdersCount', 'poolId__id', 'poolId__isInRecoveryMode', 'poolId__isPaused', 'poolId__joinExitEnabled', 'poolId__lambda', 'poolId__lastJoinExitAmp', 'poolId__lastPostJoinExitInvariant', 'poolId__lowerTarget', 'poolId__mainIndex', 'poolId__managementAumFee', 'poolId__managementFee', 'poolId__mustAllowlistLPs', 'poolId__name', 'poolId__oracleEnabled', 'poolId__owner', 'poolId__poolType', 'poolId__poolTypeVersion', 'poolId__principalToken', 'poolId__protocolAumFeeCache', 'poolId__protocolId', 'poolId__protocolSwapFeeCache', 'poolId__protocolYieldFeeCache', 'poolId__root3Alpha', 'poolId__s', 'poolId__sqrtAlpha', 'poolId__sqrtBeta', 'poolId__strategyType', 'poolId__swapEnabled', 'poolId__swapEnabledCurationSignal', 'poolId__swapEnabledInternal', 'poolId__swapFee', 'poolId__swapsCount', 'poolId__symbol', 'poolId__tauAlphaX', 'poolId__tauAlphaY', 'poolId__tauBetaX', 'poolId__tauBetaY', 'poolId__totalAumFeeCollectedInBPT', 'poolId__totalLiquidity', 'poolId__totalLiquiditySansBPT', 'poolId__totalProtocolFee', 'poolId__totalProtocolFeePaidInBPT', 'poolId__totalShares', 'poolId__totalSwapFee', 'poolId__totalSwapVolume', 'poolId__totalWeight', 'poolId__tx', 'poolId__u', 'poolId__unitSeconds', 'poolId__upperTarget', 'poolId__v', 'poolId__w', 'poolId__wrappedIndex', 'poolId__z', 'scheduledTimestamp', 'startTimestamp', 'startWeights')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class Int8(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class InvestType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('Exit', 'Join')


class JoinExit_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('amounts', 'block', 'id', 'pool', 'pool__address', 'pool__alpha', 'pool__amp', 'pool__baseToken', 'pool__beta', 'pool__c', 'pool__createTime', 'pool__dSq', 'pool__delta', 'pool__epsilon', 'pool__expiryTime', 'pool__factory', 'pool__holdersCount', 'pool__id', 'pool__isInRecoveryMode', 'pool__isPaused', 'pool__joinExitEnabled', 'pool__lambda', 'pool__lastJoinExitAmp', 'pool__lastPostJoinExitInvariant', 'pool__lowerTarget', 'pool__mainIndex', 'pool__managementAumFee', 'pool__managementFee', 'pool__mustAllowlistLPs', 'pool__name', 'pool__oracleEnabled', 'pool__owner', 'pool__poolType', 'pool__poolTypeVersion', 'pool__principalToken', 'pool__protocolAumFeeCache', 'pool__protocolId', 'pool__protocolSwapFeeCache', 'pool__protocolYieldFeeCache', 'pool__root3Alpha', 'pool__s', 'pool__sqrtAlpha', 'pool__sqrtBeta', 'pool__strategyType', 'pool__swapEnabled', 'pool__swapEnabledCurationSignal', 'pool__swapEnabledInternal', 'pool__swapFee', 'pool__swapsCount', 'pool__symbol', 'pool__tauAlphaX', 'pool__tauAlphaY', 'pool__tauBetaX', 'pool__tauBetaY', 'pool__totalAumFeeCollectedInBPT', 'pool__totalLiquidity', 'pool__totalLiquiditySansBPT', 'pool__totalProtocolFee', 'pool__totalProtocolFeePaidInBPT', 'pool__totalShares', 'pool__totalSwapFee', 'pool__totalSwapVolume', 'pool__totalWeight', 'pool__tx', 'pool__u', 'pool__unitSeconds', 'pool__upperTarget', 'pool__v', 'pool__w', 'pool__wrappedIndex', 'pool__z', 'sender', 'timestamp', 'tx', 'type', 'user', 'user__id', 'valueUSD')


class LatestPrice_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('asset', 'block', 'id', 'poolId', 'poolId__address', 'poolId__alpha', 'poolId__amp', 'poolId__baseToken', 'poolId__beta', 'poolId__c', 'poolId__createTime', 'poolId__dSq', 'poolId__delta', 'poolId__epsilon', 'poolId__expiryTime', 'poolId__factory', 'poolId__holdersCount', 'poolId__id', 'poolId__isInRecoveryMode', 'poolId__isPaused', 'poolId__joinExitEnabled', 'poolId__lambda', 'poolId__lastJoinExitAmp', 'poolId__lastPostJoinExitInvariant', 'poolId__lowerTarget', 'poolId__mainIndex', 'poolId__managementAumFee', 'poolId__managementFee', 'poolId__mustAllowlistLPs', 'poolId__name', 'poolId__oracleEnabled', 'poolId__owner', 'poolId__poolType', 'poolId__poolTypeVersion', 'poolId__principalToken', 'poolId__protocolAumFeeCache', 'poolId__protocolId', 'poolId__protocolSwapFeeCache', 'poolId__protocolYieldFeeCache', 'poolId__root3Alpha', 'poolId__s', 'poolId__sqrtAlpha', 'poolId__sqrtBeta', 'poolId__strategyType', 'poolId__swapEnabled', 'poolId__swapEnabledCurationSignal', 'poolId__swapEnabledInternal', 'poolId__swapFee', 'poolId__swapsCount', 'poolId__symbol', 'poolId__tauAlphaX', 'poolId__tauAlphaY', 'poolId__tauBetaX', 'poolId__tauBetaY', 'poolId__totalAumFeeCollectedInBPT', 'poolId__totalLiquidity', 'poolId__totalLiquiditySansBPT', 'poolId__totalProtocolFee', 'poolId__totalProtocolFeePaidInBPT', 'poolId__totalShares', 'poolId__totalSwapFee', 'poolId__totalSwapVolume', 'poolId__totalWeight', 'poolId__tx', 'poolId__u', 'poolId__unitSeconds', 'poolId__upperTarget', 'poolId__v', 'poolId__w', 'poolId__wrappedIndex', 'poolId__z', 'price', 'pricingAsset')


class ManagementOperation_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('cashDelta', 'id', 'managedDelta', 'poolTokenId', 'poolTokenId__address', 'poolTokenId__assetManager', 'poolTokenId__balance', 'poolTokenId__cashBalance', 'poolTokenId__decimals', 'poolTokenId__id', 'poolTokenId__index', 'poolTokenId__isExemptFromYieldProtocolFee', 'poolTokenId__managedBalance', 'poolTokenId__name', 'poolTokenId__oldPriceRate', 'poolTokenId__paidProtocolFees', 'poolTokenId__priceRate', 'poolTokenId__symbol', 'poolTokenId__weight', 'timestamp', 'type')


class OperationType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('Deposit', 'Update', 'Withdraw')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('asc', 'desc')


class PoolContract_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'pool', 'pool__address', 'pool__alpha', 'pool__amp', 'pool__baseToken', 'pool__beta', 'pool__c', 'pool__createTime', 'pool__dSq', 'pool__delta', 'pool__epsilon', 'pool__expiryTime', 'pool__factory', 'pool__holdersCount', 'pool__id', 'pool__isInRecoveryMode', 'pool__isPaused', 'pool__joinExitEnabled', 'pool__lambda', 'pool__lastJoinExitAmp', 'pool__lastPostJoinExitInvariant', 'pool__lowerTarget', 'pool__mainIndex', 'pool__managementAumFee', 'pool__managementFee', 'pool__mustAllowlistLPs', 'pool__name', 'pool__oracleEnabled', 'pool__owner', 'pool__poolType', 'pool__poolTypeVersion', 'pool__principalToken', 'pool__protocolAumFeeCache', 'pool__protocolId', 'pool__protocolSwapFeeCache', 'pool__protocolYieldFeeCache', 'pool__root3Alpha', 'pool__s', 'pool__sqrtAlpha', 'pool__sqrtBeta', 'pool__strategyType', 'pool__swapEnabled', 'pool__swapEnabledCurationSignal', 'pool__swapEnabledInternal', 'pool__swapFee', 'pool__swapsCount', 'pool__symbol', 'pool__tauAlphaX', 'pool__tauAlphaY', 'pool__tauBetaX', 'pool__tauBetaY', 'pool__totalAumFeeCollectedInBPT', 'pool__totalLiquidity', 'pool__totalLiquiditySansBPT', 'pool__totalProtocolFee', 'pool__totalProtocolFeePaidInBPT', 'pool__totalShares', 'pool__totalSwapFee', 'pool__totalSwapVolume', 'pool__totalWeight', 'pool__tx', 'pool__u', 'pool__unitSeconds', 'pool__upperTarget', 'pool__v', 'pool__w', 'pool__wrappedIndex', 'pool__z')


class PoolHistoricalLiquidity_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'id', 'poolId', 'poolId__address', 'poolId__alpha', 'poolId__amp', 'poolId__baseToken', 'poolId__beta', 'poolId__c', 'poolId__createTime', 'poolId__dSq', 'poolId__delta', 'poolId__epsilon', 'poolId__expiryTime', 'poolId__factory', 'poolId__holdersCount', 'poolId__id', 'poolId__isInRecoveryMode', 'poolId__isPaused', 'poolId__joinExitEnabled', 'poolId__lambda', 'poolId__lastJoinExitAmp', 'poolId__lastPostJoinExitInvariant', 'poolId__lowerTarget', 'poolId__mainIndex', 'poolId__managementAumFee', 'poolId__managementFee', 'poolId__mustAllowlistLPs', 'poolId__name', 'poolId__oracleEnabled', 'poolId__owner', 'poolId__poolType', 'poolId__poolTypeVersion', 'poolId__principalToken', 'poolId__protocolAumFeeCache', 'poolId__protocolId', 'poolId__protocolSwapFeeCache', 'poolId__protocolYieldFeeCache', 'poolId__root3Alpha', 'poolId__s', 'poolId__sqrtAlpha', 'poolId__sqrtBeta', 'poolId__strategyType', 'poolId__swapEnabled', 'poolId__swapEnabledCurationSignal', 'poolId__swapEnabledInternal', 'poolId__swapFee', 'poolId__swapsCount', 'poolId__symbol', 'poolId__tauAlphaX', 'poolId__tauAlphaY', 'poolId__tauBetaX', 'poolId__tauBetaY', 'poolId__totalAumFeeCollectedInBPT', 'poolId__totalLiquidity', 'poolId__totalLiquiditySansBPT', 'poolId__totalProtocolFee', 'poolId__totalProtocolFeePaidInBPT', 'poolId__totalShares', 'poolId__totalSwapFee', 'poolId__totalSwapVolume', 'poolId__totalWeight', 'poolId__tx', 'poolId__u', 'poolId__unitSeconds', 'poolId__upperTarget', 'poolId__v', 'poolId__w', 'poolId__wrappedIndex', 'poolId__z', 'poolLiquidity', 'poolShareValue', 'poolTotalShares', 'pricingAsset')


class PoolShare_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('balance', 'id', 'poolId', 'poolId__address', 'poolId__alpha', 'poolId__amp', 'poolId__baseToken', 'poolId__beta', 'poolId__c', 'poolId__createTime', 'poolId__dSq', 'poolId__delta', 'poolId__epsilon', 'poolId__expiryTime', 'poolId__factory', 'poolId__holdersCount', 'poolId__id', 'poolId__isInRecoveryMode', 'poolId__isPaused', 'poolId__joinExitEnabled', 'poolId__lambda', 'poolId__lastJoinExitAmp', 'poolId__lastPostJoinExitInvariant', 'poolId__lowerTarget', 'poolId__mainIndex', 'poolId__managementAumFee', 'poolId__managementFee', 'poolId__mustAllowlistLPs', 'poolId__name', 'poolId__oracleEnabled', 'poolId__owner', 'poolId__poolType', 'poolId__poolTypeVersion', 'poolId__principalToken', 'poolId__protocolAumFeeCache', 'poolId__protocolId', 'poolId__protocolSwapFeeCache', 'poolId__protocolYieldFeeCache', 'poolId__root3Alpha', 'poolId__s', 'poolId__sqrtAlpha', 'poolId__sqrtBeta', 'poolId__strategyType', 'poolId__swapEnabled', 'poolId__swapEnabledCurationSignal', 'poolId__swapEnabledInternal', 'poolId__swapFee', 'poolId__swapsCount', 'poolId__symbol', 'poolId__tauAlphaX', 'poolId__tauAlphaY', 'poolId__tauBetaX', 'poolId__tauBetaY', 'poolId__totalAumFeeCollectedInBPT', 'poolId__totalLiquidity', 'poolId__totalLiquiditySansBPT', 'poolId__totalProtocolFee', 'poolId__totalProtocolFeePaidInBPT', 'poolId__totalShares', 'poolId__totalSwapFee', 'poolId__totalSwapVolume', 'poolId__totalWeight', 'poolId__tx', 'poolId__u', 'poolId__unitSeconds', 'poolId__upperTarget', 'poolId__v', 'poolId__w', 'poolId__wrappedIndex', 'poolId__z', 'userAddress', 'userAddress__id')


class PoolSnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('amounts', 'holdersCount', 'id', 'liquidity', 'pool', 'pool__address', 'pool__alpha', 'pool__amp', 'pool__baseToken', 'pool__beta', 'pool__c', 'pool__createTime', 'pool__dSq', 'pool__delta', 'pool__epsilon', 'pool__expiryTime', 'pool__factory', 'pool__holdersCount', 'pool__id', 'pool__isInRecoveryMode', 'pool__isPaused', 'pool__joinExitEnabled', 'pool__lambda', 'pool__lastJoinExitAmp', 'pool__lastPostJoinExitInvariant', 'pool__lowerTarget', 'pool__mainIndex', 'pool__managementAumFee', 'pool__managementFee', 'pool__mustAllowlistLPs', 'pool__name', 'pool__oracleEnabled', 'pool__owner', 'pool__poolType', 'pool__poolTypeVersion', 'pool__principalToken', 'pool__protocolAumFeeCache', 'pool__protocolId', 'pool__protocolSwapFeeCache', 'pool__protocolYieldFeeCache', 'pool__root3Alpha', 'pool__s', 'pool__sqrtAlpha', 'pool__sqrtBeta', 'pool__strategyType', 'pool__swapEnabled', 'pool__swapEnabledCurationSignal', 'pool__swapEnabledInternal', 'pool__swapFee', 'pool__swapsCount', 'pool__symbol', 'pool__tauAlphaX', 'pool__tauAlphaY', 'pool__tauBetaX', 'pool__tauBetaY', 'pool__totalAumFeeCollectedInBPT', 'pool__totalLiquidity', 'pool__totalLiquiditySansBPT', 'pool__totalProtocolFee', 'pool__totalProtocolFeePaidInBPT', 'pool__totalShares', 'pool__totalSwapFee', 'pool__totalSwapVolume', 'pool__totalWeight', 'pool__tx', 'pool__u', 'pool__unitSeconds', 'pool__upperTarget', 'pool__v', 'pool__w', 'pool__wrappedIndex', 'pool__z', 'protocolFee', 'swapFees', 'swapVolume', 'swapsCount', 'timestamp', 'totalShares')


class PoolToken_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'assetManager', 'balance', 'cashBalance', 'circuitBreaker', 'circuitBreaker__bptPrice', 'circuitBreaker__id', 'circuitBreaker__lowerBoundPercentage', 'circuitBreaker__upperBoundPercentage', 'decimals', 'id', 'index', 'isExemptFromYieldProtocolFee', 'managedBalance', 'managements', 'name', 'oldPriceRate', 'paidProtocolFees', 'poolId', 'poolId__address', 'poolId__alpha', 'poolId__amp', 'poolId__baseToken', 'poolId__beta', 'poolId__c', 'poolId__createTime', 'poolId__dSq', 'poolId__delta', 'poolId__epsilon', 'poolId__expiryTime', 'poolId__factory', 'poolId__holdersCount', 'poolId__id', 'poolId__isInRecoveryMode', 'poolId__isPaused', 'poolId__joinExitEnabled', 'poolId__lambda', 'poolId__lastJoinExitAmp', 'poolId__lastPostJoinExitInvariant', 'poolId__lowerTarget', 'poolId__mainIndex', 'poolId__managementAumFee', 'poolId__managementFee', 'poolId__mustAllowlistLPs', 'poolId__name', 'poolId__oracleEnabled', 'poolId__owner', 'poolId__poolType', 'poolId__poolTypeVersion', 'poolId__principalToken', 'poolId__protocolAumFeeCache', 'poolId__protocolId', 'poolId__protocolSwapFeeCache', 'poolId__protocolYieldFeeCache', 'poolId__root3Alpha', 'poolId__s', 'poolId__sqrtAlpha', 'poolId__sqrtBeta', 'poolId__strategyType', 'poolId__swapEnabled', 'poolId__swapEnabledCurationSignal', 'poolId__swapEnabledInternal', 'poolId__swapFee', 'poolId__swapsCount', 'poolId__symbol', 'poolId__tauAlphaX', 'poolId__tauAlphaY', 'poolId__tauBetaX', 'poolId__tauBetaY', 'poolId__totalAumFeeCollectedInBPT', 'poolId__totalLiquidity', 'poolId__totalLiquiditySansBPT', 'poolId__totalProtocolFee', 'poolId__totalProtocolFeePaidInBPT', 'poolId__totalShares', 'poolId__totalSwapFee', 'poolId__totalSwapVolume', 'poolId__totalWeight', 'poolId__tx', 'poolId__u', 'poolId__unitSeconds', 'poolId__upperTarget', 'poolId__v', 'poolId__w', 'poolId__wrappedIndex', 'poolId__z', 'priceRate', 'symbol', 'token', 'token__address', 'token__decimals', 'token__fxOracleDecimals', 'token__id', 'token__latestFXPrice', 'token__latestUSDPrice', 'token__latestUSDPriceTimestamp', 'token__name', 'token__symbol', 'token__totalBalanceNotional', 'token__totalBalanceUSD', 'token__totalSwapCount', 'token__totalVolumeNotional', 'token__totalVolumeUSD', 'weight')


class Pool_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'alpha', 'amp', 'ampUpdates', 'baseToken', 'beta', 'c', 'circuitBreakers', 'createTime', 'dSq', 'delta', 'epsilon', 'expiryTime', 'factory', 'historicalValues', 'holdersCount', 'id', 'isInRecoveryMode', 'isPaused', 'joinExitEnabled', 'joinsExits', 'lambda', 'lastJoinExitAmp', 'lastPostJoinExitInvariant', 'latestAmpUpdate', 'latestAmpUpdate__endAmp', 'latestAmpUpdate__endTimestamp', 'latestAmpUpdate__id', 'latestAmpUpdate__scheduledTimestamp', 'latestAmpUpdate__startAmp', 'latestAmpUpdate__startTimestamp', 'lowerTarget', 'mainIndex', 'managementAumFee', 'managementFee', 'mustAllowlistLPs', 'name', 'oracleEnabled', 'owner', 'poolType', 'poolTypeVersion', 'priceRateProviders', 'principalToken', 'protocolAumFeeCache', 'protocolId', 'protocolIdData', 'protocolIdData__id', 'protocolIdData__name', 'protocolSwapFeeCache', 'protocolYieldFeeCache', 'root3Alpha', 's', 'shares', 'snapshots', 'sqrtAlpha', 'sqrtBeta', 'strategyType', 'swapEnabled', 'swapEnabledCurationSignal', 'swapEnabledInternal', 'swapFee', 'swaps', 'swapsCount', 'symbol', 'tauAlphaX', 'tauAlphaY', 'tauBetaX', 'tauBetaY', 'tokens', 'tokensList', 'totalAumFeeCollectedInBPT', 'totalLiquidity', 'totalLiquiditySansBPT', 'totalProtocolFee', 'totalProtocolFeePaidInBPT', 'totalShares', 'totalSwapFee', 'totalSwapVolume', 'totalWeight', 'tx', 'u', 'unitSeconds', 'upperTarget', 'v', 'vaultID', 'vaultID__id', 'vaultID__poolCount', 'vaultID__protocolFeesCollector', 'vaultID__totalLiquidity', 'vaultID__totalProtocolFee', 'vaultID__totalSwapCount', 'vaultID__totalSwapFee', 'vaultID__totalSwapVolume', 'w', 'weightUpdates', 'wrappedIndex', 'z')


class PriceRateProvider_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'cacheDuration', 'cacheExpiry', 'id', 'lastCached', 'poolId', 'poolId__address', 'poolId__alpha', 'poolId__amp', 'poolId__baseToken', 'poolId__beta', 'poolId__c', 'poolId__createTime', 'poolId__dSq', 'poolId__delta', 'poolId__epsilon', 'poolId__expiryTime', 'poolId__factory', 'poolId__holdersCount', 'poolId__id', 'poolId__isInRecoveryMode', 'poolId__isPaused', 'poolId__joinExitEnabled', 'poolId__lambda', 'poolId__lastJoinExitAmp', 'poolId__lastPostJoinExitInvariant', 'poolId__lowerTarget', 'poolId__mainIndex', 'poolId__managementAumFee', 'poolId__managementFee', 'poolId__mustAllowlistLPs', 'poolId__name', 'poolId__oracleEnabled', 'poolId__owner', 'poolId__poolType', 'poolId__poolTypeVersion', 'poolId__principalToken', 'poolId__protocolAumFeeCache', 'poolId__protocolId', 'poolId__protocolSwapFeeCache', 'poolId__protocolYieldFeeCache', 'poolId__root3Alpha', 'poolId__s', 'poolId__sqrtAlpha', 'poolId__sqrtBeta', 'poolId__strategyType', 'poolId__swapEnabled', 'poolId__swapEnabledCurationSignal', 'poolId__swapEnabledInternal', 'poolId__swapFee', 'poolId__swapsCount', 'poolId__symbol', 'poolId__tauAlphaX', 'poolId__tauAlphaY', 'poolId__tauBetaX', 'poolId__tauBetaY', 'poolId__totalAumFeeCollectedInBPT', 'poolId__totalLiquidity', 'poolId__totalLiquiditySansBPT', 'poolId__totalProtocolFee', 'poolId__totalProtocolFeePaidInBPT', 'poolId__totalShares', 'poolId__totalSwapFee', 'poolId__totalSwapVolume', 'poolId__totalWeight', 'poolId__tx', 'poolId__u', 'poolId__unitSeconds', 'poolId__upperTarget', 'poolId__v', 'poolId__w', 'poolId__wrappedIndex', 'poolId__z', 'rate', 'token', 'token__address', 'token__assetManager', 'token__balance', 'token__cashBalance', 'token__decimals', 'token__id', 'token__index', 'token__isExemptFromYieldProtocolFee', 'token__managedBalance', 'token__name', 'token__oldPriceRate', 'token__paidProtocolFees', 'token__priceRate', 'token__symbol', 'token__weight')


class ProtocolIdData_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'name')


String = sgqlc.types.String

class SwapFeeUpdate_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('endSwapFeePercentage', 'endTimestamp', 'id', 'pool', 'pool__address', 'pool__alpha', 'pool__amp', 'pool__baseToken', 'pool__beta', 'pool__c', 'pool__createTime', 'pool__dSq', 'pool__delta', 'pool__epsilon', 'pool__expiryTime', 'pool__factory', 'pool__holdersCount', 'pool__id', 'pool__isInRecoveryMode', 'pool__isPaused', 'pool__joinExitEnabled', 'pool__lambda', 'pool__lastJoinExitAmp', 'pool__lastPostJoinExitInvariant', 'pool__lowerTarget', 'pool__mainIndex', 'pool__managementAumFee', 'pool__managementFee', 'pool__mustAllowlistLPs', 'pool__name', 'pool__oracleEnabled', 'pool__owner', 'pool__poolType', 'pool__poolTypeVersion', 'pool__principalToken', 'pool__protocolAumFeeCache', 'pool__protocolId', 'pool__protocolSwapFeeCache', 'pool__protocolYieldFeeCache', 'pool__root3Alpha', 'pool__s', 'pool__sqrtAlpha', 'pool__sqrtBeta', 'pool__strategyType', 'pool__swapEnabled', 'pool__swapEnabledCurationSignal', 'pool__swapEnabledInternal', 'pool__swapFee', 'pool__swapsCount', 'pool__symbol', 'pool__tauAlphaX', 'pool__tauAlphaY', 'pool__tauBetaX', 'pool__tauBetaY', 'pool__totalAumFeeCollectedInBPT', 'pool__totalLiquidity', 'pool__totalLiquiditySansBPT', 'pool__totalProtocolFee', 'pool__totalProtocolFeePaidInBPT', 'pool__totalShares', 'pool__totalSwapFee', 'pool__totalSwapVolume', 'pool__totalWeight', 'pool__tx', 'pool__u', 'pool__unitSeconds', 'pool__upperTarget', 'pool__v', 'pool__w', 'pool__wrappedIndex', 'pool__z', 'scheduledTimestamp', 'startSwapFeePercentage', 'startTimestamp')


class Swap_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('block', 'caller', 'id', 'poolId', 'poolId__address', 'poolId__alpha', 'poolId__amp', 'poolId__baseToken', 'poolId__beta', 'poolId__c', 'poolId__createTime', 'poolId__dSq', 'poolId__delta', 'poolId__epsilon', 'poolId__expiryTime', 'poolId__factory', 'poolId__holdersCount', 'poolId__id', 'poolId__isInRecoveryMode', 'poolId__isPaused', 'poolId__joinExitEnabled', 'poolId__lambda', 'poolId__lastJoinExitAmp', 'poolId__lastPostJoinExitInvariant', 'poolId__lowerTarget', 'poolId__mainIndex', 'poolId__managementAumFee', 'poolId__managementFee', 'poolId__mustAllowlistLPs', 'poolId__name', 'poolId__oracleEnabled', 'poolId__owner', 'poolId__poolType', 'poolId__poolTypeVersion', 'poolId__principalToken', 'poolId__protocolAumFeeCache', 'poolId__protocolId', 'poolId__protocolSwapFeeCache', 'poolId__protocolYieldFeeCache', 'poolId__root3Alpha', 'poolId__s', 'poolId__sqrtAlpha', 'poolId__sqrtBeta', 'poolId__strategyType', 'poolId__swapEnabled', 'poolId__swapEnabledCurationSignal', 'poolId__swapEnabledInternal', 'poolId__swapFee', 'poolId__swapsCount', 'poolId__symbol', 'poolId__tauAlphaX', 'poolId__tauAlphaY', 'poolId__tauBetaX', 'poolId__tauBetaY', 'poolId__totalAumFeeCollectedInBPT', 'poolId__totalLiquidity', 'poolId__totalLiquiditySansBPT', 'poolId__totalProtocolFee', 'poolId__totalProtocolFeePaidInBPT', 'poolId__totalShares', 'poolId__totalSwapFee', 'poolId__totalSwapVolume', 'poolId__totalWeight', 'poolId__tx', 'poolId__u', 'poolId__unitSeconds', 'poolId__upperTarget', 'poolId__v', 'poolId__w', 'poolId__wrappedIndex', 'poolId__z', 'timestamp', 'tokenAmountIn', 'tokenAmountOut', 'tokenIn', 'tokenInSym', 'tokenOut', 'tokenOutSym', 'tx', 'userAddress', 'userAddress__id', 'valueUSD')


class TokenPrice_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('amount', 'asset', 'block', 'id', 'poolId', 'poolId__address', 'poolId__alpha', 'poolId__amp', 'poolId__baseToken', 'poolId__beta', 'poolId__c', 'poolId__createTime', 'poolId__dSq', 'poolId__delta', 'poolId__epsilon', 'poolId__expiryTime', 'poolId__factory', 'poolId__holdersCount', 'poolId__id', 'poolId__isInRecoveryMode', 'poolId__isPaused', 'poolId__joinExitEnabled', 'poolId__lambda', 'poolId__lastJoinExitAmp', 'poolId__lastPostJoinExitInvariant', 'poolId__lowerTarget', 'poolId__mainIndex', 'poolId__managementAumFee', 'poolId__managementFee', 'poolId__mustAllowlistLPs', 'poolId__name', 'poolId__oracleEnabled', 'poolId__owner', 'poolId__poolType', 'poolId__poolTypeVersion', 'poolId__principalToken', 'poolId__protocolAumFeeCache', 'poolId__protocolId', 'poolId__protocolSwapFeeCache', 'poolId__protocolYieldFeeCache', 'poolId__root3Alpha', 'poolId__s', 'poolId__sqrtAlpha', 'poolId__sqrtBeta', 'poolId__strategyType', 'poolId__swapEnabled', 'poolId__swapEnabledCurationSignal', 'poolId__swapEnabledInternal', 'poolId__swapFee', 'poolId__swapsCount', 'poolId__symbol', 'poolId__tauAlphaX', 'poolId__tauAlphaY', 'poolId__tauBetaX', 'poolId__tauBetaY', 'poolId__totalAumFeeCollectedInBPT', 'poolId__totalLiquidity', 'poolId__totalLiquiditySansBPT', 'poolId__totalProtocolFee', 'poolId__totalProtocolFeePaidInBPT', 'poolId__totalShares', 'poolId__totalSwapFee', 'poolId__totalSwapVolume', 'poolId__totalWeight', 'poolId__tx', 'poolId__u', 'poolId__unitSeconds', 'poolId__upperTarget', 'poolId__v', 'poolId__w', 'poolId__wrappedIndex', 'poolId__z', 'price', 'pricingAsset', 'timestamp')


class TokenSnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'timestamp', 'token', 'token__address', 'token__decimals', 'token__fxOracleDecimals', 'token__id', 'token__latestFXPrice', 'token__latestUSDPrice', 'token__latestUSDPriceTimestamp', 'token__name', 'token__symbol', 'token__totalBalanceNotional', 'token__totalBalanceUSD', 'token__totalSwapCount', 'token__totalVolumeNotional', 'token__totalVolumeUSD', 'totalBalanceNotional', 'totalBalanceUSD', 'totalSwapCount', 'totalVolumeNotional', 'totalVolumeUSD')


class Token_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('address', 'decimals', 'fxOracleDecimals', 'id', 'latestFXPrice', 'latestPrice', 'latestPrice__asset', 'latestPrice__block', 'latestPrice__id', 'latestPrice__price', 'latestPrice__pricingAsset', 'latestUSDPrice', 'latestUSDPriceTimestamp', 'name', 'pool', 'pool__address', 'pool__alpha', 'pool__amp', 'pool__baseToken', 'pool__beta', 'pool__c', 'pool__createTime', 'pool__dSq', 'pool__delta', 'pool__epsilon', 'pool__expiryTime', 'pool__factory', 'pool__holdersCount', 'pool__id', 'pool__isInRecoveryMode', 'pool__isPaused', 'pool__joinExitEnabled', 'pool__lambda', 'pool__lastJoinExitAmp', 'pool__lastPostJoinExitInvariant', 'pool__lowerTarget', 'pool__mainIndex', 'pool__managementAumFee', 'pool__managementFee', 'pool__mustAllowlistLPs', 'pool__name', 'pool__oracleEnabled', 'pool__owner', 'pool__poolType', 'pool__poolTypeVersion', 'pool__principalToken', 'pool__protocolAumFeeCache', 'pool__protocolId', 'pool__protocolSwapFeeCache', 'pool__protocolYieldFeeCache', 'pool__root3Alpha', 'pool__s', 'pool__sqrtAlpha', 'pool__sqrtBeta', 'pool__strategyType', 'pool__swapEnabled', 'pool__swapEnabledCurationSignal', 'pool__swapEnabledInternal', 'pool__swapFee', 'pool__swapsCount', 'pool__symbol', 'pool__tauAlphaX', 'pool__tauAlphaY', 'pool__tauBetaX', 'pool__tauBetaY', 'pool__totalAumFeeCollectedInBPT', 'pool__totalLiquidity', 'pool__totalLiquiditySansBPT', 'pool__totalProtocolFee', 'pool__totalProtocolFeePaidInBPT', 'pool__totalShares', 'pool__totalSwapFee', 'pool__totalSwapVolume', 'pool__totalWeight', 'pool__tx', 'pool__u', 'pool__unitSeconds', 'pool__upperTarget', 'pool__v', 'pool__w', 'pool__wrappedIndex', 'pool__z', 'symbol', 'totalBalanceNotional', 'totalBalanceUSD', 'totalSwapCount', 'totalVolumeNotional', 'totalVolumeUSD')


class TradePairSnapshot_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'pair', 'pair__id', 'pair__totalSwapFee', 'pair__totalSwapVolume', 'timestamp', 'totalSwapFee', 'totalSwapVolume')


class TradePair_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'token0', 'token0__address', 'token0__decimals', 'token0__fxOracleDecimals', 'token0__id', 'token0__latestFXPrice', 'token0__latestUSDPrice', 'token0__latestUSDPriceTimestamp', 'token0__name', 'token0__symbol', 'token0__totalBalanceNotional', 'token0__totalBalanceUSD', 'token0__totalSwapCount', 'token0__totalVolumeNotional', 'token0__totalVolumeUSD', 'token1', 'token1__address', 'token1__decimals', 'token1__fxOracleDecimals', 'token1__id', 'token1__latestFXPrice', 'token1__latestUSDPrice', 'token1__latestUSDPriceTimestamp', 'token1__name', 'token1__symbol', 'token1__totalBalanceNotional', 'token1__totalBalanceUSD', 'token1__totalSwapCount', 'token1__totalVolumeNotional', 'token1__totalVolumeUSD', 'totalSwapFee', 'totalSwapVolume')


class UserInternalBalance_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('balance', 'id', 'token', 'tokenInfo', 'tokenInfo__address', 'tokenInfo__decimals', 'tokenInfo__fxOracleDecimals', 'tokenInfo__id', 'tokenInfo__latestFXPrice', 'tokenInfo__latestUSDPrice', 'tokenInfo__latestUSDPriceTimestamp', 'tokenInfo__name', 'tokenInfo__symbol', 'tokenInfo__totalBalanceNotional', 'tokenInfo__totalBalanceUSD', 'tokenInfo__totalSwapCount', 'tokenInfo__totalVolumeNotional', 'tokenInfo__totalVolumeUSD', 'userAddress', 'userAddress__id')


class User_orderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('id', 'sharesOwned', 'swaps', 'userInternalBalances')


class _SubgraphErrorPolicy_(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('allow', 'deny')



########################################################################
# Input Objects
########################################################################
class AmpUpdate_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_id', 'pool_id_not', 'pool_id_gt', 'pool_id_lt', 'pool_id_gte', 'pool_id_lte', 'pool_id_in', 'pool_id_not_in', 'pool_id_contains', 'pool_id_contains_nocase', 'pool_id_not_contains', 'pool_id_not_contains_nocase', 'pool_id_starts_with', 'pool_id_starts_with_nocase', 'pool_id_not_starts_with', 'pool_id_not_starts_with_nocase', 'pool_id_ends_with', 'pool_id_ends_with_nocase', 'pool_id_not_ends_with', 'pool_id_not_ends_with_nocase', 'pool_id_', 'scheduled_timestamp', 'scheduled_timestamp_not', 'scheduled_timestamp_gt', 'scheduled_timestamp_lt', 'scheduled_timestamp_gte', 'scheduled_timestamp_lte', 'scheduled_timestamp_in', 'scheduled_timestamp_not_in', 'start_timestamp', 'start_timestamp_not', 'start_timestamp_gt', 'start_timestamp_lt', 'start_timestamp_gte', 'start_timestamp_lte', 'start_timestamp_in', 'start_timestamp_not_in', 'end_timestamp', 'end_timestamp_not', 'end_timestamp_gt', 'end_timestamp_lt', 'end_timestamp_gte', 'end_timestamp_lte', 'end_timestamp_in', 'end_timestamp_not_in', 'start_amp', 'start_amp_not', 'start_amp_gt', 'start_amp_lt', 'start_amp_gte', 'start_amp_lte', 'start_amp_in', 'start_amp_not_in', 'end_amp', 'end_amp_not', 'end_amp_gt', 'end_amp_lt', 'end_amp_gte', 'end_amp_lte', 'end_amp_in', 'end_amp_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool_id = sgqlc.types.Field(String, graphql_name='poolId')
    pool_id_not = sgqlc.types.Field(String, graphql_name='poolId_not')
    pool_id_gt = sgqlc.types.Field(String, graphql_name='poolId_gt')
    pool_id_lt = sgqlc.types.Field(String, graphql_name='poolId_lt')
    pool_id_gte = sgqlc.types.Field(String, graphql_name='poolId_gte')
    pool_id_lte = sgqlc.types.Field(String, graphql_name='poolId_lte')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_in')
    pool_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_not_in')
    pool_id_contains = sgqlc.types.Field(String, graphql_name='poolId_contains')
    pool_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_contains_nocase')
    pool_id_not_contains = sgqlc.types.Field(String, graphql_name='poolId_not_contains')
    pool_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_contains_nocase')
    pool_id_starts_with = sgqlc.types.Field(String, graphql_name='poolId_starts_with')
    pool_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_starts_with_nocase')
    pool_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with')
    pool_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with_nocase')
    pool_id_ends_with = sgqlc.types.Field(String, graphql_name='poolId_ends_with')
    pool_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_ends_with_nocase')
    pool_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with')
    pool_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with_nocase')
    pool_id_ = sgqlc.types.Field('Pool_filter', graphql_name='poolId_')
    scheduled_timestamp = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp')
    scheduled_timestamp_not = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_not')
    scheduled_timestamp_gt = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_gt')
    scheduled_timestamp_lt = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_lt')
    scheduled_timestamp_gte = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_gte')
    scheduled_timestamp_lte = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_lte')
    scheduled_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='scheduledTimestamp_in')
    scheduled_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='scheduledTimestamp_not_in')
    start_timestamp = sgqlc.types.Field(BigInt, graphql_name='startTimestamp')
    start_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_not')
    start_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_gt')
    start_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_lt')
    start_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_gte')
    start_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_lte')
    start_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startTimestamp_in')
    start_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startTimestamp_not_in')
    end_timestamp = sgqlc.types.Field(BigInt, graphql_name='endTimestamp')
    end_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_not')
    end_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_gt')
    end_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_lt')
    end_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_gte')
    end_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_lte')
    end_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endTimestamp_in')
    end_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endTimestamp_not_in')
    start_amp = sgqlc.types.Field(BigInt, graphql_name='startAmp')
    start_amp_not = sgqlc.types.Field(BigInt, graphql_name='startAmp_not')
    start_amp_gt = sgqlc.types.Field(BigInt, graphql_name='startAmp_gt')
    start_amp_lt = sgqlc.types.Field(BigInt, graphql_name='startAmp_lt')
    start_amp_gte = sgqlc.types.Field(BigInt, graphql_name='startAmp_gte')
    start_amp_lte = sgqlc.types.Field(BigInt, graphql_name='startAmp_lte')
    start_amp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startAmp_in')
    start_amp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startAmp_not_in')
    end_amp = sgqlc.types.Field(BigInt, graphql_name='endAmp')
    end_amp_not = sgqlc.types.Field(BigInt, graphql_name='endAmp_not')
    end_amp_gt = sgqlc.types.Field(BigInt, graphql_name='endAmp_gt')
    end_amp_lt = sgqlc.types.Field(BigInt, graphql_name='endAmp_lt')
    end_amp_gte = sgqlc.types.Field(BigInt, graphql_name='endAmp_gte')
    end_amp_lte = sgqlc.types.Field(BigInt, graphql_name='endAmp_lte')
    end_amp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endAmp_in')
    end_amp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endAmp_not_in')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('AmpUpdate_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('AmpUpdate_filter'), graphql_name='or')


class BalancerSnapshot_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'vault', 'vault_not', 'vault_gt', 'vault_lt', 'vault_gte', 'vault_lte', 'vault_in', 'vault_not_in', 'vault_contains', 'vault_contains_nocase', 'vault_not_contains', 'vault_not_contains_nocase', 'vault_starts_with', 'vault_starts_with_nocase', 'vault_not_starts_with', 'vault_not_starts_with_nocase', 'vault_ends_with', 'vault_ends_with_nocase', 'vault_not_ends_with', 'vault_not_ends_with_nocase', 'vault_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'pool_count', 'pool_count_not', 'pool_count_gt', 'pool_count_lt', 'pool_count_gte', 'pool_count_lte', 'pool_count_in', 'pool_count_not_in', 'total_liquidity', 'total_liquidity_not', 'total_liquidity_gt', 'total_liquidity_lt', 'total_liquidity_gte', 'total_liquidity_lte', 'total_liquidity_in', 'total_liquidity_not_in', 'total_swap_count', 'total_swap_count_not', 'total_swap_count_gt', 'total_swap_count_lt', 'total_swap_count_gte', 'total_swap_count_lte', 'total_swap_count_in', 'total_swap_count_not_in', 'total_swap_volume', 'total_swap_volume_not', 'total_swap_volume_gt', 'total_swap_volume_lt', 'total_swap_volume_gte', 'total_swap_volume_lte', 'total_swap_volume_in', 'total_swap_volume_not_in', 'total_swap_fee', 'total_swap_fee_not', 'total_swap_fee_gt', 'total_swap_fee_lt', 'total_swap_fee_gte', 'total_swap_fee_lte', 'total_swap_fee_in', 'total_swap_fee_not_in', 'total_protocol_fee', 'total_protocol_fee_not', 'total_protocol_fee_gt', 'total_protocol_fee_lt', 'total_protocol_fee_gte', 'total_protocol_fee_lte', 'total_protocol_fee_in', 'total_protocol_fee_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    vault = sgqlc.types.Field(String, graphql_name='vault')
    vault_not = sgqlc.types.Field(String, graphql_name='vault_not')
    vault_gt = sgqlc.types.Field(String, graphql_name='vault_gt')
    vault_lt = sgqlc.types.Field(String, graphql_name='vault_lt')
    vault_gte = sgqlc.types.Field(String, graphql_name='vault_gte')
    vault_lte = sgqlc.types.Field(String, graphql_name='vault_lte')
    vault_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='vault_in')
    vault_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='vault_not_in')
    vault_contains = sgqlc.types.Field(String, graphql_name='vault_contains')
    vault_contains_nocase = sgqlc.types.Field(String, graphql_name='vault_contains_nocase')
    vault_not_contains = sgqlc.types.Field(String, graphql_name='vault_not_contains')
    vault_not_contains_nocase = sgqlc.types.Field(String, graphql_name='vault_not_contains_nocase')
    vault_starts_with = sgqlc.types.Field(String, graphql_name='vault_starts_with')
    vault_starts_with_nocase = sgqlc.types.Field(String, graphql_name='vault_starts_with_nocase')
    vault_not_starts_with = sgqlc.types.Field(String, graphql_name='vault_not_starts_with')
    vault_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='vault_not_starts_with_nocase')
    vault_ends_with = sgqlc.types.Field(String, graphql_name='vault_ends_with')
    vault_ends_with_nocase = sgqlc.types.Field(String, graphql_name='vault_ends_with_nocase')
    vault_not_ends_with = sgqlc.types.Field(String, graphql_name='vault_not_ends_with')
    vault_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='vault_not_ends_with_nocase')
    vault_ = sgqlc.types.Field('Balancer_filter', graphql_name='vault_')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(Int, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(Int, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(Int, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(Int, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(Int, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_not_in')
    pool_count = sgqlc.types.Field(Int, graphql_name='poolCount')
    pool_count_not = sgqlc.types.Field(Int, graphql_name='poolCount_not')
    pool_count_gt = sgqlc.types.Field(Int, graphql_name='poolCount_gt')
    pool_count_lt = sgqlc.types.Field(Int, graphql_name='poolCount_lt')
    pool_count_gte = sgqlc.types.Field(Int, graphql_name='poolCount_gte')
    pool_count_lte = sgqlc.types.Field(Int, graphql_name='poolCount_lte')
    pool_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='poolCount_in')
    pool_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='poolCount_not_in')
    total_liquidity = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity')
    total_liquidity_not = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_not')
    total_liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_gt')
    total_liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_lt')
    total_liquidity_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_gte')
    total_liquidity_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_lte')
    total_liquidity_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalLiquidity_in')
    total_liquidity_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalLiquidity_not_in')
    total_swap_count = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount')
    total_swap_count_not = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_not')
    total_swap_count_gt = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_gt')
    total_swap_count_lt = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_lt')
    total_swap_count_gte = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_gte')
    total_swap_count_lte = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_lte')
    total_swap_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSwapCount_in')
    total_swap_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSwapCount_not_in')
    total_swap_volume = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume')
    total_swap_volume_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_not')
    total_swap_volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gt')
    total_swap_volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lt')
    total_swap_volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gte')
    total_swap_volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lte')
    total_swap_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_in')
    total_swap_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_not_in')
    total_swap_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee')
    total_swap_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_not')
    total_swap_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gt')
    total_swap_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lt')
    total_swap_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gte')
    total_swap_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lte')
    total_swap_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_in')
    total_swap_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_not_in')
    total_protocol_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee')
    total_protocol_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_not')
    total_protocol_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_gt')
    total_protocol_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_lt')
    total_protocol_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_gte')
    total_protocol_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_lte')
    total_protocol_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalProtocolFee_in')
    total_protocol_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalProtocolFee_not_in')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('BalancerSnapshot_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('BalancerSnapshot_filter'), graphql_name='or')


class Balancer_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_count', 'pool_count_not', 'pool_count_gt', 'pool_count_lt', 'pool_count_gte', 'pool_count_lte', 'pool_count_in', 'pool_count_not_in', 'pools_', 'snapshots_', 'total_liquidity', 'total_liquidity_not', 'total_liquidity_gt', 'total_liquidity_lt', 'total_liquidity_gte', 'total_liquidity_lte', 'total_liquidity_in', 'total_liquidity_not_in', 'total_swap_count', 'total_swap_count_not', 'total_swap_count_gt', 'total_swap_count_lt', 'total_swap_count_gte', 'total_swap_count_lte', 'total_swap_count_in', 'total_swap_count_not_in', 'total_swap_volume', 'total_swap_volume_not', 'total_swap_volume_gt', 'total_swap_volume_lt', 'total_swap_volume_gte', 'total_swap_volume_lte', 'total_swap_volume_in', 'total_swap_volume_not_in', 'total_swap_fee', 'total_swap_fee_not', 'total_swap_fee_gt', 'total_swap_fee_lt', 'total_swap_fee_gte', 'total_swap_fee_lte', 'total_swap_fee_in', 'total_swap_fee_not_in', 'total_protocol_fee', 'total_protocol_fee_not', 'total_protocol_fee_gt', 'total_protocol_fee_lt', 'total_protocol_fee_gte', 'total_protocol_fee_lte', 'total_protocol_fee_in', 'total_protocol_fee_not_in', 'protocol_fees_collector', 'protocol_fees_collector_not', 'protocol_fees_collector_gt', 'protocol_fees_collector_lt', 'protocol_fees_collector_gte', 'protocol_fees_collector_lte', 'protocol_fees_collector_in', 'protocol_fees_collector_not_in', 'protocol_fees_collector_contains', 'protocol_fees_collector_not_contains', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool_count = sgqlc.types.Field(Int, graphql_name='poolCount')
    pool_count_not = sgqlc.types.Field(Int, graphql_name='poolCount_not')
    pool_count_gt = sgqlc.types.Field(Int, graphql_name='poolCount_gt')
    pool_count_lt = sgqlc.types.Field(Int, graphql_name='poolCount_lt')
    pool_count_gte = sgqlc.types.Field(Int, graphql_name='poolCount_gte')
    pool_count_lte = sgqlc.types.Field(Int, graphql_name='poolCount_lte')
    pool_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='poolCount_in')
    pool_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='poolCount_not_in')
    pools_ = sgqlc.types.Field('Pool_filter', graphql_name='pools_')
    snapshots_ = sgqlc.types.Field(BalancerSnapshot_filter, graphql_name='snapshots_')
    total_liquidity = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity')
    total_liquidity_not = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_not')
    total_liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_gt')
    total_liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_lt')
    total_liquidity_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_gte')
    total_liquidity_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_lte')
    total_liquidity_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalLiquidity_in')
    total_liquidity_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalLiquidity_not_in')
    total_swap_count = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount')
    total_swap_count_not = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_not')
    total_swap_count_gt = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_gt')
    total_swap_count_lt = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_lt')
    total_swap_count_gte = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_gte')
    total_swap_count_lte = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_lte')
    total_swap_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSwapCount_in')
    total_swap_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSwapCount_not_in')
    total_swap_volume = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume')
    total_swap_volume_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_not')
    total_swap_volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gt')
    total_swap_volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lt')
    total_swap_volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gte')
    total_swap_volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lte')
    total_swap_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_in')
    total_swap_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_not_in')
    total_swap_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee')
    total_swap_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_not')
    total_swap_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gt')
    total_swap_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lt')
    total_swap_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gte')
    total_swap_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lte')
    total_swap_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_in')
    total_swap_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_not_in')
    total_protocol_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee')
    total_protocol_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_not')
    total_protocol_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_gt')
    total_protocol_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_lt')
    total_protocol_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_gte')
    total_protocol_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_lte')
    total_protocol_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalProtocolFee_in')
    total_protocol_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalProtocolFee_not_in')
    protocol_fees_collector = sgqlc.types.Field(Bytes, graphql_name='protocolFeesCollector')
    protocol_fees_collector_not = sgqlc.types.Field(Bytes, graphql_name='protocolFeesCollector_not')
    protocol_fees_collector_gt = sgqlc.types.Field(Bytes, graphql_name='protocolFeesCollector_gt')
    protocol_fees_collector_lt = sgqlc.types.Field(Bytes, graphql_name='protocolFeesCollector_lt')
    protocol_fees_collector_gte = sgqlc.types.Field(Bytes, graphql_name='protocolFeesCollector_gte')
    protocol_fees_collector_lte = sgqlc.types.Field(Bytes, graphql_name='protocolFeesCollector_lte')
    protocol_fees_collector_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='protocolFeesCollector_in')
    protocol_fees_collector_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='protocolFeesCollector_not_in')
    protocol_fees_collector_contains = sgqlc.types.Field(Bytes, graphql_name='protocolFeesCollector_contains')
    protocol_fees_collector_not_contains = sgqlc.types.Field(Bytes, graphql_name='protocolFeesCollector_not_contains')
    _change_block = sgqlc.types.Field('BlockChangedFilter', graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Balancer_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Balancer_filter'), graphql_name='or')


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


class CircuitBreaker_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'token_', 'bpt_price', 'bpt_price_not', 'bpt_price_gt', 'bpt_price_lt', 'bpt_price_gte', 'bpt_price_lte', 'bpt_price_in', 'bpt_price_not_in', 'lower_bound_percentage', 'lower_bound_percentage_not', 'lower_bound_percentage_gt', 'lower_bound_percentage_lt', 'lower_bound_percentage_gte', 'lower_bound_percentage_lte', 'lower_bound_percentage_in', 'lower_bound_percentage_not_in', 'upper_bound_percentage', 'upper_bound_percentage_not', 'upper_bound_percentage_gt', 'upper_bound_percentage_lt', 'upper_bound_percentage_gte', 'upper_bound_percentage_lte', 'upper_bound_percentage_in', 'upper_bound_percentage_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
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
    token_ = sgqlc.types.Field('PoolToken_filter', graphql_name='token_')
    bpt_price = sgqlc.types.Field(BigDecimal, graphql_name='bptPrice')
    bpt_price_not = sgqlc.types.Field(BigDecimal, graphql_name='bptPrice_not')
    bpt_price_gt = sgqlc.types.Field(BigDecimal, graphql_name='bptPrice_gt')
    bpt_price_lt = sgqlc.types.Field(BigDecimal, graphql_name='bptPrice_lt')
    bpt_price_gte = sgqlc.types.Field(BigDecimal, graphql_name='bptPrice_gte')
    bpt_price_lte = sgqlc.types.Field(BigDecimal, graphql_name='bptPrice_lte')
    bpt_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='bptPrice_in')
    bpt_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='bptPrice_not_in')
    lower_bound_percentage = sgqlc.types.Field(BigDecimal, graphql_name='lowerBoundPercentage')
    lower_bound_percentage_not = sgqlc.types.Field(BigDecimal, graphql_name='lowerBoundPercentage_not')
    lower_bound_percentage_gt = sgqlc.types.Field(BigDecimal, graphql_name='lowerBoundPercentage_gt')
    lower_bound_percentage_lt = sgqlc.types.Field(BigDecimal, graphql_name='lowerBoundPercentage_lt')
    lower_bound_percentage_gte = sgqlc.types.Field(BigDecimal, graphql_name='lowerBoundPercentage_gte')
    lower_bound_percentage_lte = sgqlc.types.Field(BigDecimal, graphql_name='lowerBoundPercentage_lte')
    lower_bound_percentage_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lowerBoundPercentage_in')
    lower_bound_percentage_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lowerBoundPercentage_not_in')
    upper_bound_percentage = sgqlc.types.Field(BigDecimal, graphql_name='upperBoundPercentage')
    upper_bound_percentage_not = sgqlc.types.Field(BigDecimal, graphql_name='upperBoundPercentage_not')
    upper_bound_percentage_gt = sgqlc.types.Field(BigDecimal, graphql_name='upperBoundPercentage_gt')
    upper_bound_percentage_lt = sgqlc.types.Field(BigDecimal, graphql_name='upperBoundPercentage_lt')
    upper_bound_percentage_gte = sgqlc.types.Field(BigDecimal, graphql_name='upperBoundPercentage_gte')
    upper_bound_percentage_lte = sgqlc.types.Field(BigDecimal, graphql_name='upperBoundPercentage_lte')
    upper_bound_percentage_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='upperBoundPercentage_in')
    upper_bound_percentage_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='upperBoundPercentage_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('CircuitBreaker_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('CircuitBreaker_filter'), graphql_name='or')


class FXOracle_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'tokens', 'tokens_not', 'tokens_contains', 'tokens_contains_nocase', 'tokens_not_contains', 'tokens_not_contains_nocase', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokens')
    tokens_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokens_not')
    tokens_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokens_contains')
    tokens_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokens_contains_nocase')
    tokens_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokens_not_contains')
    tokens_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokens_not_contains_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('FXOracle_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('FXOracle_filter'), graphql_name='or')


class GradualWeightUpdate_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_id', 'pool_id_not', 'pool_id_gt', 'pool_id_lt', 'pool_id_gte', 'pool_id_lte', 'pool_id_in', 'pool_id_not_in', 'pool_id_contains', 'pool_id_contains_nocase', 'pool_id_not_contains', 'pool_id_not_contains_nocase', 'pool_id_starts_with', 'pool_id_starts_with_nocase', 'pool_id_not_starts_with', 'pool_id_not_starts_with_nocase', 'pool_id_ends_with', 'pool_id_ends_with_nocase', 'pool_id_not_ends_with', 'pool_id_not_ends_with_nocase', 'pool_id_', 'scheduled_timestamp', 'scheduled_timestamp_not', 'scheduled_timestamp_gt', 'scheduled_timestamp_lt', 'scheduled_timestamp_gte', 'scheduled_timestamp_lte', 'scheduled_timestamp_in', 'scheduled_timestamp_not_in', 'start_timestamp', 'start_timestamp_not', 'start_timestamp_gt', 'start_timestamp_lt', 'start_timestamp_gte', 'start_timestamp_lte', 'start_timestamp_in', 'start_timestamp_not_in', 'end_timestamp', 'end_timestamp_not', 'end_timestamp_gt', 'end_timestamp_lt', 'end_timestamp_gte', 'end_timestamp_lte', 'end_timestamp_in', 'end_timestamp_not_in', 'start_weights', 'start_weights_not', 'start_weights_contains', 'start_weights_contains_nocase', 'start_weights_not_contains', 'start_weights_not_contains_nocase', 'end_weights', 'end_weights_not', 'end_weights_contains', 'end_weights_contains_nocase', 'end_weights_not_contains', 'end_weights_not_contains_nocase', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool_id = sgqlc.types.Field(String, graphql_name='poolId')
    pool_id_not = sgqlc.types.Field(String, graphql_name='poolId_not')
    pool_id_gt = sgqlc.types.Field(String, graphql_name='poolId_gt')
    pool_id_lt = sgqlc.types.Field(String, graphql_name='poolId_lt')
    pool_id_gte = sgqlc.types.Field(String, graphql_name='poolId_gte')
    pool_id_lte = sgqlc.types.Field(String, graphql_name='poolId_lte')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_in')
    pool_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_not_in')
    pool_id_contains = sgqlc.types.Field(String, graphql_name='poolId_contains')
    pool_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_contains_nocase')
    pool_id_not_contains = sgqlc.types.Field(String, graphql_name='poolId_not_contains')
    pool_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_contains_nocase')
    pool_id_starts_with = sgqlc.types.Field(String, graphql_name='poolId_starts_with')
    pool_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_starts_with_nocase')
    pool_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with')
    pool_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with_nocase')
    pool_id_ends_with = sgqlc.types.Field(String, graphql_name='poolId_ends_with')
    pool_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_ends_with_nocase')
    pool_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with')
    pool_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with_nocase')
    pool_id_ = sgqlc.types.Field('Pool_filter', graphql_name='poolId_')
    scheduled_timestamp = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp')
    scheduled_timestamp_not = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_not')
    scheduled_timestamp_gt = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_gt')
    scheduled_timestamp_lt = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_lt')
    scheduled_timestamp_gte = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_gte')
    scheduled_timestamp_lte = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_lte')
    scheduled_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='scheduledTimestamp_in')
    scheduled_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='scheduledTimestamp_not_in')
    start_timestamp = sgqlc.types.Field(BigInt, graphql_name='startTimestamp')
    start_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_not')
    start_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_gt')
    start_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_lt')
    start_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_gte')
    start_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_lte')
    start_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startTimestamp_in')
    start_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startTimestamp_not_in')
    end_timestamp = sgqlc.types.Field(BigInt, graphql_name='endTimestamp')
    end_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_not')
    end_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_gt')
    end_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_lt')
    end_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_gte')
    end_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_lte')
    end_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endTimestamp_in')
    end_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endTimestamp_not_in')
    start_weights = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startWeights')
    start_weights_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startWeights_not')
    start_weights_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startWeights_contains')
    start_weights_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startWeights_contains_nocase')
    start_weights_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startWeights_not_contains')
    start_weights_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startWeights_not_contains_nocase')
    end_weights = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endWeights')
    end_weights_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endWeights_not')
    end_weights_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endWeights_contains')
    end_weights_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endWeights_contains_nocase')
    end_weights_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endWeights_not_contains')
    end_weights_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endWeights_not_contains_nocase')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('GradualWeightUpdate_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('GradualWeightUpdate_filter'), graphql_name='or')


class JoinExit_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'type', 'type_not', 'type_in', 'type_not_in', 'sender', 'sender_not', 'sender_gt', 'sender_lt', 'sender_gte', 'sender_lte', 'sender_in', 'sender_not_in', 'sender_contains', 'sender_not_contains', 'amounts', 'amounts_not', 'amounts_contains', 'amounts_contains_nocase', 'amounts_not_contains', 'amounts_not_contains_nocase', 'value_usd', 'value_usd_not', 'value_usd_gt', 'value_usd_lt', 'value_usd_gte', 'value_usd_lte', 'value_usd_in', 'value_usd_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'user', 'user_not', 'user_gt', 'user_lt', 'user_gte', 'user_lte', 'user_in', 'user_not_in', 'user_contains', 'user_contains_nocase', 'user_not_contains', 'user_not_contains_nocase', 'user_starts_with', 'user_starts_with_nocase', 'user_not_starts_with', 'user_not_starts_with_nocase', 'user_ends_with', 'user_ends_with_nocase', 'user_not_ends_with', 'user_not_ends_with_nocase', 'user_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'tx', 'tx_not', 'tx_gt', 'tx_lt', 'tx_gte', 'tx_lte', 'tx_in', 'tx_not_in', 'tx_contains', 'tx_not_contains', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    type = sgqlc.types.Field(InvestType, graphql_name='type')
    type_not = sgqlc.types.Field(InvestType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(InvestType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(InvestType)), graphql_name='type_not_in')
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
    amounts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts')
    amounts_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_not')
    amounts_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_contains')
    amounts_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_contains_nocase')
    amounts_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_not_contains')
    amounts_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_not_contains_nocase')
    value_usd = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD')
    value_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_not')
    value_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_gt')
    value_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_lt')
    value_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_gte')
    value_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_lte')
    value_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='valueUSD_in')
    value_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='valueUSD_not_in')
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
    user = sgqlc.types.Field(String, graphql_name='user')
    user_not = sgqlc.types.Field(String, graphql_name='user_not')
    user_gt = sgqlc.types.Field(String, graphql_name='user_gt')
    user_lt = sgqlc.types.Field(String, graphql_name='user_lt')
    user_gte = sgqlc.types.Field(String, graphql_name='user_gte')
    user_lte = sgqlc.types.Field(String, graphql_name='user_lte')
    user_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_in')
    user_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='user_not_in')
    user_contains = sgqlc.types.Field(String, graphql_name='user_contains')
    user_contains_nocase = sgqlc.types.Field(String, graphql_name='user_contains_nocase')
    user_not_contains = sgqlc.types.Field(String, graphql_name='user_not_contains')
    user_not_contains_nocase = sgqlc.types.Field(String, graphql_name='user_not_contains_nocase')
    user_starts_with = sgqlc.types.Field(String, graphql_name='user_starts_with')
    user_starts_with_nocase = sgqlc.types.Field(String, graphql_name='user_starts_with_nocase')
    user_not_starts_with = sgqlc.types.Field(String, graphql_name='user_not_starts_with')
    user_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='user_not_starts_with_nocase')
    user_ends_with = sgqlc.types.Field(String, graphql_name='user_ends_with')
    user_ends_with_nocase = sgqlc.types.Field(String, graphql_name='user_ends_with_nocase')
    user_not_ends_with = sgqlc.types.Field(String, graphql_name='user_not_ends_with')
    user_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='user_not_ends_with_nocase')
    user_ = sgqlc.types.Field('User_filter', graphql_name='user_')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(Int, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(Int, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(Int, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(Int, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(Int, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_not_in')
    tx = sgqlc.types.Field(Bytes, graphql_name='tx')
    tx_not = sgqlc.types.Field(Bytes, graphql_name='tx_not')
    tx_gt = sgqlc.types.Field(Bytes, graphql_name='tx_gt')
    tx_lt = sgqlc.types.Field(Bytes, graphql_name='tx_lt')
    tx_gte = sgqlc.types.Field(Bytes, graphql_name='tx_gte')
    tx_lte = sgqlc.types.Field(Bytes, graphql_name='tx_lte')
    tx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tx_in')
    tx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tx_not_in')
    tx_contains = sgqlc.types.Field(Bytes, graphql_name='tx_contains')
    tx_not_contains = sgqlc.types.Field(Bytes, graphql_name='tx_not_contains')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('JoinExit_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('JoinExit_filter'), graphql_name='or')


class LatestPrice_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'asset', 'asset_not', 'asset_gt', 'asset_lt', 'asset_gte', 'asset_lte', 'asset_in', 'asset_not_in', 'asset_contains', 'asset_not_contains', 'pricing_asset', 'pricing_asset_not', 'pricing_asset_gt', 'pricing_asset_lt', 'pricing_asset_gte', 'pricing_asset_lte', 'pricing_asset_in', 'pricing_asset_not_in', 'pricing_asset_contains', 'pricing_asset_not_contains', 'pool_id', 'pool_id_not', 'pool_id_gt', 'pool_id_lt', 'pool_id_gte', 'pool_id_lte', 'pool_id_in', 'pool_id_not_in', 'pool_id_contains', 'pool_id_contains_nocase', 'pool_id_not_contains', 'pool_id_not_contains_nocase', 'pool_id_starts_with', 'pool_id_starts_with_nocase', 'pool_id_not_starts_with', 'pool_id_not_starts_with_nocase', 'pool_id_ends_with', 'pool_id_ends_with_nocase', 'pool_id_not_ends_with', 'pool_id_not_ends_with_nocase', 'pool_id_', 'price', 'price_not', 'price_gt', 'price_lt', 'price_gte', 'price_lte', 'price_in', 'price_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    asset = sgqlc.types.Field(Bytes, graphql_name='asset')
    asset_not = sgqlc.types.Field(Bytes, graphql_name='asset_not')
    asset_gt = sgqlc.types.Field(Bytes, graphql_name='asset_gt')
    asset_lt = sgqlc.types.Field(Bytes, graphql_name='asset_lt')
    asset_gte = sgqlc.types.Field(Bytes, graphql_name='asset_gte')
    asset_lte = sgqlc.types.Field(Bytes, graphql_name='asset_lte')
    asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='asset_in')
    asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='asset_not_in')
    asset_contains = sgqlc.types.Field(Bytes, graphql_name='asset_contains')
    asset_not_contains = sgqlc.types.Field(Bytes, graphql_name='asset_not_contains')
    pricing_asset = sgqlc.types.Field(Bytes, graphql_name='pricingAsset')
    pricing_asset_not = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_not')
    pricing_asset_gt = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_gt')
    pricing_asset_lt = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_lt')
    pricing_asset_gte = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_gte')
    pricing_asset_lte = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_lte')
    pricing_asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='pricingAsset_in')
    pricing_asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='pricingAsset_not_in')
    pricing_asset_contains = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_contains')
    pricing_asset_not_contains = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_not_contains')
    pool_id = sgqlc.types.Field(String, graphql_name='poolId')
    pool_id_not = sgqlc.types.Field(String, graphql_name='poolId_not')
    pool_id_gt = sgqlc.types.Field(String, graphql_name='poolId_gt')
    pool_id_lt = sgqlc.types.Field(String, graphql_name='poolId_lt')
    pool_id_gte = sgqlc.types.Field(String, graphql_name='poolId_gte')
    pool_id_lte = sgqlc.types.Field(String, graphql_name='poolId_lte')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_in')
    pool_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_not_in')
    pool_id_contains = sgqlc.types.Field(String, graphql_name='poolId_contains')
    pool_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_contains_nocase')
    pool_id_not_contains = sgqlc.types.Field(String, graphql_name='poolId_not_contains')
    pool_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_contains_nocase')
    pool_id_starts_with = sgqlc.types.Field(String, graphql_name='poolId_starts_with')
    pool_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_starts_with_nocase')
    pool_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with')
    pool_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with_nocase')
    pool_id_ends_with = sgqlc.types.Field(String, graphql_name='poolId_ends_with')
    pool_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_ends_with_nocase')
    pool_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with')
    pool_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with_nocase')
    pool_id_ = sgqlc.types.Field('Pool_filter', graphql_name='poolId_')
    price = sgqlc.types.Field(BigDecimal, graphql_name='price')
    price_not = sgqlc.types.Field(BigDecimal, graphql_name='price_not')
    price_gt = sgqlc.types.Field(BigDecimal, graphql_name='price_gt')
    price_lt = sgqlc.types.Field(BigDecimal, graphql_name='price_lt')
    price_gte = sgqlc.types.Field(BigDecimal, graphql_name='price_gte')
    price_lte = sgqlc.types.Field(BigDecimal, graphql_name='price_lte')
    price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='price_in')
    price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='price_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('LatestPrice_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('LatestPrice_filter'), graphql_name='or')


class ManagementOperation_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'type', 'type_not', 'type_in', 'type_not_in', 'cash_delta', 'cash_delta_not', 'cash_delta_gt', 'cash_delta_lt', 'cash_delta_gte', 'cash_delta_lte', 'cash_delta_in', 'cash_delta_not_in', 'managed_delta', 'managed_delta_not', 'managed_delta_gt', 'managed_delta_lt', 'managed_delta_gte', 'managed_delta_lte', 'managed_delta_in', 'managed_delta_not_in', 'pool_token_id', 'pool_token_id_not', 'pool_token_id_gt', 'pool_token_id_lt', 'pool_token_id_gte', 'pool_token_id_lte', 'pool_token_id_in', 'pool_token_id_not_in', 'pool_token_id_contains', 'pool_token_id_contains_nocase', 'pool_token_id_not_contains', 'pool_token_id_not_contains_nocase', 'pool_token_id_starts_with', 'pool_token_id_starts_with_nocase', 'pool_token_id_not_starts_with', 'pool_token_id_not_starts_with_nocase', 'pool_token_id_ends_with', 'pool_token_id_ends_with_nocase', 'pool_token_id_not_ends_with', 'pool_token_id_not_ends_with_nocase', 'pool_token_id_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    type = sgqlc.types.Field(OperationType, graphql_name='type')
    type_not = sgqlc.types.Field(OperationType, graphql_name='type_not')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OperationType)), graphql_name='type_in')
    type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OperationType)), graphql_name='type_not_in')
    cash_delta = sgqlc.types.Field(BigDecimal, graphql_name='cashDelta')
    cash_delta_not = sgqlc.types.Field(BigDecimal, graphql_name='cashDelta_not')
    cash_delta_gt = sgqlc.types.Field(BigDecimal, graphql_name='cashDelta_gt')
    cash_delta_lt = sgqlc.types.Field(BigDecimal, graphql_name='cashDelta_lt')
    cash_delta_gte = sgqlc.types.Field(BigDecimal, graphql_name='cashDelta_gte')
    cash_delta_lte = sgqlc.types.Field(BigDecimal, graphql_name='cashDelta_lte')
    cash_delta_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cashDelta_in')
    cash_delta_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cashDelta_not_in')
    managed_delta = sgqlc.types.Field(BigDecimal, graphql_name='managedDelta')
    managed_delta_not = sgqlc.types.Field(BigDecimal, graphql_name='managedDelta_not')
    managed_delta_gt = sgqlc.types.Field(BigDecimal, graphql_name='managedDelta_gt')
    managed_delta_lt = sgqlc.types.Field(BigDecimal, graphql_name='managedDelta_lt')
    managed_delta_gte = sgqlc.types.Field(BigDecimal, graphql_name='managedDelta_gte')
    managed_delta_lte = sgqlc.types.Field(BigDecimal, graphql_name='managedDelta_lte')
    managed_delta_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='managedDelta_in')
    managed_delta_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='managedDelta_not_in')
    pool_token_id = sgqlc.types.Field(String, graphql_name='poolTokenId')
    pool_token_id_not = sgqlc.types.Field(String, graphql_name='poolTokenId_not')
    pool_token_id_gt = sgqlc.types.Field(String, graphql_name='poolTokenId_gt')
    pool_token_id_lt = sgqlc.types.Field(String, graphql_name='poolTokenId_lt')
    pool_token_id_gte = sgqlc.types.Field(String, graphql_name='poolTokenId_gte')
    pool_token_id_lte = sgqlc.types.Field(String, graphql_name='poolTokenId_lte')
    pool_token_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolTokenId_in')
    pool_token_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolTokenId_not_in')
    pool_token_id_contains = sgqlc.types.Field(String, graphql_name='poolTokenId_contains')
    pool_token_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolTokenId_contains_nocase')
    pool_token_id_not_contains = sgqlc.types.Field(String, graphql_name='poolTokenId_not_contains')
    pool_token_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolTokenId_not_contains_nocase')
    pool_token_id_starts_with = sgqlc.types.Field(String, graphql_name='poolTokenId_starts_with')
    pool_token_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolTokenId_starts_with_nocase')
    pool_token_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolTokenId_not_starts_with')
    pool_token_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolTokenId_not_starts_with_nocase')
    pool_token_id_ends_with = sgqlc.types.Field(String, graphql_name='poolTokenId_ends_with')
    pool_token_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolTokenId_ends_with_nocase')
    pool_token_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolTokenId_not_ends_with')
    pool_token_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolTokenId_not_ends_with_nocase')
    pool_token_id_ = sgqlc.types.Field('PoolToken_filter', graphql_name='poolTokenId_')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(Int, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(Int, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(Int, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(Int, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(Int, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('ManagementOperation_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('ManagementOperation_filter'), graphql_name='or')


class PoolContract_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
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
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PoolContract_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PoolContract_filter'), graphql_name='or')


class PoolHistoricalLiquidity_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_id', 'pool_id_not', 'pool_id_gt', 'pool_id_lt', 'pool_id_gte', 'pool_id_lte', 'pool_id_in', 'pool_id_not_in', 'pool_id_contains', 'pool_id_contains_nocase', 'pool_id_not_contains', 'pool_id_not_contains_nocase', 'pool_id_starts_with', 'pool_id_starts_with_nocase', 'pool_id_not_starts_with', 'pool_id_not_starts_with_nocase', 'pool_id_ends_with', 'pool_id_ends_with_nocase', 'pool_id_not_ends_with', 'pool_id_not_ends_with_nocase', 'pool_id_', 'pool_total_shares', 'pool_total_shares_not', 'pool_total_shares_gt', 'pool_total_shares_lt', 'pool_total_shares_gte', 'pool_total_shares_lte', 'pool_total_shares_in', 'pool_total_shares_not_in', 'pool_liquidity', 'pool_liquidity_not', 'pool_liquidity_gt', 'pool_liquidity_lt', 'pool_liquidity_gte', 'pool_liquidity_lte', 'pool_liquidity_in', 'pool_liquidity_not_in', 'pool_share_value', 'pool_share_value_not', 'pool_share_value_gt', 'pool_share_value_lt', 'pool_share_value_gte', 'pool_share_value_lte', 'pool_share_value_in', 'pool_share_value_not_in', 'pricing_asset', 'pricing_asset_not', 'pricing_asset_gt', 'pricing_asset_lt', 'pricing_asset_gte', 'pricing_asset_lte', 'pricing_asset_in', 'pricing_asset_not_in', 'pricing_asset_contains', 'pricing_asset_not_contains', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool_id = sgqlc.types.Field(String, graphql_name='poolId')
    pool_id_not = sgqlc.types.Field(String, graphql_name='poolId_not')
    pool_id_gt = sgqlc.types.Field(String, graphql_name='poolId_gt')
    pool_id_lt = sgqlc.types.Field(String, graphql_name='poolId_lt')
    pool_id_gte = sgqlc.types.Field(String, graphql_name='poolId_gte')
    pool_id_lte = sgqlc.types.Field(String, graphql_name='poolId_lte')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_in')
    pool_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_not_in')
    pool_id_contains = sgqlc.types.Field(String, graphql_name='poolId_contains')
    pool_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_contains_nocase')
    pool_id_not_contains = sgqlc.types.Field(String, graphql_name='poolId_not_contains')
    pool_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_contains_nocase')
    pool_id_starts_with = sgqlc.types.Field(String, graphql_name='poolId_starts_with')
    pool_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_starts_with_nocase')
    pool_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with')
    pool_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with_nocase')
    pool_id_ends_with = sgqlc.types.Field(String, graphql_name='poolId_ends_with')
    pool_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_ends_with_nocase')
    pool_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with')
    pool_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with_nocase')
    pool_id_ = sgqlc.types.Field('Pool_filter', graphql_name='poolId_')
    pool_total_shares = sgqlc.types.Field(BigDecimal, graphql_name='poolTotalShares')
    pool_total_shares_not = sgqlc.types.Field(BigDecimal, graphql_name='poolTotalShares_not')
    pool_total_shares_gt = sgqlc.types.Field(BigDecimal, graphql_name='poolTotalShares_gt')
    pool_total_shares_lt = sgqlc.types.Field(BigDecimal, graphql_name='poolTotalShares_lt')
    pool_total_shares_gte = sgqlc.types.Field(BigDecimal, graphql_name='poolTotalShares_gte')
    pool_total_shares_lte = sgqlc.types.Field(BigDecimal, graphql_name='poolTotalShares_lte')
    pool_total_shares_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='poolTotalShares_in')
    pool_total_shares_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='poolTotalShares_not_in')
    pool_liquidity = sgqlc.types.Field(BigDecimal, graphql_name='poolLiquidity')
    pool_liquidity_not = sgqlc.types.Field(BigDecimal, graphql_name='poolLiquidity_not')
    pool_liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name='poolLiquidity_gt')
    pool_liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name='poolLiquidity_lt')
    pool_liquidity_gte = sgqlc.types.Field(BigDecimal, graphql_name='poolLiquidity_gte')
    pool_liquidity_lte = sgqlc.types.Field(BigDecimal, graphql_name='poolLiquidity_lte')
    pool_liquidity_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='poolLiquidity_in')
    pool_liquidity_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='poolLiquidity_not_in')
    pool_share_value = sgqlc.types.Field(BigDecimal, graphql_name='poolShareValue')
    pool_share_value_not = sgqlc.types.Field(BigDecimal, graphql_name='poolShareValue_not')
    pool_share_value_gt = sgqlc.types.Field(BigDecimal, graphql_name='poolShareValue_gt')
    pool_share_value_lt = sgqlc.types.Field(BigDecimal, graphql_name='poolShareValue_lt')
    pool_share_value_gte = sgqlc.types.Field(BigDecimal, graphql_name='poolShareValue_gte')
    pool_share_value_lte = sgqlc.types.Field(BigDecimal, graphql_name='poolShareValue_lte')
    pool_share_value_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='poolShareValue_in')
    pool_share_value_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='poolShareValue_not_in')
    pricing_asset = sgqlc.types.Field(Bytes, graphql_name='pricingAsset')
    pricing_asset_not = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_not')
    pricing_asset_gt = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_gt')
    pricing_asset_lt = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_lt')
    pricing_asset_gte = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_gte')
    pricing_asset_lte = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_lte')
    pricing_asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='pricingAsset_in')
    pricing_asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='pricingAsset_not_in')
    pricing_asset_contains = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_contains')
    pricing_asset_not_contains = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_not_contains')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PoolHistoricalLiquidity_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PoolHistoricalLiquidity_filter'), graphql_name='or')


class PoolShare_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'user_address', 'user_address_not', 'user_address_gt', 'user_address_lt', 'user_address_gte', 'user_address_lte', 'user_address_in', 'user_address_not_in', 'user_address_contains', 'user_address_contains_nocase', 'user_address_not_contains', 'user_address_not_contains_nocase', 'user_address_starts_with', 'user_address_starts_with_nocase', 'user_address_not_starts_with', 'user_address_not_starts_with_nocase', 'user_address_ends_with', 'user_address_ends_with_nocase', 'user_address_not_ends_with', 'user_address_not_ends_with_nocase', 'user_address_', 'pool_id', 'pool_id_not', 'pool_id_gt', 'pool_id_lt', 'pool_id_gte', 'pool_id_lte', 'pool_id_in', 'pool_id_not_in', 'pool_id_contains', 'pool_id_contains_nocase', 'pool_id_not_contains', 'pool_id_not_contains_nocase', 'pool_id_starts_with', 'pool_id_starts_with_nocase', 'pool_id_not_starts_with', 'pool_id_not_starts_with_nocase', 'pool_id_ends_with', 'pool_id_ends_with_nocase', 'pool_id_not_ends_with', 'pool_id_not_ends_with_nocase', 'pool_id_', 'balance', 'balance_not', 'balance_gt', 'balance_lt', 'balance_gte', 'balance_lte', 'balance_in', 'balance_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    user_address = sgqlc.types.Field(String, graphql_name='userAddress')
    user_address_not = sgqlc.types.Field(String, graphql_name='userAddress_not')
    user_address_gt = sgqlc.types.Field(String, graphql_name='userAddress_gt')
    user_address_lt = sgqlc.types.Field(String, graphql_name='userAddress_lt')
    user_address_gte = sgqlc.types.Field(String, graphql_name='userAddress_gte')
    user_address_lte = sgqlc.types.Field(String, graphql_name='userAddress_lte')
    user_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userAddress_in')
    user_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userAddress_not_in')
    user_address_contains = sgqlc.types.Field(String, graphql_name='userAddress_contains')
    user_address_contains_nocase = sgqlc.types.Field(String, graphql_name='userAddress_contains_nocase')
    user_address_not_contains = sgqlc.types.Field(String, graphql_name='userAddress_not_contains')
    user_address_not_contains_nocase = sgqlc.types.Field(String, graphql_name='userAddress_not_contains_nocase')
    user_address_starts_with = sgqlc.types.Field(String, graphql_name='userAddress_starts_with')
    user_address_starts_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_starts_with_nocase')
    user_address_not_starts_with = sgqlc.types.Field(String, graphql_name='userAddress_not_starts_with')
    user_address_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_not_starts_with_nocase')
    user_address_ends_with = sgqlc.types.Field(String, graphql_name='userAddress_ends_with')
    user_address_ends_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_ends_with_nocase')
    user_address_not_ends_with = sgqlc.types.Field(String, graphql_name='userAddress_not_ends_with')
    user_address_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_not_ends_with_nocase')
    user_address_ = sgqlc.types.Field('User_filter', graphql_name='userAddress_')
    pool_id = sgqlc.types.Field(String, graphql_name='poolId')
    pool_id_not = sgqlc.types.Field(String, graphql_name='poolId_not')
    pool_id_gt = sgqlc.types.Field(String, graphql_name='poolId_gt')
    pool_id_lt = sgqlc.types.Field(String, graphql_name='poolId_lt')
    pool_id_gte = sgqlc.types.Field(String, graphql_name='poolId_gte')
    pool_id_lte = sgqlc.types.Field(String, graphql_name='poolId_lte')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_in')
    pool_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_not_in')
    pool_id_contains = sgqlc.types.Field(String, graphql_name='poolId_contains')
    pool_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_contains_nocase')
    pool_id_not_contains = sgqlc.types.Field(String, graphql_name='poolId_not_contains')
    pool_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_contains_nocase')
    pool_id_starts_with = sgqlc.types.Field(String, graphql_name='poolId_starts_with')
    pool_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_starts_with_nocase')
    pool_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with')
    pool_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with_nocase')
    pool_id_ends_with = sgqlc.types.Field(String, graphql_name='poolId_ends_with')
    pool_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_ends_with_nocase')
    pool_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with')
    pool_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with_nocase')
    pool_id_ = sgqlc.types.Field('Pool_filter', graphql_name='poolId_')
    balance = sgqlc.types.Field(BigDecimal, graphql_name='balance')
    balance_not = sgqlc.types.Field(BigDecimal, graphql_name='balance_not')
    balance_gt = sgqlc.types.Field(BigDecimal, graphql_name='balance_gt')
    balance_lt = sgqlc.types.Field(BigDecimal, graphql_name='balance_lt')
    balance_gte = sgqlc.types.Field(BigDecimal, graphql_name='balance_gte')
    balance_lte = sgqlc.types.Field(BigDecimal, graphql_name='balance_lte')
    balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_in')
    balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PoolShare_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PoolShare_filter'), graphql_name='or')


class PoolSnapshot_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'amounts', 'amounts_not', 'amounts_contains', 'amounts_contains_nocase', 'amounts_not_contains', 'amounts_not_contains_nocase', 'total_shares', 'total_shares_not', 'total_shares_gt', 'total_shares_lt', 'total_shares_gte', 'total_shares_lte', 'total_shares_in', 'total_shares_not_in', 'swap_volume', 'swap_volume_not', 'swap_volume_gt', 'swap_volume_lt', 'swap_volume_gte', 'swap_volume_lte', 'swap_volume_in', 'swap_volume_not_in', 'protocol_fee', 'protocol_fee_not', 'protocol_fee_gt', 'protocol_fee_lt', 'protocol_fee_gte', 'protocol_fee_lte', 'protocol_fee_in', 'protocol_fee_not_in', 'swap_fees', 'swap_fees_not', 'swap_fees_gt', 'swap_fees_lt', 'swap_fees_gte', 'swap_fees_lte', 'swap_fees_in', 'swap_fees_not_in', 'liquidity', 'liquidity_not', 'liquidity_gt', 'liquidity_lt', 'liquidity_gte', 'liquidity_lte', 'liquidity_in', 'liquidity_not_in', 'swaps_count', 'swaps_count_not', 'swaps_count_gt', 'swaps_count_lt', 'swaps_count_gte', 'swaps_count_lte', 'swaps_count_in', 'swaps_count_not_in', 'holders_count', 'holders_count_not', 'holders_count_gt', 'holders_count_lt', 'holders_count_gte', 'holders_count_lte', 'holders_count_in', 'holders_count_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
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
    amounts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts')
    amounts_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_not')
    amounts_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_contains')
    amounts_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_contains_nocase')
    amounts_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_not_contains')
    amounts_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amounts_not_contains_nocase')
    total_shares = sgqlc.types.Field(BigDecimal, graphql_name='totalShares')
    total_shares_not = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_not')
    total_shares_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_gt')
    total_shares_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_lt')
    total_shares_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_gte')
    total_shares_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_lte')
    total_shares_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalShares_in')
    total_shares_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalShares_not_in')
    swap_volume = sgqlc.types.Field(BigDecimal, graphql_name='swapVolume')
    swap_volume_not = sgqlc.types.Field(BigDecimal, graphql_name='swapVolume_not')
    swap_volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='swapVolume_gt')
    swap_volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='swapVolume_lt')
    swap_volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='swapVolume_gte')
    swap_volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='swapVolume_lte')
    swap_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='swapVolume_in')
    swap_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='swapVolume_not_in')
    protocol_fee = sgqlc.types.Field(BigDecimal, graphql_name='protocolFee')
    protocol_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolFee_not')
    protocol_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolFee_gt')
    protocol_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolFee_lt')
    protocol_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolFee_gte')
    protocol_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolFee_lte')
    protocol_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolFee_in')
    protocol_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolFee_not_in')
    swap_fees = sgqlc.types.Field(BigDecimal, graphql_name='swapFees')
    swap_fees_not = sgqlc.types.Field(BigDecimal, graphql_name='swapFees_not')
    swap_fees_gt = sgqlc.types.Field(BigDecimal, graphql_name='swapFees_gt')
    swap_fees_lt = sgqlc.types.Field(BigDecimal, graphql_name='swapFees_lt')
    swap_fees_gte = sgqlc.types.Field(BigDecimal, graphql_name='swapFees_gte')
    swap_fees_lte = sgqlc.types.Field(BigDecimal, graphql_name='swapFees_lte')
    swap_fees_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='swapFees_in')
    swap_fees_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='swapFees_not_in')
    liquidity = sgqlc.types.Field(BigDecimal, graphql_name='liquidity')
    liquidity_not = sgqlc.types.Field(BigDecimal, graphql_name='liquidity_not')
    liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name='liquidity_gt')
    liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name='liquidity_lt')
    liquidity_gte = sgqlc.types.Field(BigDecimal, graphql_name='liquidity_gte')
    liquidity_lte = sgqlc.types.Field(BigDecimal, graphql_name='liquidity_lte')
    liquidity_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='liquidity_in')
    liquidity_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='liquidity_not_in')
    swaps_count = sgqlc.types.Field(BigInt, graphql_name='swapsCount')
    swaps_count_not = sgqlc.types.Field(BigInt, graphql_name='swapsCount_not')
    swaps_count_gt = sgqlc.types.Field(BigInt, graphql_name='swapsCount_gt')
    swaps_count_lt = sgqlc.types.Field(BigInt, graphql_name='swapsCount_lt')
    swaps_count_gte = sgqlc.types.Field(BigInt, graphql_name='swapsCount_gte')
    swaps_count_lte = sgqlc.types.Field(BigInt, graphql_name='swapsCount_lte')
    swaps_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='swapsCount_in')
    swaps_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='swapsCount_not_in')
    holders_count = sgqlc.types.Field(BigInt, graphql_name='holdersCount')
    holders_count_not = sgqlc.types.Field(BigInt, graphql_name='holdersCount_not')
    holders_count_gt = sgqlc.types.Field(BigInt, graphql_name='holdersCount_gt')
    holders_count_lt = sgqlc.types.Field(BigInt, graphql_name='holdersCount_lt')
    holders_count_gte = sgqlc.types.Field(BigInt, graphql_name='holdersCount_gte')
    holders_count_lte = sgqlc.types.Field(BigInt, graphql_name='holdersCount_lte')
    holders_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='holdersCount_in')
    holders_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='holdersCount_not_in')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(Int, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(Int, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(Int, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(Int, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(Int, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PoolSnapshot_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PoolSnapshot_filter'), graphql_name='or')


class PoolToken_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_id', 'pool_id_not', 'pool_id_gt', 'pool_id_lt', 'pool_id_gte', 'pool_id_lte', 'pool_id_in', 'pool_id_not_in', 'pool_id_contains', 'pool_id_contains_nocase', 'pool_id_not_contains', 'pool_id_not_contains_nocase', 'pool_id_starts_with', 'pool_id_starts_with_nocase', 'pool_id_not_starts_with', 'pool_id_not_starts_with_nocase', 'pool_id_ends_with', 'pool_id_ends_with_nocase', 'pool_id_not_ends_with', 'pool_id_not_ends_with_nocase', 'pool_id_', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'token_', 'asset_manager', 'asset_manager_not', 'asset_manager_gt', 'asset_manager_lt', 'asset_manager_gte', 'asset_manager_lte', 'asset_manager_in', 'asset_manager_not_in', 'asset_manager_contains', 'asset_manager_not_contains', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_contains_nocase', 'symbol_not_contains', 'symbol_not_contains_nocase', 'symbol_starts_with', 'symbol_starts_with_nocase', 'symbol_not_starts_with', 'symbol_not_starts_with_nocase', 'symbol_ends_with', 'symbol_ends_with_nocase', 'symbol_not_ends_with', 'symbol_not_ends_with_nocase', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'decimals', 'decimals_not', 'decimals_gt', 'decimals_lt', 'decimals_gte', 'decimals_lte', 'decimals_in', 'decimals_not_in', 'index', 'index_not', 'index_gt', 'index_lt', 'index_gte', 'index_lte', 'index_in', 'index_not_in', 'address', 'address_not', 'address_gt', 'address_lt', 'address_gte', 'address_lte', 'address_in', 'address_not_in', 'address_contains', 'address_contains_nocase', 'address_not_contains', 'address_not_contains_nocase', 'address_starts_with', 'address_starts_with_nocase', 'address_not_starts_with', 'address_not_starts_with_nocase', 'address_ends_with', 'address_ends_with_nocase', 'address_not_ends_with', 'address_not_ends_with_nocase', 'old_price_rate', 'old_price_rate_not', 'old_price_rate_gt', 'old_price_rate_lt', 'old_price_rate_gte', 'old_price_rate_lte', 'old_price_rate_in', 'old_price_rate_not_in', 'price_rate', 'price_rate_not', 'price_rate_gt', 'price_rate_lt', 'price_rate_gte', 'price_rate_lte', 'price_rate_in', 'price_rate_not_in', 'balance', 'balance_not', 'balance_gt', 'balance_lt', 'balance_gte', 'balance_lte', 'balance_in', 'balance_not_in', 'paid_protocol_fees', 'paid_protocol_fees_not', 'paid_protocol_fees_gt', 'paid_protocol_fees_lt', 'paid_protocol_fees_gte', 'paid_protocol_fees_lte', 'paid_protocol_fees_in', 'paid_protocol_fees_not_in', 'cash_balance', 'cash_balance_not', 'cash_balance_gt', 'cash_balance_lt', 'cash_balance_gte', 'cash_balance_lte', 'cash_balance_in', 'cash_balance_not_in', 'managed_balance', 'managed_balance_not', 'managed_balance_gt', 'managed_balance_lt', 'managed_balance_gte', 'managed_balance_lte', 'managed_balance_in', 'managed_balance_not_in', 'managements_', 'weight', 'weight_not', 'weight_gt', 'weight_lt', 'weight_gte', 'weight_lte', 'weight_in', 'weight_not_in', 'is_exempt_from_yield_protocol_fee', 'is_exempt_from_yield_protocol_fee_not', 'is_exempt_from_yield_protocol_fee_in', 'is_exempt_from_yield_protocol_fee_not_in', 'circuit_breaker', 'circuit_breaker_not', 'circuit_breaker_gt', 'circuit_breaker_lt', 'circuit_breaker_gte', 'circuit_breaker_lte', 'circuit_breaker_in', 'circuit_breaker_not_in', 'circuit_breaker_contains', 'circuit_breaker_contains_nocase', 'circuit_breaker_not_contains', 'circuit_breaker_not_contains_nocase', 'circuit_breaker_starts_with', 'circuit_breaker_starts_with_nocase', 'circuit_breaker_not_starts_with', 'circuit_breaker_not_starts_with_nocase', 'circuit_breaker_ends_with', 'circuit_breaker_ends_with_nocase', 'circuit_breaker_not_ends_with', 'circuit_breaker_not_ends_with_nocase', 'circuit_breaker_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool_id = sgqlc.types.Field(String, graphql_name='poolId')
    pool_id_not = sgqlc.types.Field(String, graphql_name='poolId_not')
    pool_id_gt = sgqlc.types.Field(String, graphql_name='poolId_gt')
    pool_id_lt = sgqlc.types.Field(String, graphql_name='poolId_lt')
    pool_id_gte = sgqlc.types.Field(String, graphql_name='poolId_gte')
    pool_id_lte = sgqlc.types.Field(String, graphql_name='poolId_lte')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_in')
    pool_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_not_in')
    pool_id_contains = sgqlc.types.Field(String, graphql_name='poolId_contains')
    pool_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_contains_nocase')
    pool_id_not_contains = sgqlc.types.Field(String, graphql_name='poolId_not_contains')
    pool_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_contains_nocase')
    pool_id_starts_with = sgqlc.types.Field(String, graphql_name='poolId_starts_with')
    pool_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_starts_with_nocase')
    pool_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with')
    pool_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with_nocase')
    pool_id_ends_with = sgqlc.types.Field(String, graphql_name='poolId_ends_with')
    pool_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_ends_with_nocase')
    pool_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with')
    pool_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with_nocase')
    pool_id_ = sgqlc.types.Field('Pool_filter', graphql_name='poolId_')
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
    asset_manager = sgqlc.types.Field(Bytes, graphql_name='assetManager')
    asset_manager_not = sgqlc.types.Field(Bytes, graphql_name='assetManager_not')
    asset_manager_gt = sgqlc.types.Field(Bytes, graphql_name='assetManager_gt')
    asset_manager_lt = sgqlc.types.Field(Bytes, graphql_name='assetManager_lt')
    asset_manager_gte = sgqlc.types.Field(Bytes, graphql_name='assetManager_gte')
    asset_manager_lte = sgqlc.types.Field(Bytes, graphql_name='assetManager_lte')
    asset_manager_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='assetManager_in')
    asset_manager_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='assetManager_not_in')
    asset_manager_contains = sgqlc.types.Field(Bytes, graphql_name='assetManager_contains')
    asset_manager_not_contains = sgqlc.types.Field(Bytes, graphql_name='assetManager_not_contains')
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
    decimals = sgqlc.types.Field(Int, graphql_name='decimals')
    decimals_not = sgqlc.types.Field(Int, graphql_name='decimals_not')
    decimals_gt = sgqlc.types.Field(Int, graphql_name='decimals_gt')
    decimals_lt = sgqlc.types.Field(Int, graphql_name='decimals_lt')
    decimals_gte = sgqlc.types.Field(Int, graphql_name='decimals_gte')
    decimals_lte = sgqlc.types.Field(Int, graphql_name='decimals_lte')
    decimals_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='decimals_in')
    decimals_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='decimals_not_in')
    index = sgqlc.types.Field(Int, graphql_name='index')
    index_not = sgqlc.types.Field(Int, graphql_name='index_not')
    index_gt = sgqlc.types.Field(Int, graphql_name='index_gt')
    index_lt = sgqlc.types.Field(Int, graphql_name='index_lt')
    index_gte = sgqlc.types.Field(Int, graphql_name='index_gte')
    index_lte = sgqlc.types.Field(Int, graphql_name='index_lte')
    index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='index_in')
    index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='index_not_in')
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
    old_price_rate = sgqlc.types.Field(BigDecimal, graphql_name='oldPriceRate')
    old_price_rate_not = sgqlc.types.Field(BigDecimal, graphql_name='oldPriceRate_not')
    old_price_rate_gt = sgqlc.types.Field(BigDecimal, graphql_name='oldPriceRate_gt')
    old_price_rate_lt = sgqlc.types.Field(BigDecimal, graphql_name='oldPriceRate_lt')
    old_price_rate_gte = sgqlc.types.Field(BigDecimal, graphql_name='oldPriceRate_gte')
    old_price_rate_lte = sgqlc.types.Field(BigDecimal, graphql_name='oldPriceRate_lte')
    old_price_rate_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='oldPriceRate_in')
    old_price_rate_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='oldPriceRate_not_in')
    price_rate = sgqlc.types.Field(BigDecimal, graphql_name='priceRate')
    price_rate_not = sgqlc.types.Field(BigDecimal, graphql_name='priceRate_not')
    price_rate_gt = sgqlc.types.Field(BigDecimal, graphql_name='priceRate_gt')
    price_rate_lt = sgqlc.types.Field(BigDecimal, graphql_name='priceRate_lt')
    price_rate_gte = sgqlc.types.Field(BigDecimal, graphql_name='priceRate_gte')
    price_rate_lte = sgqlc.types.Field(BigDecimal, graphql_name='priceRate_lte')
    price_rate_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='priceRate_in')
    price_rate_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='priceRate_not_in')
    balance = sgqlc.types.Field(BigDecimal, graphql_name='balance')
    balance_not = sgqlc.types.Field(BigDecimal, graphql_name='balance_not')
    balance_gt = sgqlc.types.Field(BigDecimal, graphql_name='balance_gt')
    balance_lt = sgqlc.types.Field(BigDecimal, graphql_name='balance_lt')
    balance_gte = sgqlc.types.Field(BigDecimal, graphql_name='balance_gte')
    balance_lte = sgqlc.types.Field(BigDecimal, graphql_name='balance_lte')
    balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_in')
    balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_not_in')
    paid_protocol_fees = sgqlc.types.Field(BigDecimal, graphql_name='paidProtocolFees')
    paid_protocol_fees_not = sgqlc.types.Field(BigDecimal, graphql_name='paidProtocolFees_not')
    paid_protocol_fees_gt = sgqlc.types.Field(BigDecimal, graphql_name='paidProtocolFees_gt')
    paid_protocol_fees_lt = sgqlc.types.Field(BigDecimal, graphql_name='paidProtocolFees_lt')
    paid_protocol_fees_gte = sgqlc.types.Field(BigDecimal, graphql_name='paidProtocolFees_gte')
    paid_protocol_fees_lte = sgqlc.types.Field(BigDecimal, graphql_name='paidProtocolFees_lte')
    paid_protocol_fees_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='paidProtocolFees_in')
    paid_protocol_fees_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='paidProtocolFees_not_in')
    cash_balance = sgqlc.types.Field(BigDecimal, graphql_name='cashBalance')
    cash_balance_not = sgqlc.types.Field(BigDecimal, graphql_name='cashBalance_not')
    cash_balance_gt = sgqlc.types.Field(BigDecimal, graphql_name='cashBalance_gt')
    cash_balance_lt = sgqlc.types.Field(BigDecimal, graphql_name='cashBalance_lt')
    cash_balance_gte = sgqlc.types.Field(BigDecimal, graphql_name='cashBalance_gte')
    cash_balance_lte = sgqlc.types.Field(BigDecimal, graphql_name='cashBalance_lte')
    cash_balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cashBalance_in')
    cash_balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='cashBalance_not_in')
    managed_balance = sgqlc.types.Field(BigDecimal, graphql_name='managedBalance')
    managed_balance_not = sgqlc.types.Field(BigDecimal, graphql_name='managedBalance_not')
    managed_balance_gt = sgqlc.types.Field(BigDecimal, graphql_name='managedBalance_gt')
    managed_balance_lt = sgqlc.types.Field(BigDecimal, graphql_name='managedBalance_lt')
    managed_balance_gte = sgqlc.types.Field(BigDecimal, graphql_name='managedBalance_gte')
    managed_balance_lte = sgqlc.types.Field(BigDecimal, graphql_name='managedBalance_lte')
    managed_balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='managedBalance_in')
    managed_balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='managedBalance_not_in')
    managements_ = sgqlc.types.Field(ManagementOperation_filter, graphql_name='managements_')
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')
    weight_not = sgqlc.types.Field(BigDecimal, graphql_name='weight_not')
    weight_gt = sgqlc.types.Field(BigDecimal, graphql_name='weight_gt')
    weight_lt = sgqlc.types.Field(BigDecimal, graphql_name='weight_lt')
    weight_gte = sgqlc.types.Field(BigDecimal, graphql_name='weight_gte')
    weight_lte = sgqlc.types.Field(BigDecimal, graphql_name='weight_lte')
    weight_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_in')
    weight_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='weight_not_in')
    is_exempt_from_yield_protocol_fee = sgqlc.types.Field(Boolean, graphql_name='isExemptFromYieldProtocolFee')
    is_exempt_from_yield_protocol_fee_not = sgqlc.types.Field(Boolean, graphql_name='isExemptFromYieldProtocolFee_not')
    is_exempt_from_yield_protocol_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isExemptFromYieldProtocolFee_in')
    is_exempt_from_yield_protocol_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isExemptFromYieldProtocolFee_not_in')
    circuit_breaker = sgqlc.types.Field(String, graphql_name='circuitBreaker')
    circuit_breaker_not = sgqlc.types.Field(String, graphql_name='circuitBreaker_not')
    circuit_breaker_gt = sgqlc.types.Field(String, graphql_name='circuitBreaker_gt')
    circuit_breaker_lt = sgqlc.types.Field(String, graphql_name='circuitBreaker_lt')
    circuit_breaker_gte = sgqlc.types.Field(String, graphql_name='circuitBreaker_gte')
    circuit_breaker_lte = sgqlc.types.Field(String, graphql_name='circuitBreaker_lte')
    circuit_breaker_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='circuitBreaker_in')
    circuit_breaker_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='circuitBreaker_not_in')
    circuit_breaker_contains = sgqlc.types.Field(String, graphql_name='circuitBreaker_contains')
    circuit_breaker_contains_nocase = sgqlc.types.Field(String, graphql_name='circuitBreaker_contains_nocase')
    circuit_breaker_not_contains = sgqlc.types.Field(String, graphql_name='circuitBreaker_not_contains')
    circuit_breaker_not_contains_nocase = sgqlc.types.Field(String, graphql_name='circuitBreaker_not_contains_nocase')
    circuit_breaker_starts_with = sgqlc.types.Field(String, graphql_name='circuitBreaker_starts_with')
    circuit_breaker_starts_with_nocase = sgqlc.types.Field(String, graphql_name='circuitBreaker_starts_with_nocase')
    circuit_breaker_not_starts_with = sgqlc.types.Field(String, graphql_name='circuitBreaker_not_starts_with')
    circuit_breaker_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='circuitBreaker_not_starts_with_nocase')
    circuit_breaker_ends_with = sgqlc.types.Field(String, graphql_name='circuitBreaker_ends_with')
    circuit_breaker_ends_with_nocase = sgqlc.types.Field(String, graphql_name='circuitBreaker_ends_with_nocase')
    circuit_breaker_not_ends_with = sgqlc.types.Field(String, graphql_name='circuitBreaker_not_ends_with')
    circuit_breaker_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='circuitBreaker_not_ends_with_nocase')
    circuit_breaker_ = sgqlc.types.Field(CircuitBreaker_filter, graphql_name='circuitBreaker_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PoolToken_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PoolToken_filter'), graphql_name='or')


class Pool_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'address', 'address_not', 'address_gt', 'address_lt', 'address_gte', 'address_lte', 'address_in', 'address_not_in', 'address_contains', 'address_not_contains', 'pool_type', 'pool_type_not', 'pool_type_gt', 'pool_type_lt', 'pool_type_gte', 'pool_type_lte', 'pool_type_in', 'pool_type_not_in', 'pool_type_contains', 'pool_type_contains_nocase', 'pool_type_not_contains', 'pool_type_not_contains_nocase', 'pool_type_starts_with', 'pool_type_starts_with_nocase', 'pool_type_not_starts_with', 'pool_type_not_starts_with_nocase', 'pool_type_ends_with', 'pool_type_ends_with_nocase', 'pool_type_not_ends_with', 'pool_type_not_ends_with_nocase', 'pool_type_version', 'pool_type_version_not', 'pool_type_version_gt', 'pool_type_version_lt', 'pool_type_version_gte', 'pool_type_version_lte', 'pool_type_version_in', 'pool_type_version_not_in', 'factory', 'factory_not', 'factory_gt', 'factory_lt', 'factory_gte', 'factory_lte', 'factory_in', 'factory_not_in', 'factory_contains', 'factory_not_contains', 'strategy_type', 'strategy_type_not', 'strategy_type_gt', 'strategy_type_lt', 'strategy_type_gte', 'strategy_type_lte', 'strategy_type_in', 'strategy_type_not_in', 'oracle_enabled', 'oracle_enabled_not', 'oracle_enabled_in', 'oracle_enabled_not_in', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_contains_nocase', 'symbol_not_contains', 'symbol_not_contains_nocase', 'symbol_starts_with', 'symbol_starts_with_nocase', 'symbol_not_starts_with', 'symbol_not_starts_with_nocase', 'symbol_ends_with', 'symbol_ends_with_nocase', 'symbol_not_ends_with', 'symbol_not_ends_with_nocase', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'swap_enabled', 'swap_enabled_not', 'swap_enabled_in', 'swap_enabled_not_in', 'swap_enabled_internal', 'swap_enabled_internal_not', 'swap_enabled_internal_in', 'swap_enabled_internal_not_in', 'swap_enabled_curation_signal', 'swap_enabled_curation_signal_not', 'swap_enabled_curation_signal_in', 'swap_enabled_curation_signal_not_in', 'swap_fee', 'swap_fee_not', 'swap_fee_gt', 'swap_fee_lt', 'swap_fee_gte', 'swap_fee_lte', 'swap_fee_in', 'swap_fee_not_in', 'owner', 'owner_not', 'owner_gt', 'owner_lt', 'owner_gte', 'owner_lte', 'owner_in', 'owner_not_in', 'owner_contains', 'owner_not_contains', 'is_paused', 'is_paused_not', 'is_paused_in', 'is_paused_not_in', 'total_weight', 'total_weight_not', 'total_weight_gt', 'total_weight_lt', 'total_weight_gte', 'total_weight_lte', 'total_weight_in', 'total_weight_not_in', 'total_swap_volume', 'total_swap_volume_not', 'total_swap_volume_gt', 'total_swap_volume_lt', 'total_swap_volume_gte', 'total_swap_volume_lte', 'total_swap_volume_in', 'total_swap_volume_not_in', 'total_swap_fee', 'total_swap_fee_not', 'total_swap_fee_gt', 'total_swap_fee_lt', 'total_swap_fee_gte', 'total_swap_fee_lte', 'total_swap_fee_in', 'total_swap_fee_not_in', 'total_liquidity', 'total_liquidity_not', 'total_liquidity_gt', 'total_liquidity_lt', 'total_liquidity_gte', 'total_liquidity_lte', 'total_liquidity_in', 'total_liquidity_not_in', 'total_liquidity_sans_bpt', 'total_liquidity_sans_bpt_not', 'total_liquidity_sans_bpt_gt', 'total_liquidity_sans_bpt_lt', 'total_liquidity_sans_bpt_gte', 'total_liquidity_sans_bpt_lte', 'total_liquidity_sans_bpt_in', 'total_liquidity_sans_bpt_not_in', 'total_shares', 'total_shares_not', 'total_shares_gt', 'total_shares_lt', 'total_shares_gte', 'total_shares_lte', 'total_shares_in', 'total_shares_not_in', 'total_protocol_fee', 'total_protocol_fee_not', 'total_protocol_fee_gt', 'total_protocol_fee_lt', 'total_protocol_fee_gte', 'total_protocol_fee_lte', 'total_protocol_fee_in', 'total_protocol_fee_not_in', 'create_time', 'create_time_not', 'create_time_gt', 'create_time_lt', 'create_time_gte', 'create_time_lte', 'create_time_in', 'create_time_not_in', 'swaps_count', 'swaps_count_not', 'swaps_count_gt', 'swaps_count_lt', 'swaps_count_gte', 'swaps_count_lte', 'swaps_count_in', 'swaps_count_not_in', 'holders_count', 'holders_count_not', 'holders_count_gt', 'holders_count_lt', 'holders_count_gte', 'holders_count_lte', 'holders_count_in', 'holders_count_not_in', 'vault_id', 'vault_id_not', 'vault_id_gt', 'vault_id_lt', 'vault_id_gte', 'vault_id_lte', 'vault_id_in', 'vault_id_not_in', 'vault_id_contains', 'vault_id_contains_nocase', 'vault_id_not_contains', 'vault_id_not_contains_nocase', 'vault_id_starts_with', 'vault_id_starts_with_nocase', 'vault_id_not_starts_with', 'vault_id_not_starts_with_nocase', 'vault_id_ends_with', 'vault_id_ends_with_nocase', 'vault_id_not_ends_with', 'vault_id_not_ends_with_nocase', 'vault_id_', 'tx', 'tx_not', 'tx_gt', 'tx_lt', 'tx_gte', 'tx_lte', 'tx_in', 'tx_not_in', 'tx_contains', 'tx_not_contains', 'tokens_list', 'tokens_list_not', 'tokens_list_contains', 'tokens_list_contains_nocase', 'tokens_list_not_contains', 'tokens_list_not_contains_nocase', 'tokens_', 'joins_exits_', 'swaps_', 'shares_', 'snapshots_', 'historical_values_', 'weight_updates_', 'amp', 'amp_not', 'amp_gt', 'amp_lt', 'amp_gte', 'amp_lte', 'amp_in', 'amp_not_in', 'latest_amp_update', 'latest_amp_update_not', 'latest_amp_update_gt', 'latest_amp_update_lt', 'latest_amp_update_gte', 'latest_amp_update_lte', 'latest_amp_update_in', 'latest_amp_update_not_in', 'latest_amp_update_contains', 'latest_amp_update_contains_nocase', 'latest_amp_update_not_contains', 'latest_amp_update_not_contains_nocase', 'latest_amp_update_starts_with', 'latest_amp_update_starts_with_nocase', 'latest_amp_update_not_starts_with', 'latest_amp_update_not_starts_with_nocase', 'latest_amp_update_ends_with', 'latest_amp_update_ends_with_nocase', 'latest_amp_update_not_ends_with', 'latest_amp_update_not_ends_with_nocase', 'latest_amp_update_', 'amp_updates_', 'price_rate_providers_', 'principal_token', 'principal_token_not', 'principal_token_gt', 'principal_token_lt', 'principal_token_gte', 'principal_token_lte', 'principal_token_in', 'principal_token_not_in', 'principal_token_contains', 'principal_token_not_contains', 'base_token', 'base_token_not', 'base_token_gt', 'base_token_lt', 'base_token_gte', 'base_token_lte', 'base_token_in', 'base_token_not_in', 'base_token_contains', 'base_token_not_contains', 'expiry_time', 'expiry_time_not', 'expiry_time_gt', 'expiry_time_lt', 'expiry_time_gte', 'expiry_time_lte', 'expiry_time_in', 'expiry_time_not_in', 'unit_seconds', 'unit_seconds_not', 'unit_seconds_gt', 'unit_seconds_lt', 'unit_seconds_gte', 'unit_seconds_lte', 'unit_seconds_in', 'unit_seconds_not_in', 'management_fee', 'management_fee_not', 'management_fee_gt', 'management_fee_lt', 'management_fee_gte', 'management_fee_lte', 'management_fee_in', 'management_fee_not_in', 'join_exit_enabled', 'join_exit_enabled_not', 'join_exit_enabled_in', 'join_exit_enabled_not_in', 'must_allowlist_lps', 'must_allowlist_lps_not', 'must_allowlist_lps_in', 'must_allowlist_lps_not_in', 'management_aum_fee', 'management_aum_fee_not', 'management_aum_fee_gt', 'management_aum_fee_lt', 'management_aum_fee_gte', 'management_aum_fee_lte', 'management_aum_fee_in', 'management_aum_fee_not_in', 'total_aum_fee_collected_in_bpt', 'total_aum_fee_collected_in_bpt_not', 'total_aum_fee_collected_in_bpt_gt', 'total_aum_fee_collected_in_bpt_lt', 'total_aum_fee_collected_in_bpt_gte', 'total_aum_fee_collected_in_bpt_lte', 'total_aum_fee_collected_in_bpt_in', 'total_aum_fee_collected_in_bpt_not_in', 'circuit_breakers_', 'main_index', 'main_index_not', 'main_index_gt', 'main_index_lt', 'main_index_gte', 'main_index_lte', 'main_index_in', 'main_index_not_in', 'wrapped_index', 'wrapped_index_not', 'wrapped_index_gt', 'wrapped_index_lt', 'wrapped_index_gte', 'wrapped_index_lte', 'wrapped_index_in', 'wrapped_index_not_in', 'lower_target', 'lower_target_not', 'lower_target_gt', 'lower_target_lt', 'lower_target_gte', 'lower_target_lte', 'lower_target_in', 'lower_target_not_in', 'upper_target', 'upper_target_not', 'upper_target_gt', 'upper_target_lt', 'upper_target_gte', 'upper_target_lte', 'upper_target_in', 'upper_target_not_in', 'sqrt_alpha', 'sqrt_alpha_not', 'sqrt_alpha_gt', 'sqrt_alpha_lt', 'sqrt_alpha_gte', 'sqrt_alpha_lte', 'sqrt_alpha_in', 'sqrt_alpha_not_in', 'sqrt_beta', 'sqrt_beta_not', 'sqrt_beta_gt', 'sqrt_beta_lt', 'sqrt_beta_gte', 'sqrt_beta_lte', 'sqrt_beta_in', 'sqrt_beta_not_in', 'root3_alpha', 'root3_alpha_not', 'root3_alpha_gt', 'root3_alpha_lt', 'root3_alpha_gte', 'root3_alpha_lte', 'root3_alpha_in', 'root3_alpha_not_in', 'c', 'c_not', 'c_gt', 'c_lt', 'c_gte', 'c_lte', 'c_in', 'c_not_in', 's', 's_not', 's_gt', 's_lt', 's_gte', 's_lte', 's_in', 's_not_in', 'tau_alpha_x', 'tau_alpha_x_not', 'tau_alpha_x_gt', 'tau_alpha_x_lt', 'tau_alpha_x_gte', 'tau_alpha_x_lte', 'tau_alpha_x_in', 'tau_alpha_x_not_in', 'tau_alpha_y', 'tau_alpha_y_not', 'tau_alpha_y_gt', 'tau_alpha_y_lt', 'tau_alpha_y_gte', 'tau_alpha_y_lte', 'tau_alpha_y_in', 'tau_alpha_y_not_in', 'tau_beta_x', 'tau_beta_x_not', 'tau_beta_x_gt', 'tau_beta_x_lt', 'tau_beta_x_gte', 'tau_beta_x_lte', 'tau_beta_x_in', 'tau_beta_x_not_in', 'tau_beta_y', 'tau_beta_y_not', 'tau_beta_y_gt', 'tau_beta_y_lt', 'tau_beta_y_gte', 'tau_beta_y_lte', 'tau_beta_y_in', 'tau_beta_y_not_in', 'u', 'u_not', 'u_gt', 'u_lt', 'u_gte', 'u_lte', 'u_in', 'u_not_in', 'v', 'v_not', 'v_gt', 'v_lt', 'v_gte', 'v_lte', 'v_in', 'v_not_in', 'w', 'w_not', 'w_gt', 'w_lt', 'w_gte', 'w_lte', 'w_in', 'w_not_in', 'z', 'z_not', 'z_gt', 'z_lt', 'z_gte', 'z_lte', 'z_in', 'z_not_in', 'd_sq', 'd_sq_not', 'd_sq_gt', 'd_sq_lt', 'd_sq_gte', 'd_sq_lte', 'd_sq_in', 'd_sq_not_in', 'alpha', 'alpha_not', 'alpha_gt', 'alpha_lt', 'alpha_gte', 'alpha_lte', 'alpha_in', 'alpha_not_in', 'beta', 'beta_not', 'beta_gt', 'beta_lt', 'beta_gte', 'beta_lte', 'beta_in', 'beta_not_in', 'lambda_', 'lambda_not', 'lambda_gt', 'lambda_lt', 'lambda_gte', 'lambda_lte', 'lambda_in', 'lambda_not_in', 'delta', 'delta_not', 'delta_gt', 'delta_lt', 'delta_gte', 'delta_lte', 'delta_in', 'delta_not_in', 'epsilon', 'epsilon_not', 'epsilon_gt', 'epsilon_lt', 'epsilon_gte', 'epsilon_lte', 'epsilon_in', 'epsilon_not_in', 'is_in_recovery_mode', 'is_in_recovery_mode_not', 'is_in_recovery_mode_in', 'is_in_recovery_mode_not_in', 'protocol_swap_fee_cache', 'protocol_swap_fee_cache_not', 'protocol_swap_fee_cache_gt', 'protocol_swap_fee_cache_lt', 'protocol_swap_fee_cache_gte', 'protocol_swap_fee_cache_lte', 'protocol_swap_fee_cache_in', 'protocol_swap_fee_cache_not_in', 'protocol_yield_fee_cache', 'protocol_yield_fee_cache_not', 'protocol_yield_fee_cache_gt', 'protocol_yield_fee_cache_lt', 'protocol_yield_fee_cache_gte', 'protocol_yield_fee_cache_lte', 'protocol_yield_fee_cache_in', 'protocol_yield_fee_cache_not_in', 'protocol_aum_fee_cache', 'protocol_aum_fee_cache_not', 'protocol_aum_fee_cache_gt', 'protocol_aum_fee_cache_lt', 'protocol_aum_fee_cache_gte', 'protocol_aum_fee_cache_lte', 'protocol_aum_fee_cache_in', 'protocol_aum_fee_cache_not_in', 'total_protocol_fee_paid_in_bpt', 'total_protocol_fee_paid_in_bpt_not', 'total_protocol_fee_paid_in_bpt_gt', 'total_protocol_fee_paid_in_bpt_lt', 'total_protocol_fee_paid_in_bpt_gte', 'total_protocol_fee_paid_in_bpt_lte', 'total_protocol_fee_paid_in_bpt_in', 'total_protocol_fee_paid_in_bpt_not_in', 'last_join_exit_amp', 'last_join_exit_amp_not', 'last_join_exit_amp_gt', 'last_join_exit_amp_lt', 'last_join_exit_amp_gte', 'last_join_exit_amp_lte', 'last_join_exit_amp_in', 'last_join_exit_amp_not_in', 'last_post_join_exit_invariant', 'last_post_join_exit_invariant_not', 'last_post_join_exit_invariant_gt', 'last_post_join_exit_invariant_lt', 'last_post_join_exit_invariant_gte', 'last_post_join_exit_invariant_lte', 'last_post_join_exit_invariant_in', 'last_post_join_exit_invariant_not_in', 'protocol_id', 'protocol_id_not', 'protocol_id_gt', 'protocol_id_lt', 'protocol_id_gte', 'protocol_id_lte', 'protocol_id_in', 'protocol_id_not_in', 'protocol_id_data', 'protocol_id_data_not', 'protocol_id_data_gt', 'protocol_id_data_lt', 'protocol_id_data_gte', 'protocol_id_data_lte', 'protocol_id_data_in', 'protocol_id_data_not_in', 'protocol_id_data_contains', 'protocol_id_data_contains_nocase', 'protocol_id_data_not_contains', 'protocol_id_data_not_contains_nocase', 'protocol_id_data_starts_with', 'protocol_id_data_starts_with_nocase', 'protocol_id_data_not_starts_with', 'protocol_id_data_not_starts_with_nocase', 'protocol_id_data_ends_with', 'protocol_id_data_ends_with_nocase', 'protocol_id_data_not_ends_with', 'protocol_id_data_not_ends_with_nocase', 'protocol_id_data_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    address = sgqlc.types.Field(Bytes, graphql_name='address')
    address_not = sgqlc.types.Field(Bytes, graphql_name='address_not')
    address_gt = sgqlc.types.Field(Bytes, graphql_name='address_gt')
    address_lt = sgqlc.types.Field(Bytes, graphql_name='address_lt')
    address_gte = sgqlc.types.Field(Bytes, graphql_name='address_gte')
    address_lte = sgqlc.types.Field(Bytes, graphql_name='address_lte')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(Bytes, graphql_name='address_contains')
    address_not_contains = sgqlc.types.Field(Bytes, graphql_name='address_not_contains')
    pool_type = sgqlc.types.Field(String, graphql_name='poolType')
    pool_type_not = sgqlc.types.Field(String, graphql_name='poolType_not')
    pool_type_gt = sgqlc.types.Field(String, graphql_name='poolType_gt')
    pool_type_lt = sgqlc.types.Field(String, graphql_name='poolType_lt')
    pool_type_gte = sgqlc.types.Field(String, graphql_name='poolType_gte')
    pool_type_lte = sgqlc.types.Field(String, graphql_name='poolType_lte')
    pool_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolType_in')
    pool_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolType_not_in')
    pool_type_contains = sgqlc.types.Field(String, graphql_name='poolType_contains')
    pool_type_contains_nocase = sgqlc.types.Field(String, graphql_name='poolType_contains_nocase')
    pool_type_not_contains = sgqlc.types.Field(String, graphql_name='poolType_not_contains')
    pool_type_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolType_not_contains_nocase')
    pool_type_starts_with = sgqlc.types.Field(String, graphql_name='poolType_starts_with')
    pool_type_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolType_starts_with_nocase')
    pool_type_not_starts_with = sgqlc.types.Field(String, graphql_name='poolType_not_starts_with')
    pool_type_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolType_not_starts_with_nocase')
    pool_type_ends_with = sgqlc.types.Field(String, graphql_name='poolType_ends_with')
    pool_type_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolType_ends_with_nocase')
    pool_type_not_ends_with = sgqlc.types.Field(String, graphql_name='poolType_not_ends_with')
    pool_type_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolType_not_ends_with_nocase')
    pool_type_version = sgqlc.types.Field(Int, graphql_name='poolTypeVersion')
    pool_type_version_not = sgqlc.types.Field(Int, graphql_name='poolTypeVersion_not')
    pool_type_version_gt = sgqlc.types.Field(Int, graphql_name='poolTypeVersion_gt')
    pool_type_version_lt = sgqlc.types.Field(Int, graphql_name='poolTypeVersion_lt')
    pool_type_version_gte = sgqlc.types.Field(Int, graphql_name='poolTypeVersion_gte')
    pool_type_version_lte = sgqlc.types.Field(Int, graphql_name='poolTypeVersion_lte')
    pool_type_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='poolTypeVersion_in')
    pool_type_version_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='poolTypeVersion_not_in')
    factory = sgqlc.types.Field(Bytes, graphql_name='factory')
    factory_not = sgqlc.types.Field(Bytes, graphql_name='factory_not')
    factory_gt = sgqlc.types.Field(Bytes, graphql_name='factory_gt')
    factory_lt = sgqlc.types.Field(Bytes, graphql_name='factory_lt')
    factory_gte = sgqlc.types.Field(Bytes, graphql_name='factory_gte')
    factory_lte = sgqlc.types.Field(Bytes, graphql_name='factory_lte')
    factory_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='factory_in')
    factory_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='factory_not_in')
    factory_contains = sgqlc.types.Field(Bytes, graphql_name='factory_contains')
    factory_not_contains = sgqlc.types.Field(Bytes, graphql_name='factory_not_contains')
    strategy_type = sgqlc.types.Field(Int, graphql_name='strategyType')
    strategy_type_not = sgqlc.types.Field(Int, graphql_name='strategyType_not')
    strategy_type_gt = sgqlc.types.Field(Int, graphql_name='strategyType_gt')
    strategy_type_lt = sgqlc.types.Field(Int, graphql_name='strategyType_lt')
    strategy_type_gte = sgqlc.types.Field(Int, graphql_name='strategyType_gte')
    strategy_type_lte = sgqlc.types.Field(Int, graphql_name='strategyType_lte')
    strategy_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='strategyType_in')
    strategy_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='strategyType_not_in')
    oracle_enabled = sgqlc.types.Field(Boolean, graphql_name='oracleEnabled')
    oracle_enabled_not = sgqlc.types.Field(Boolean, graphql_name='oracleEnabled_not')
    oracle_enabled_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='oracleEnabled_in')
    oracle_enabled_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='oracleEnabled_not_in')
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
    swap_enabled = sgqlc.types.Field(Boolean, graphql_name='swapEnabled')
    swap_enabled_not = sgqlc.types.Field(Boolean, graphql_name='swapEnabled_not')
    swap_enabled_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='swapEnabled_in')
    swap_enabled_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='swapEnabled_not_in')
    swap_enabled_internal = sgqlc.types.Field(Boolean, graphql_name='swapEnabledInternal')
    swap_enabled_internal_not = sgqlc.types.Field(Boolean, graphql_name='swapEnabledInternal_not')
    swap_enabled_internal_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='swapEnabledInternal_in')
    swap_enabled_internal_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='swapEnabledInternal_not_in')
    swap_enabled_curation_signal = sgqlc.types.Field(Boolean, graphql_name='swapEnabledCurationSignal')
    swap_enabled_curation_signal_not = sgqlc.types.Field(Boolean, graphql_name='swapEnabledCurationSignal_not')
    swap_enabled_curation_signal_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='swapEnabledCurationSignal_in')
    swap_enabled_curation_signal_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='swapEnabledCurationSignal_not_in')
    swap_fee = sgqlc.types.Field(BigDecimal, graphql_name='swapFee')
    swap_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='swapFee_not')
    swap_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='swapFee_gt')
    swap_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='swapFee_lt')
    swap_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='swapFee_gte')
    swap_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='swapFee_lte')
    swap_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='swapFee_in')
    swap_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='swapFee_not_in')
    owner = sgqlc.types.Field(Bytes, graphql_name='owner')
    owner_not = sgqlc.types.Field(Bytes, graphql_name='owner_not')
    owner_gt = sgqlc.types.Field(Bytes, graphql_name='owner_gt')
    owner_lt = sgqlc.types.Field(Bytes, graphql_name='owner_lt')
    owner_gte = sgqlc.types.Field(Bytes, graphql_name='owner_gte')
    owner_lte = sgqlc.types.Field(Bytes, graphql_name='owner_lte')
    owner_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='owner_in')
    owner_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='owner_not_in')
    owner_contains = sgqlc.types.Field(Bytes, graphql_name='owner_contains')
    owner_not_contains = sgqlc.types.Field(Bytes, graphql_name='owner_not_contains')
    is_paused = sgqlc.types.Field(Boolean, graphql_name='isPaused')
    is_paused_not = sgqlc.types.Field(Boolean, graphql_name='isPaused_not')
    is_paused_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isPaused_in')
    is_paused_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isPaused_not_in')
    total_weight = sgqlc.types.Field(BigDecimal, graphql_name='totalWeight')
    total_weight_not = sgqlc.types.Field(BigDecimal, graphql_name='totalWeight_not')
    total_weight_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalWeight_gt')
    total_weight_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalWeight_lt')
    total_weight_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalWeight_gte')
    total_weight_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalWeight_lte')
    total_weight_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalWeight_in')
    total_weight_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalWeight_not_in')
    total_swap_volume = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume')
    total_swap_volume_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_not')
    total_swap_volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gt')
    total_swap_volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lt')
    total_swap_volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gte')
    total_swap_volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lte')
    total_swap_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_in')
    total_swap_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_not_in')
    total_swap_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee')
    total_swap_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_not')
    total_swap_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gt')
    total_swap_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lt')
    total_swap_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gte')
    total_swap_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lte')
    total_swap_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_in')
    total_swap_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_not_in')
    total_liquidity = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity')
    total_liquidity_not = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_not')
    total_liquidity_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_gt')
    total_liquidity_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_lt')
    total_liquidity_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_gte')
    total_liquidity_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquidity_lte')
    total_liquidity_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalLiquidity_in')
    total_liquidity_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalLiquidity_not_in')
    total_liquidity_sans_bpt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquiditySansBPT')
    total_liquidity_sans_bpt_not = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquiditySansBPT_not')
    total_liquidity_sans_bpt_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquiditySansBPT_gt')
    total_liquidity_sans_bpt_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquiditySansBPT_lt')
    total_liquidity_sans_bpt_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquiditySansBPT_gte')
    total_liquidity_sans_bpt_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquiditySansBPT_lte')
    total_liquidity_sans_bpt_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalLiquiditySansBPT_in')
    total_liquidity_sans_bpt_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalLiquiditySansBPT_not_in')
    total_shares = sgqlc.types.Field(BigDecimal, graphql_name='totalShares')
    total_shares_not = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_not')
    total_shares_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_gt')
    total_shares_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_lt')
    total_shares_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_gte')
    total_shares_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalShares_lte')
    total_shares_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalShares_in')
    total_shares_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalShares_not_in')
    total_protocol_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee')
    total_protocol_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_not')
    total_protocol_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_gt')
    total_protocol_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_lt')
    total_protocol_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_gte')
    total_protocol_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee_lte')
    total_protocol_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalProtocolFee_in')
    total_protocol_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalProtocolFee_not_in')
    create_time = sgqlc.types.Field(Int, graphql_name='createTime')
    create_time_not = sgqlc.types.Field(Int, graphql_name='createTime_not')
    create_time_gt = sgqlc.types.Field(Int, graphql_name='createTime_gt')
    create_time_lt = sgqlc.types.Field(Int, graphql_name='createTime_lt')
    create_time_gte = sgqlc.types.Field(Int, graphql_name='createTime_gte')
    create_time_lte = sgqlc.types.Field(Int, graphql_name='createTime_lte')
    create_time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='createTime_in')
    create_time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='createTime_not_in')
    swaps_count = sgqlc.types.Field(BigInt, graphql_name='swapsCount')
    swaps_count_not = sgqlc.types.Field(BigInt, graphql_name='swapsCount_not')
    swaps_count_gt = sgqlc.types.Field(BigInt, graphql_name='swapsCount_gt')
    swaps_count_lt = sgqlc.types.Field(BigInt, graphql_name='swapsCount_lt')
    swaps_count_gte = sgqlc.types.Field(BigInt, graphql_name='swapsCount_gte')
    swaps_count_lte = sgqlc.types.Field(BigInt, graphql_name='swapsCount_lte')
    swaps_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='swapsCount_in')
    swaps_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='swapsCount_not_in')
    holders_count = sgqlc.types.Field(BigInt, graphql_name='holdersCount')
    holders_count_not = sgqlc.types.Field(BigInt, graphql_name='holdersCount_not')
    holders_count_gt = sgqlc.types.Field(BigInt, graphql_name='holdersCount_gt')
    holders_count_lt = sgqlc.types.Field(BigInt, graphql_name='holdersCount_lt')
    holders_count_gte = sgqlc.types.Field(BigInt, graphql_name='holdersCount_gte')
    holders_count_lte = sgqlc.types.Field(BigInt, graphql_name='holdersCount_lte')
    holders_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='holdersCount_in')
    holders_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='holdersCount_not_in')
    vault_id = sgqlc.types.Field(String, graphql_name='vaultID')
    vault_id_not = sgqlc.types.Field(String, graphql_name='vaultID_not')
    vault_id_gt = sgqlc.types.Field(String, graphql_name='vaultID_gt')
    vault_id_lt = sgqlc.types.Field(String, graphql_name='vaultID_lt')
    vault_id_gte = sgqlc.types.Field(String, graphql_name='vaultID_gte')
    vault_id_lte = sgqlc.types.Field(String, graphql_name='vaultID_lte')
    vault_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='vaultID_in')
    vault_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='vaultID_not_in')
    vault_id_contains = sgqlc.types.Field(String, graphql_name='vaultID_contains')
    vault_id_contains_nocase = sgqlc.types.Field(String, graphql_name='vaultID_contains_nocase')
    vault_id_not_contains = sgqlc.types.Field(String, graphql_name='vaultID_not_contains')
    vault_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='vaultID_not_contains_nocase')
    vault_id_starts_with = sgqlc.types.Field(String, graphql_name='vaultID_starts_with')
    vault_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='vaultID_starts_with_nocase')
    vault_id_not_starts_with = sgqlc.types.Field(String, graphql_name='vaultID_not_starts_with')
    vault_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='vaultID_not_starts_with_nocase')
    vault_id_ends_with = sgqlc.types.Field(String, graphql_name='vaultID_ends_with')
    vault_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='vaultID_ends_with_nocase')
    vault_id_not_ends_with = sgqlc.types.Field(String, graphql_name='vaultID_not_ends_with')
    vault_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='vaultID_not_ends_with_nocase')
    vault_id_ = sgqlc.types.Field(Balancer_filter, graphql_name='vaultID_')
    tx = sgqlc.types.Field(Bytes, graphql_name='tx')
    tx_not = sgqlc.types.Field(Bytes, graphql_name='tx_not')
    tx_gt = sgqlc.types.Field(Bytes, graphql_name='tx_gt')
    tx_lt = sgqlc.types.Field(Bytes, graphql_name='tx_lt')
    tx_gte = sgqlc.types.Field(Bytes, graphql_name='tx_gte')
    tx_lte = sgqlc.types.Field(Bytes, graphql_name='tx_lte')
    tx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tx_in')
    tx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tx_not_in')
    tx_contains = sgqlc.types.Field(Bytes, graphql_name='tx_contains')
    tx_not_contains = sgqlc.types.Field(Bytes, graphql_name='tx_not_contains')
    tokens_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokensList')
    tokens_list_not = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokensList_not')
    tokens_list_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokensList_contains')
    tokens_list_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokensList_contains_nocase')
    tokens_list_not_contains = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokensList_not_contains')
    tokens_list_not_contains_nocase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokensList_not_contains_nocase')
    tokens_ = sgqlc.types.Field(PoolToken_filter, graphql_name='tokens_')
    joins_exits_ = sgqlc.types.Field(JoinExit_filter, graphql_name='joinsExits_')
    swaps_ = sgqlc.types.Field('Swap_filter', graphql_name='swaps_')
    shares_ = sgqlc.types.Field(PoolShare_filter, graphql_name='shares_')
    snapshots_ = sgqlc.types.Field(PoolSnapshot_filter, graphql_name='snapshots_')
    historical_values_ = sgqlc.types.Field(PoolHistoricalLiquidity_filter, graphql_name='historicalValues_')
    weight_updates_ = sgqlc.types.Field(GradualWeightUpdate_filter, graphql_name='weightUpdates_')
    amp = sgqlc.types.Field(BigInt, graphql_name='amp')
    amp_not = sgqlc.types.Field(BigInt, graphql_name='amp_not')
    amp_gt = sgqlc.types.Field(BigInt, graphql_name='amp_gt')
    amp_lt = sgqlc.types.Field(BigInt, graphql_name='amp_lt')
    amp_gte = sgqlc.types.Field(BigInt, graphql_name='amp_gte')
    amp_lte = sgqlc.types.Field(BigInt, graphql_name='amp_lte')
    amp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amp_in')
    amp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='amp_not_in')
    latest_amp_update = sgqlc.types.Field(String, graphql_name='latestAmpUpdate')
    latest_amp_update_not = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_not')
    latest_amp_update_gt = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_gt')
    latest_amp_update_lt = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_lt')
    latest_amp_update_gte = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_gte')
    latest_amp_update_lte = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_lte')
    latest_amp_update_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='latestAmpUpdate_in')
    latest_amp_update_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='latestAmpUpdate_not_in')
    latest_amp_update_contains = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_contains')
    latest_amp_update_contains_nocase = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_contains_nocase')
    latest_amp_update_not_contains = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_not_contains')
    latest_amp_update_not_contains_nocase = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_not_contains_nocase')
    latest_amp_update_starts_with = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_starts_with')
    latest_amp_update_starts_with_nocase = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_starts_with_nocase')
    latest_amp_update_not_starts_with = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_not_starts_with')
    latest_amp_update_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_not_starts_with_nocase')
    latest_amp_update_ends_with = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_ends_with')
    latest_amp_update_ends_with_nocase = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_ends_with_nocase')
    latest_amp_update_not_ends_with = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_not_ends_with')
    latest_amp_update_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='latestAmpUpdate_not_ends_with_nocase')
    latest_amp_update_ = sgqlc.types.Field(AmpUpdate_filter, graphql_name='latestAmpUpdate_')
    amp_updates_ = sgqlc.types.Field(AmpUpdate_filter, graphql_name='ampUpdates_')
    price_rate_providers_ = sgqlc.types.Field('PriceRateProvider_filter', graphql_name='priceRateProviders_')
    principal_token = sgqlc.types.Field(Bytes, graphql_name='principalToken')
    principal_token_not = sgqlc.types.Field(Bytes, graphql_name='principalToken_not')
    principal_token_gt = sgqlc.types.Field(Bytes, graphql_name='principalToken_gt')
    principal_token_lt = sgqlc.types.Field(Bytes, graphql_name='principalToken_lt')
    principal_token_gte = sgqlc.types.Field(Bytes, graphql_name='principalToken_gte')
    principal_token_lte = sgqlc.types.Field(Bytes, graphql_name='principalToken_lte')
    principal_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='principalToken_in')
    principal_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='principalToken_not_in')
    principal_token_contains = sgqlc.types.Field(Bytes, graphql_name='principalToken_contains')
    principal_token_not_contains = sgqlc.types.Field(Bytes, graphql_name='principalToken_not_contains')
    base_token = sgqlc.types.Field(Bytes, graphql_name='baseToken')
    base_token_not = sgqlc.types.Field(Bytes, graphql_name='baseToken_not')
    base_token_gt = sgqlc.types.Field(Bytes, graphql_name='baseToken_gt')
    base_token_lt = sgqlc.types.Field(Bytes, graphql_name='baseToken_lt')
    base_token_gte = sgqlc.types.Field(Bytes, graphql_name='baseToken_gte')
    base_token_lte = sgqlc.types.Field(Bytes, graphql_name='baseToken_lte')
    base_token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='baseToken_in')
    base_token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='baseToken_not_in')
    base_token_contains = sgqlc.types.Field(Bytes, graphql_name='baseToken_contains')
    base_token_not_contains = sgqlc.types.Field(Bytes, graphql_name='baseToken_not_contains')
    expiry_time = sgqlc.types.Field(BigInt, graphql_name='expiryTime')
    expiry_time_not = sgqlc.types.Field(BigInt, graphql_name='expiryTime_not')
    expiry_time_gt = sgqlc.types.Field(BigInt, graphql_name='expiryTime_gt')
    expiry_time_lt = sgqlc.types.Field(BigInt, graphql_name='expiryTime_lt')
    expiry_time_gte = sgqlc.types.Field(BigInt, graphql_name='expiryTime_gte')
    expiry_time_lte = sgqlc.types.Field(BigInt, graphql_name='expiryTime_lte')
    expiry_time_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='expiryTime_in')
    expiry_time_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='expiryTime_not_in')
    unit_seconds = sgqlc.types.Field(BigInt, graphql_name='unitSeconds')
    unit_seconds_not = sgqlc.types.Field(BigInt, graphql_name='unitSeconds_not')
    unit_seconds_gt = sgqlc.types.Field(BigInt, graphql_name='unitSeconds_gt')
    unit_seconds_lt = sgqlc.types.Field(BigInt, graphql_name='unitSeconds_lt')
    unit_seconds_gte = sgqlc.types.Field(BigInt, graphql_name='unitSeconds_gte')
    unit_seconds_lte = sgqlc.types.Field(BigInt, graphql_name='unitSeconds_lte')
    unit_seconds_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='unitSeconds_in')
    unit_seconds_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='unitSeconds_not_in')
    management_fee = sgqlc.types.Field(BigDecimal, graphql_name='managementFee')
    management_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='managementFee_not')
    management_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='managementFee_gt')
    management_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='managementFee_lt')
    management_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='managementFee_gte')
    management_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='managementFee_lte')
    management_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='managementFee_in')
    management_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='managementFee_not_in')
    join_exit_enabled = sgqlc.types.Field(Boolean, graphql_name='joinExitEnabled')
    join_exit_enabled_not = sgqlc.types.Field(Boolean, graphql_name='joinExitEnabled_not')
    join_exit_enabled_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='joinExitEnabled_in')
    join_exit_enabled_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='joinExitEnabled_not_in')
    must_allowlist_lps = sgqlc.types.Field(Boolean, graphql_name='mustAllowlistLPs')
    must_allowlist_lps_not = sgqlc.types.Field(Boolean, graphql_name='mustAllowlistLPs_not')
    must_allowlist_lps_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='mustAllowlistLPs_in')
    must_allowlist_lps_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='mustAllowlistLPs_not_in')
    management_aum_fee = sgqlc.types.Field(BigDecimal, graphql_name='managementAumFee')
    management_aum_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='managementAumFee_not')
    management_aum_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='managementAumFee_gt')
    management_aum_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='managementAumFee_lt')
    management_aum_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='managementAumFee_gte')
    management_aum_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='managementAumFee_lte')
    management_aum_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='managementAumFee_in')
    management_aum_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='managementAumFee_not_in')
    total_aum_fee_collected_in_bpt = sgqlc.types.Field(BigDecimal, graphql_name='totalAumFeeCollectedInBPT')
    total_aum_fee_collected_in_bpt_not = sgqlc.types.Field(BigDecimal, graphql_name='totalAumFeeCollectedInBPT_not')
    total_aum_fee_collected_in_bpt_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalAumFeeCollectedInBPT_gt')
    total_aum_fee_collected_in_bpt_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalAumFeeCollectedInBPT_lt')
    total_aum_fee_collected_in_bpt_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalAumFeeCollectedInBPT_gte')
    total_aum_fee_collected_in_bpt_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalAumFeeCollectedInBPT_lte')
    total_aum_fee_collected_in_bpt_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalAumFeeCollectedInBPT_in')
    total_aum_fee_collected_in_bpt_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalAumFeeCollectedInBPT_not_in')
    circuit_breakers_ = sgqlc.types.Field(CircuitBreaker_filter, graphql_name='circuitBreakers_')
    main_index = sgqlc.types.Field(Int, graphql_name='mainIndex')
    main_index_not = sgqlc.types.Field(Int, graphql_name='mainIndex_not')
    main_index_gt = sgqlc.types.Field(Int, graphql_name='mainIndex_gt')
    main_index_lt = sgqlc.types.Field(Int, graphql_name='mainIndex_lt')
    main_index_gte = sgqlc.types.Field(Int, graphql_name='mainIndex_gte')
    main_index_lte = sgqlc.types.Field(Int, graphql_name='mainIndex_lte')
    main_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='mainIndex_in')
    main_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='mainIndex_not_in')
    wrapped_index = sgqlc.types.Field(Int, graphql_name='wrappedIndex')
    wrapped_index_not = sgqlc.types.Field(Int, graphql_name='wrappedIndex_not')
    wrapped_index_gt = sgqlc.types.Field(Int, graphql_name='wrappedIndex_gt')
    wrapped_index_lt = sgqlc.types.Field(Int, graphql_name='wrappedIndex_lt')
    wrapped_index_gte = sgqlc.types.Field(Int, graphql_name='wrappedIndex_gte')
    wrapped_index_lte = sgqlc.types.Field(Int, graphql_name='wrappedIndex_lte')
    wrapped_index_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='wrappedIndex_in')
    wrapped_index_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='wrappedIndex_not_in')
    lower_target = sgqlc.types.Field(BigDecimal, graphql_name='lowerTarget')
    lower_target_not = sgqlc.types.Field(BigDecimal, graphql_name='lowerTarget_not')
    lower_target_gt = sgqlc.types.Field(BigDecimal, graphql_name='lowerTarget_gt')
    lower_target_lt = sgqlc.types.Field(BigDecimal, graphql_name='lowerTarget_lt')
    lower_target_gte = sgqlc.types.Field(BigDecimal, graphql_name='lowerTarget_gte')
    lower_target_lte = sgqlc.types.Field(BigDecimal, graphql_name='lowerTarget_lte')
    lower_target_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lowerTarget_in')
    lower_target_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lowerTarget_not_in')
    upper_target = sgqlc.types.Field(BigDecimal, graphql_name='upperTarget')
    upper_target_not = sgqlc.types.Field(BigDecimal, graphql_name='upperTarget_not')
    upper_target_gt = sgqlc.types.Field(BigDecimal, graphql_name='upperTarget_gt')
    upper_target_lt = sgqlc.types.Field(BigDecimal, graphql_name='upperTarget_lt')
    upper_target_gte = sgqlc.types.Field(BigDecimal, graphql_name='upperTarget_gte')
    upper_target_lte = sgqlc.types.Field(BigDecimal, graphql_name='upperTarget_lte')
    upper_target_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='upperTarget_in')
    upper_target_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='upperTarget_not_in')
    sqrt_alpha = sgqlc.types.Field(BigDecimal, graphql_name='sqrtAlpha')
    sqrt_alpha_not = sgqlc.types.Field(BigDecimal, graphql_name='sqrtAlpha_not')
    sqrt_alpha_gt = sgqlc.types.Field(BigDecimal, graphql_name='sqrtAlpha_gt')
    sqrt_alpha_lt = sgqlc.types.Field(BigDecimal, graphql_name='sqrtAlpha_lt')
    sqrt_alpha_gte = sgqlc.types.Field(BigDecimal, graphql_name='sqrtAlpha_gte')
    sqrt_alpha_lte = sgqlc.types.Field(BigDecimal, graphql_name='sqrtAlpha_lte')
    sqrt_alpha_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='sqrtAlpha_in')
    sqrt_alpha_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='sqrtAlpha_not_in')
    sqrt_beta = sgqlc.types.Field(BigDecimal, graphql_name='sqrtBeta')
    sqrt_beta_not = sgqlc.types.Field(BigDecimal, graphql_name='sqrtBeta_not')
    sqrt_beta_gt = sgqlc.types.Field(BigDecimal, graphql_name='sqrtBeta_gt')
    sqrt_beta_lt = sgqlc.types.Field(BigDecimal, graphql_name='sqrtBeta_lt')
    sqrt_beta_gte = sgqlc.types.Field(BigDecimal, graphql_name='sqrtBeta_gte')
    sqrt_beta_lte = sgqlc.types.Field(BigDecimal, graphql_name='sqrtBeta_lte')
    sqrt_beta_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='sqrtBeta_in')
    sqrt_beta_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='sqrtBeta_not_in')
    root3_alpha = sgqlc.types.Field(BigDecimal, graphql_name='root3Alpha')
    root3_alpha_not = sgqlc.types.Field(BigDecimal, graphql_name='root3Alpha_not')
    root3_alpha_gt = sgqlc.types.Field(BigDecimal, graphql_name='root3Alpha_gt')
    root3_alpha_lt = sgqlc.types.Field(BigDecimal, graphql_name='root3Alpha_lt')
    root3_alpha_gte = sgqlc.types.Field(BigDecimal, graphql_name='root3Alpha_gte')
    root3_alpha_lte = sgqlc.types.Field(BigDecimal, graphql_name='root3Alpha_lte')
    root3_alpha_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='root3Alpha_in')
    root3_alpha_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='root3Alpha_not_in')
    c = sgqlc.types.Field(BigDecimal, graphql_name='c')
    c_not = sgqlc.types.Field(BigDecimal, graphql_name='c_not')
    c_gt = sgqlc.types.Field(BigDecimal, graphql_name='c_gt')
    c_lt = sgqlc.types.Field(BigDecimal, graphql_name='c_lt')
    c_gte = sgqlc.types.Field(BigDecimal, graphql_name='c_gte')
    c_lte = sgqlc.types.Field(BigDecimal, graphql_name='c_lte')
    c_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='c_in')
    c_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='c_not_in')
    s = sgqlc.types.Field(BigDecimal, graphql_name='s')
    s_not = sgqlc.types.Field(BigDecimal, graphql_name='s_not')
    s_gt = sgqlc.types.Field(BigDecimal, graphql_name='s_gt')
    s_lt = sgqlc.types.Field(BigDecimal, graphql_name='s_lt')
    s_gte = sgqlc.types.Field(BigDecimal, graphql_name='s_gte')
    s_lte = sgqlc.types.Field(BigDecimal, graphql_name='s_lte')
    s_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='s_in')
    s_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='s_not_in')
    tau_alpha_x = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaX')
    tau_alpha_x_not = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaX_not')
    tau_alpha_x_gt = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaX_gt')
    tau_alpha_x_lt = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaX_lt')
    tau_alpha_x_gte = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaX_gte')
    tau_alpha_x_lte = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaX_lte')
    tau_alpha_x_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tauAlphaX_in')
    tau_alpha_x_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tauAlphaX_not_in')
    tau_alpha_y = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaY')
    tau_alpha_y_not = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaY_not')
    tau_alpha_y_gt = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaY_gt')
    tau_alpha_y_lt = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaY_lt')
    tau_alpha_y_gte = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaY_gte')
    tau_alpha_y_lte = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaY_lte')
    tau_alpha_y_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tauAlphaY_in')
    tau_alpha_y_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tauAlphaY_not_in')
    tau_beta_x = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaX')
    tau_beta_x_not = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaX_not')
    tau_beta_x_gt = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaX_gt')
    tau_beta_x_lt = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaX_lt')
    tau_beta_x_gte = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaX_gte')
    tau_beta_x_lte = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaX_lte')
    tau_beta_x_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tauBetaX_in')
    tau_beta_x_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tauBetaX_not_in')
    tau_beta_y = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaY')
    tau_beta_y_not = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaY_not')
    tau_beta_y_gt = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaY_gt')
    tau_beta_y_lt = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaY_lt')
    tau_beta_y_gte = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaY_gte')
    tau_beta_y_lte = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaY_lte')
    tau_beta_y_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tauBetaY_in')
    tau_beta_y_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tauBetaY_not_in')
    u = sgqlc.types.Field(BigDecimal, graphql_name='u')
    u_not = sgqlc.types.Field(BigDecimal, graphql_name='u_not')
    u_gt = sgqlc.types.Field(BigDecimal, graphql_name='u_gt')
    u_lt = sgqlc.types.Field(BigDecimal, graphql_name='u_lt')
    u_gte = sgqlc.types.Field(BigDecimal, graphql_name='u_gte')
    u_lte = sgqlc.types.Field(BigDecimal, graphql_name='u_lte')
    u_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='u_in')
    u_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='u_not_in')
    v = sgqlc.types.Field(BigDecimal, graphql_name='v')
    v_not = sgqlc.types.Field(BigDecimal, graphql_name='v_not')
    v_gt = sgqlc.types.Field(BigDecimal, graphql_name='v_gt')
    v_lt = sgqlc.types.Field(BigDecimal, graphql_name='v_lt')
    v_gte = sgqlc.types.Field(BigDecimal, graphql_name='v_gte')
    v_lte = sgqlc.types.Field(BigDecimal, graphql_name='v_lte')
    v_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='v_in')
    v_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='v_not_in')
    w = sgqlc.types.Field(BigDecimal, graphql_name='w')
    w_not = sgqlc.types.Field(BigDecimal, graphql_name='w_not')
    w_gt = sgqlc.types.Field(BigDecimal, graphql_name='w_gt')
    w_lt = sgqlc.types.Field(BigDecimal, graphql_name='w_lt')
    w_gte = sgqlc.types.Field(BigDecimal, graphql_name='w_gte')
    w_lte = sgqlc.types.Field(BigDecimal, graphql_name='w_lte')
    w_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='w_in')
    w_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='w_not_in')
    z = sgqlc.types.Field(BigDecimal, graphql_name='z')
    z_not = sgqlc.types.Field(BigDecimal, graphql_name='z_not')
    z_gt = sgqlc.types.Field(BigDecimal, graphql_name='z_gt')
    z_lt = sgqlc.types.Field(BigDecimal, graphql_name='z_lt')
    z_gte = sgqlc.types.Field(BigDecimal, graphql_name='z_gte')
    z_lte = sgqlc.types.Field(BigDecimal, graphql_name='z_lte')
    z_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='z_in')
    z_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='z_not_in')
    d_sq = sgqlc.types.Field(BigDecimal, graphql_name='dSq')
    d_sq_not = sgqlc.types.Field(BigDecimal, graphql_name='dSq_not')
    d_sq_gt = sgqlc.types.Field(BigDecimal, graphql_name='dSq_gt')
    d_sq_lt = sgqlc.types.Field(BigDecimal, graphql_name='dSq_lt')
    d_sq_gte = sgqlc.types.Field(BigDecimal, graphql_name='dSq_gte')
    d_sq_lte = sgqlc.types.Field(BigDecimal, graphql_name='dSq_lte')
    d_sq_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dSq_in')
    d_sq_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='dSq_not_in')
    alpha = sgqlc.types.Field(BigDecimal, graphql_name='alpha')
    alpha_not = sgqlc.types.Field(BigDecimal, graphql_name='alpha_not')
    alpha_gt = sgqlc.types.Field(BigDecimal, graphql_name='alpha_gt')
    alpha_lt = sgqlc.types.Field(BigDecimal, graphql_name='alpha_lt')
    alpha_gte = sgqlc.types.Field(BigDecimal, graphql_name='alpha_gte')
    alpha_lte = sgqlc.types.Field(BigDecimal, graphql_name='alpha_lte')
    alpha_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='alpha_in')
    alpha_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='alpha_not_in')
    beta = sgqlc.types.Field(BigDecimal, graphql_name='beta')
    beta_not = sgqlc.types.Field(BigDecimal, graphql_name='beta_not')
    beta_gt = sgqlc.types.Field(BigDecimal, graphql_name='beta_gt')
    beta_lt = sgqlc.types.Field(BigDecimal, graphql_name='beta_lt')
    beta_gte = sgqlc.types.Field(BigDecimal, graphql_name='beta_gte')
    beta_lte = sgqlc.types.Field(BigDecimal, graphql_name='beta_lte')
    beta_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='beta_in')
    beta_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='beta_not_in')
    lambda_ = sgqlc.types.Field(BigDecimal, graphql_name='lambda')
    lambda_not = sgqlc.types.Field(BigDecimal, graphql_name='lambda_not')
    lambda_gt = sgqlc.types.Field(BigDecimal, graphql_name='lambda_gt')
    lambda_lt = sgqlc.types.Field(BigDecimal, graphql_name='lambda_lt')
    lambda_gte = sgqlc.types.Field(BigDecimal, graphql_name='lambda_gte')
    lambda_lte = sgqlc.types.Field(BigDecimal, graphql_name='lambda_lte')
    lambda_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lambda_in')
    lambda_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lambda_not_in')
    delta = sgqlc.types.Field(BigDecimal, graphql_name='delta')
    delta_not = sgqlc.types.Field(BigDecimal, graphql_name='delta_not')
    delta_gt = sgqlc.types.Field(BigDecimal, graphql_name='delta_gt')
    delta_lt = sgqlc.types.Field(BigDecimal, graphql_name='delta_lt')
    delta_gte = sgqlc.types.Field(BigDecimal, graphql_name='delta_gte')
    delta_lte = sgqlc.types.Field(BigDecimal, graphql_name='delta_lte')
    delta_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='delta_in')
    delta_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='delta_not_in')
    epsilon = sgqlc.types.Field(BigDecimal, graphql_name='epsilon')
    epsilon_not = sgqlc.types.Field(BigDecimal, graphql_name='epsilon_not')
    epsilon_gt = sgqlc.types.Field(BigDecimal, graphql_name='epsilon_gt')
    epsilon_lt = sgqlc.types.Field(BigDecimal, graphql_name='epsilon_lt')
    epsilon_gte = sgqlc.types.Field(BigDecimal, graphql_name='epsilon_gte')
    epsilon_lte = sgqlc.types.Field(BigDecimal, graphql_name='epsilon_lte')
    epsilon_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='epsilon_in')
    epsilon_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='epsilon_not_in')
    is_in_recovery_mode = sgqlc.types.Field(Boolean, graphql_name='isInRecoveryMode')
    is_in_recovery_mode_not = sgqlc.types.Field(Boolean, graphql_name='isInRecoveryMode_not')
    is_in_recovery_mode_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isInRecoveryMode_in')
    is_in_recovery_mode_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Boolean)), graphql_name='isInRecoveryMode_not_in')
    protocol_swap_fee_cache = sgqlc.types.Field(BigDecimal, graphql_name='protocolSwapFeeCache')
    protocol_swap_fee_cache_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolSwapFeeCache_not')
    protocol_swap_fee_cache_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolSwapFeeCache_gt')
    protocol_swap_fee_cache_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolSwapFeeCache_lt')
    protocol_swap_fee_cache_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolSwapFeeCache_gte')
    protocol_swap_fee_cache_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolSwapFeeCache_lte')
    protocol_swap_fee_cache_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolSwapFeeCache_in')
    protocol_swap_fee_cache_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolSwapFeeCache_not_in')
    protocol_yield_fee_cache = sgqlc.types.Field(BigDecimal, graphql_name='protocolYieldFeeCache')
    protocol_yield_fee_cache_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolYieldFeeCache_not')
    protocol_yield_fee_cache_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolYieldFeeCache_gt')
    protocol_yield_fee_cache_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolYieldFeeCache_lt')
    protocol_yield_fee_cache_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolYieldFeeCache_gte')
    protocol_yield_fee_cache_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolYieldFeeCache_lte')
    protocol_yield_fee_cache_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolYieldFeeCache_in')
    protocol_yield_fee_cache_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolYieldFeeCache_not_in')
    protocol_aum_fee_cache = sgqlc.types.Field(BigDecimal, graphql_name='protocolAumFeeCache')
    protocol_aum_fee_cache_not = sgqlc.types.Field(BigDecimal, graphql_name='protocolAumFeeCache_not')
    protocol_aum_fee_cache_gt = sgqlc.types.Field(BigDecimal, graphql_name='protocolAumFeeCache_gt')
    protocol_aum_fee_cache_lt = sgqlc.types.Field(BigDecimal, graphql_name='protocolAumFeeCache_lt')
    protocol_aum_fee_cache_gte = sgqlc.types.Field(BigDecimal, graphql_name='protocolAumFeeCache_gte')
    protocol_aum_fee_cache_lte = sgqlc.types.Field(BigDecimal, graphql_name='protocolAumFeeCache_lte')
    protocol_aum_fee_cache_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolAumFeeCache_in')
    protocol_aum_fee_cache_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='protocolAumFeeCache_not_in')
    total_protocol_fee_paid_in_bpt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFeePaidInBPT')
    total_protocol_fee_paid_in_bpt_not = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFeePaidInBPT_not')
    total_protocol_fee_paid_in_bpt_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFeePaidInBPT_gt')
    total_protocol_fee_paid_in_bpt_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFeePaidInBPT_lt')
    total_protocol_fee_paid_in_bpt_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFeePaidInBPT_gte')
    total_protocol_fee_paid_in_bpt_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFeePaidInBPT_lte')
    total_protocol_fee_paid_in_bpt_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalProtocolFeePaidInBPT_in')
    total_protocol_fee_paid_in_bpt_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalProtocolFeePaidInBPT_not_in')
    last_join_exit_amp = sgqlc.types.Field(BigInt, graphql_name='lastJoinExitAmp')
    last_join_exit_amp_not = sgqlc.types.Field(BigInt, graphql_name='lastJoinExitAmp_not')
    last_join_exit_amp_gt = sgqlc.types.Field(BigInt, graphql_name='lastJoinExitAmp_gt')
    last_join_exit_amp_lt = sgqlc.types.Field(BigInt, graphql_name='lastJoinExitAmp_lt')
    last_join_exit_amp_gte = sgqlc.types.Field(BigInt, graphql_name='lastJoinExitAmp_gte')
    last_join_exit_amp_lte = sgqlc.types.Field(BigInt, graphql_name='lastJoinExitAmp_lte')
    last_join_exit_amp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='lastJoinExitAmp_in')
    last_join_exit_amp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='lastJoinExitAmp_not_in')
    last_post_join_exit_invariant = sgqlc.types.Field(BigDecimal, graphql_name='lastPostJoinExitInvariant')
    last_post_join_exit_invariant_not = sgqlc.types.Field(BigDecimal, graphql_name='lastPostJoinExitInvariant_not')
    last_post_join_exit_invariant_gt = sgqlc.types.Field(BigDecimal, graphql_name='lastPostJoinExitInvariant_gt')
    last_post_join_exit_invariant_lt = sgqlc.types.Field(BigDecimal, graphql_name='lastPostJoinExitInvariant_lt')
    last_post_join_exit_invariant_gte = sgqlc.types.Field(BigDecimal, graphql_name='lastPostJoinExitInvariant_gte')
    last_post_join_exit_invariant_lte = sgqlc.types.Field(BigDecimal, graphql_name='lastPostJoinExitInvariant_lte')
    last_post_join_exit_invariant_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lastPostJoinExitInvariant_in')
    last_post_join_exit_invariant_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='lastPostJoinExitInvariant_not_in')
    protocol_id = sgqlc.types.Field(Int, graphql_name='protocolId')
    protocol_id_not = sgqlc.types.Field(Int, graphql_name='protocolId_not')
    protocol_id_gt = sgqlc.types.Field(Int, graphql_name='protocolId_gt')
    protocol_id_lt = sgqlc.types.Field(Int, graphql_name='protocolId_lt')
    protocol_id_gte = sgqlc.types.Field(Int, graphql_name='protocolId_gte')
    protocol_id_lte = sgqlc.types.Field(Int, graphql_name='protocolId_lte')
    protocol_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='protocolId_in')
    protocol_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='protocolId_not_in')
    protocol_id_data = sgqlc.types.Field(String, graphql_name='protocolIdData')
    protocol_id_data_not = sgqlc.types.Field(String, graphql_name='protocolIdData_not')
    protocol_id_data_gt = sgqlc.types.Field(String, graphql_name='protocolIdData_gt')
    protocol_id_data_lt = sgqlc.types.Field(String, graphql_name='protocolIdData_lt')
    protocol_id_data_gte = sgqlc.types.Field(String, graphql_name='protocolIdData_gte')
    protocol_id_data_lte = sgqlc.types.Field(String, graphql_name='protocolIdData_lte')
    protocol_id_data_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocolIdData_in')
    protocol_id_data_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='protocolIdData_not_in')
    protocol_id_data_contains = sgqlc.types.Field(String, graphql_name='protocolIdData_contains')
    protocol_id_data_contains_nocase = sgqlc.types.Field(String, graphql_name='protocolIdData_contains_nocase')
    protocol_id_data_not_contains = sgqlc.types.Field(String, graphql_name='protocolIdData_not_contains')
    protocol_id_data_not_contains_nocase = sgqlc.types.Field(String, graphql_name='protocolIdData_not_contains_nocase')
    protocol_id_data_starts_with = sgqlc.types.Field(String, graphql_name='protocolIdData_starts_with')
    protocol_id_data_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocolIdData_starts_with_nocase')
    protocol_id_data_not_starts_with = sgqlc.types.Field(String, graphql_name='protocolIdData_not_starts_with')
    protocol_id_data_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='protocolIdData_not_starts_with_nocase')
    protocol_id_data_ends_with = sgqlc.types.Field(String, graphql_name='protocolIdData_ends_with')
    protocol_id_data_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocolIdData_ends_with_nocase')
    protocol_id_data_not_ends_with = sgqlc.types.Field(String, graphql_name='protocolIdData_not_ends_with')
    protocol_id_data_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='protocolIdData_not_ends_with_nocase')
    protocol_id_data_ = sgqlc.types.Field('ProtocolIdData_filter', graphql_name='protocolIdData_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Pool_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Pool_filter'), graphql_name='or')


class PriceRateProvider_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_id', 'pool_id_not', 'pool_id_gt', 'pool_id_lt', 'pool_id_gte', 'pool_id_lte', 'pool_id_in', 'pool_id_not_in', 'pool_id_contains', 'pool_id_contains_nocase', 'pool_id_not_contains', 'pool_id_not_contains_nocase', 'pool_id_starts_with', 'pool_id_starts_with_nocase', 'pool_id_not_starts_with', 'pool_id_not_starts_with_nocase', 'pool_id_ends_with', 'pool_id_ends_with_nocase', 'pool_id_not_ends_with', 'pool_id_not_ends_with_nocase', 'pool_id_', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'token_', 'address', 'address_not', 'address_gt', 'address_lt', 'address_gte', 'address_lte', 'address_in', 'address_not_in', 'address_contains', 'address_not_contains', 'rate', 'rate_not', 'rate_gt', 'rate_lt', 'rate_gte', 'rate_lte', 'rate_in', 'rate_not_in', 'last_cached', 'last_cached_not', 'last_cached_gt', 'last_cached_lt', 'last_cached_gte', 'last_cached_lte', 'last_cached_in', 'last_cached_not_in', 'cache_duration', 'cache_duration_not', 'cache_duration_gt', 'cache_duration_lt', 'cache_duration_gte', 'cache_duration_lte', 'cache_duration_in', 'cache_duration_not_in', 'cache_expiry', 'cache_expiry_not', 'cache_expiry_gt', 'cache_expiry_lt', 'cache_expiry_gte', 'cache_expiry_lte', 'cache_expiry_in', 'cache_expiry_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool_id = sgqlc.types.Field(String, graphql_name='poolId')
    pool_id_not = sgqlc.types.Field(String, graphql_name='poolId_not')
    pool_id_gt = sgqlc.types.Field(String, graphql_name='poolId_gt')
    pool_id_lt = sgqlc.types.Field(String, graphql_name='poolId_lt')
    pool_id_gte = sgqlc.types.Field(String, graphql_name='poolId_gte')
    pool_id_lte = sgqlc.types.Field(String, graphql_name='poolId_lte')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_in')
    pool_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_not_in')
    pool_id_contains = sgqlc.types.Field(String, graphql_name='poolId_contains')
    pool_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_contains_nocase')
    pool_id_not_contains = sgqlc.types.Field(String, graphql_name='poolId_not_contains')
    pool_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_contains_nocase')
    pool_id_starts_with = sgqlc.types.Field(String, graphql_name='poolId_starts_with')
    pool_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_starts_with_nocase')
    pool_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with')
    pool_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with_nocase')
    pool_id_ends_with = sgqlc.types.Field(String, graphql_name='poolId_ends_with')
    pool_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_ends_with_nocase')
    pool_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with')
    pool_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with_nocase')
    pool_id_ = sgqlc.types.Field(Pool_filter, graphql_name='poolId_')
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
    token_ = sgqlc.types.Field(PoolToken_filter, graphql_name='token_')
    address = sgqlc.types.Field(Bytes, graphql_name='address')
    address_not = sgqlc.types.Field(Bytes, graphql_name='address_not')
    address_gt = sgqlc.types.Field(Bytes, graphql_name='address_gt')
    address_lt = sgqlc.types.Field(Bytes, graphql_name='address_lt')
    address_gte = sgqlc.types.Field(Bytes, graphql_name='address_gte')
    address_lte = sgqlc.types.Field(Bytes, graphql_name='address_lte')
    address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_in')
    address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='address_not_in')
    address_contains = sgqlc.types.Field(Bytes, graphql_name='address_contains')
    address_not_contains = sgqlc.types.Field(Bytes, graphql_name='address_not_contains')
    rate = sgqlc.types.Field(BigDecimal, graphql_name='rate')
    rate_not = sgqlc.types.Field(BigDecimal, graphql_name='rate_not')
    rate_gt = sgqlc.types.Field(BigDecimal, graphql_name='rate_gt')
    rate_lt = sgqlc.types.Field(BigDecimal, graphql_name='rate_lt')
    rate_gte = sgqlc.types.Field(BigDecimal, graphql_name='rate_gte')
    rate_lte = sgqlc.types.Field(BigDecimal, graphql_name='rate_lte')
    rate_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rate_in')
    rate_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='rate_not_in')
    last_cached = sgqlc.types.Field(Int, graphql_name='lastCached')
    last_cached_not = sgqlc.types.Field(Int, graphql_name='lastCached_not')
    last_cached_gt = sgqlc.types.Field(Int, graphql_name='lastCached_gt')
    last_cached_lt = sgqlc.types.Field(Int, graphql_name='lastCached_lt')
    last_cached_gte = sgqlc.types.Field(Int, graphql_name='lastCached_gte')
    last_cached_lte = sgqlc.types.Field(Int, graphql_name='lastCached_lte')
    last_cached_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='lastCached_in')
    last_cached_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='lastCached_not_in')
    cache_duration = sgqlc.types.Field(Int, graphql_name='cacheDuration')
    cache_duration_not = sgqlc.types.Field(Int, graphql_name='cacheDuration_not')
    cache_duration_gt = sgqlc.types.Field(Int, graphql_name='cacheDuration_gt')
    cache_duration_lt = sgqlc.types.Field(Int, graphql_name='cacheDuration_lt')
    cache_duration_gte = sgqlc.types.Field(Int, graphql_name='cacheDuration_gte')
    cache_duration_lte = sgqlc.types.Field(Int, graphql_name='cacheDuration_lte')
    cache_duration_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cacheDuration_in')
    cache_duration_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cacheDuration_not_in')
    cache_expiry = sgqlc.types.Field(Int, graphql_name='cacheExpiry')
    cache_expiry_not = sgqlc.types.Field(Int, graphql_name='cacheExpiry_not')
    cache_expiry_gt = sgqlc.types.Field(Int, graphql_name='cacheExpiry_gt')
    cache_expiry_lt = sgqlc.types.Field(Int, graphql_name='cacheExpiry_lt')
    cache_expiry_gte = sgqlc.types.Field(Int, graphql_name='cacheExpiry_gte')
    cache_expiry_lte = sgqlc.types.Field(Int, graphql_name='cacheExpiry_lte')
    cache_expiry_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cacheExpiry_in')
    cache_expiry_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='cacheExpiry_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('PriceRateProvider_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('PriceRateProvider_filter'), graphql_name='or')


class ProtocolIdData_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', '_change_block', 'and_', 'or_')
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
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('ProtocolIdData_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('ProtocolIdData_filter'), graphql_name='or')


class SwapFeeUpdate_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'scheduled_timestamp', 'scheduled_timestamp_not', 'scheduled_timestamp_gt', 'scheduled_timestamp_lt', 'scheduled_timestamp_gte', 'scheduled_timestamp_lte', 'scheduled_timestamp_in', 'scheduled_timestamp_not_in', 'start_timestamp', 'start_timestamp_not', 'start_timestamp_gt', 'start_timestamp_lt', 'start_timestamp_gte', 'start_timestamp_lte', 'start_timestamp_in', 'start_timestamp_not_in', 'end_timestamp', 'end_timestamp_not', 'end_timestamp_gt', 'end_timestamp_lt', 'end_timestamp_gte', 'end_timestamp_lte', 'end_timestamp_in', 'end_timestamp_not_in', 'start_swap_fee_percentage', 'start_swap_fee_percentage_not', 'start_swap_fee_percentage_gt', 'start_swap_fee_percentage_lt', 'start_swap_fee_percentage_gte', 'start_swap_fee_percentage_lte', 'start_swap_fee_percentage_in', 'start_swap_fee_percentage_not_in', 'end_swap_fee_percentage', 'end_swap_fee_percentage_not', 'end_swap_fee_percentage_gt', 'end_swap_fee_percentage_lt', 'end_swap_fee_percentage_gte', 'end_swap_fee_percentage_lte', 'end_swap_fee_percentage_in', 'end_swap_fee_percentage_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
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
    scheduled_timestamp = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp')
    scheduled_timestamp_not = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_not')
    scheduled_timestamp_gt = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_gt')
    scheduled_timestamp_lt = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_lt')
    scheduled_timestamp_gte = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_gte')
    scheduled_timestamp_lte = sgqlc.types.Field(Int, graphql_name='scheduledTimestamp_lte')
    scheduled_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='scheduledTimestamp_in')
    scheduled_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='scheduledTimestamp_not_in')
    start_timestamp = sgqlc.types.Field(BigInt, graphql_name='startTimestamp')
    start_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_not')
    start_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_gt')
    start_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_lt')
    start_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_gte')
    start_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='startTimestamp_lte')
    start_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startTimestamp_in')
    start_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='startTimestamp_not_in')
    end_timestamp = sgqlc.types.Field(BigInt, graphql_name='endTimestamp')
    end_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_not')
    end_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_gt')
    end_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_lt')
    end_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_gte')
    end_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='endTimestamp_lte')
    end_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endTimestamp_in')
    end_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='endTimestamp_not_in')
    start_swap_fee_percentage = sgqlc.types.Field(BigDecimal, graphql_name='startSwapFeePercentage')
    start_swap_fee_percentage_not = sgqlc.types.Field(BigDecimal, graphql_name='startSwapFeePercentage_not')
    start_swap_fee_percentage_gt = sgqlc.types.Field(BigDecimal, graphql_name='startSwapFeePercentage_gt')
    start_swap_fee_percentage_lt = sgqlc.types.Field(BigDecimal, graphql_name='startSwapFeePercentage_lt')
    start_swap_fee_percentage_gte = sgqlc.types.Field(BigDecimal, graphql_name='startSwapFeePercentage_gte')
    start_swap_fee_percentage_lte = sgqlc.types.Field(BigDecimal, graphql_name='startSwapFeePercentage_lte')
    start_swap_fee_percentage_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='startSwapFeePercentage_in')
    start_swap_fee_percentage_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='startSwapFeePercentage_not_in')
    end_swap_fee_percentage = sgqlc.types.Field(BigDecimal, graphql_name='endSwapFeePercentage')
    end_swap_fee_percentage_not = sgqlc.types.Field(BigDecimal, graphql_name='endSwapFeePercentage_not')
    end_swap_fee_percentage_gt = sgqlc.types.Field(BigDecimal, graphql_name='endSwapFeePercentage_gt')
    end_swap_fee_percentage_lt = sgqlc.types.Field(BigDecimal, graphql_name='endSwapFeePercentage_lt')
    end_swap_fee_percentage_gte = sgqlc.types.Field(BigDecimal, graphql_name='endSwapFeePercentage_gte')
    end_swap_fee_percentage_lte = sgqlc.types.Field(BigDecimal, graphql_name='endSwapFeePercentage_lte')
    end_swap_fee_percentage_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='endSwapFeePercentage_in')
    end_swap_fee_percentage_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='endSwapFeePercentage_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('SwapFeeUpdate_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('SwapFeeUpdate_filter'), graphql_name='or')


class Swap_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'caller', 'caller_not', 'caller_gt', 'caller_lt', 'caller_gte', 'caller_lte', 'caller_in', 'caller_not_in', 'caller_contains', 'caller_not_contains', 'token_in', 'token_in_not', 'token_in_gt', 'token_in_lt', 'token_in_gte', 'token_in_lte', 'token_in_in', 'token_in_not_in', 'token_in_contains', 'token_in_not_contains', 'token_in_sym', 'token_in_sym_not', 'token_in_sym_gt', 'token_in_sym_lt', 'token_in_sym_gte', 'token_in_sym_lte', 'token_in_sym_in', 'token_in_sym_not_in', 'token_in_sym_contains', 'token_in_sym_contains_nocase', 'token_in_sym_not_contains', 'token_in_sym_not_contains_nocase', 'token_in_sym_starts_with', 'token_in_sym_starts_with_nocase', 'token_in_sym_not_starts_with', 'token_in_sym_not_starts_with_nocase', 'token_in_sym_ends_with', 'token_in_sym_ends_with_nocase', 'token_in_sym_not_ends_with', 'token_in_sym_not_ends_with_nocase', 'token_out', 'token_out_not', 'token_out_gt', 'token_out_lt', 'token_out_gte', 'token_out_lte', 'token_out_in', 'token_out_not_in', 'token_out_contains', 'token_out_not_contains', 'token_out_sym', 'token_out_sym_not', 'token_out_sym_gt', 'token_out_sym_lt', 'token_out_sym_gte', 'token_out_sym_lte', 'token_out_sym_in', 'token_out_sym_not_in', 'token_out_sym_contains', 'token_out_sym_contains_nocase', 'token_out_sym_not_contains', 'token_out_sym_not_contains_nocase', 'token_out_sym_starts_with', 'token_out_sym_starts_with_nocase', 'token_out_sym_not_starts_with', 'token_out_sym_not_starts_with_nocase', 'token_out_sym_ends_with', 'token_out_sym_ends_with_nocase', 'token_out_sym_not_ends_with', 'token_out_sym_not_ends_with_nocase', 'token_amount_in', 'token_amount_in_not', 'token_amount_in_gt', 'token_amount_in_lt', 'token_amount_in_gte', 'token_amount_in_lte', 'token_amount_in_in', 'token_amount_in_not_in', 'token_amount_out', 'token_amount_out_not', 'token_amount_out_gt', 'token_amount_out_lt', 'token_amount_out_gte', 'token_amount_out_lte', 'token_amount_out_in', 'token_amount_out_not_in', 'value_usd', 'value_usd_not', 'value_usd_gt', 'value_usd_lt', 'value_usd_gte', 'value_usd_lte', 'value_usd_in', 'value_usd_not_in', 'pool_id', 'pool_id_not', 'pool_id_gt', 'pool_id_lt', 'pool_id_gte', 'pool_id_lte', 'pool_id_in', 'pool_id_not_in', 'pool_id_contains', 'pool_id_contains_nocase', 'pool_id_not_contains', 'pool_id_not_contains_nocase', 'pool_id_starts_with', 'pool_id_starts_with_nocase', 'pool_id_not_starts_with', 'pool_id_not_starts_with_nocase', 'pool_id_ends_with', 'pool_id_ends_with_nocase', 'pool_id_not_ends_with', 'pool_id_not_ends_with_nocase', 'pool_id_', 'user_address', 'user_address_not', 'user_address_gt', 'user_address_lt', 'user_address_gte', 'user_address_lte', 'user_address_in', 'user_address_not_in', 'user_address_contains', 'user_address_contains_nocase', 'user_address_not_contains', 'user_address_not_contains_nocase', 'user_address_starts_with', 'user_address_starts_with_nocase', 'user_address_not_starts_with', 'user_address_not_starts_with_nocase', 'user_address_ends_with', 'user_address_ends_with_nocase', 'user_address_not_ends_with', 'user_address_not_ends_with_nocase', 'user_address_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'tx', 'tx_not', 'tx_gt', 'tx_lt', 'tx_gte', 'tx_lte', 'tx_in', 'tx_not_in', 'tx_contains', 'tx_not_contains', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    caller = sgqlc.types.Field(Bytes, graphql_name='caller')
    caller_not = sgqlc.types.Field(Bytes, graphql_name='caller_not')
    caller_gt = sgqlc.types.Field(Bytes, graphql_name='caller_gt')
    caller_lt = sgqlc.types.Field(Bytes, graphql_name='caller_lt')
    caller_gte = sgqlc.types.Field(Bytes, graphql_name='caller_gte')
    caller_lte = sgqlc.types.Field(Bytes, graphql_name='caller_lte')
    caller_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='caller_in')
    caller_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='caller_not_in')
    caller_contains = sgqlc.types.Field(Bytes, graphql_name='caller_contains')
    caller_not_contains = sgqlc.types.Field(Bytes, graphql_name='caller_not_contains')
    token_in = sgqlc.types.Field(Bytes, graphql_name='tokenIn')
    token_in_not = sgqlc.types.Field(Bytes, graphql_name='tokenIn_not')
    token_in_gt = sgqlc.types.Field(Bytes, graphql_name='tokenIn_gt')
    token_in_lt = sgqlc.types.Field(Bytes, graphql_name='tokenIn_lt')
    token_in_gte = sgqlc.types.Field(Bytes, graphql_name='tokenIn_gte')
    token_in_lte = sgqlc.types.Field(Bytes, graphql_name='tokenIn_lte')
    token_in_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenIn_in')
    token_in_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenIn_not_in')
    token_in_contains = sgqlc.types.Field(Bytes, graphql_name='tokenIn_contains')
    token_in_not_contains = sgqlc.types.Field(Bytes, graphql_name='tokenIn_not_contains')
    token_in_sym = sgqlc.types.Field(String, graphql_name='tokenInSym')
    token_in_sym_not = sgqlc.types.Field(String, graphql_name='tokenInSym_not')
    token_in_sym_gt = sgqlc.types.Field(String, graphql_name='tokenInSym_gt')
    token_in_sym_lt = sgqlc.types.Field(String, graphql_name='tokenInSym_lt')
    token_in_sym_gte = sgqlc.types.Field(String, graphql_name='tokenInSym_gte')
    token_in_sym_lte = sgqlc.types.Field(String, graphql_name='tokenInSym_lte')
    token_in_sym_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenInSym_in')
    token_in_sym_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenInSym_not_in')
    token_in_sym_contains = sgqlc.types.Field(String, graphql_name='tokenInSym_contains')
    token_in_sym_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenInSym_contains_nocase')
    token_in_sym_not_contains = sgqlc.types.Field(String, graphql_name='tokenInSym_not_contains')
    token_in_sym_not_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenInSym_not_contains_nocase')
    token_in_sym_starts_with = sgqlc.types.Field(String, graphql_name='tokenInSym_starts_with')
    token_in_sym_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenInSym_starts_with_nocase')
    token_in_sym_not_starts_with = sgqlc.types.Field(String, graphql_name='tokenInSym_not_starts_with')
    token_in_sym_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenInSym_not_starts_with_nocase')
    token_in_sym_ends_with = sgqlc.types.Field(String, graphql_name='tokenInSym_ends_with')
    token_in_sym_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenInSym_ends_with_nocase')
    token_in_sym_not_ends_with = sgqlc.types.Field(String, graphql_name='tokenInSym_not_ends_with')
    token_in_sym_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenInSym_not_ends_with_nocase')
    token_out = sgqlc.types.Field(Bytes, graphql_name='tokenOut')
    token_out_not = sgqlc.types.Field(Bytes, graphql_name='tokenOut_not')
    token_out_gt = sgqlc.types.Field(Bytes, graphql_name='tokenOut_gt')
    token_out_lt = sgqlc.types.Field(Bytes, graphql_name='tokenOut_lt')
    token_out_gte = sgqlc.types.Field(Bytes, graphql_name='tokenOut_gte')
    token_out_lte = sgqlc.types.Field(Bytes, graphql_name='tokenOut_lte')
    token_out_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenOut_in')
    token_out_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tokenOut_not_in')
    token_out_contains = sgqlc.types.Field(Bytes, graphql_name='tokenOut_contains')
    token_out_not_contains = sgqlc.types.Field(Bytes, graphql_name='tokenOut_not_contains')
    token_out_sym = sgqlc.types.Field(String, graphql_name='tokenOutSym')
    token_out_sym_not = sgqlc.types.Field(String, graphql_name='tokenOutSym_not')
    token_out_sym_gt = sgqlc.types.Field(String, graphql_name='tokenOutSym_gt')
    token_out_sym_lt = sgqlc.types.Field(String, graphql_name='tokenOutSym_lt')
    token_out_sym_gte = sgqlc.types.Field(String, graphql_name='tokenOutSym_gte')
    token_out_sym_lte = sgqlc.types.Field(String, graphql_name='tokenOutSym_lte')
    token_out_sym_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenOutSym_in')
    token_out_sym_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenOutSym_not_in')
    token_out_sym_contains = sgqlc.types.Field(String, graphql_name='tokenOutSym_contains')
    token_out_sym_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenOutSym_contains_nocase')
    token_out_sym_not_contains = sgqlc.types.Field(String, graphql_name='tokenOutSym_not_contains')
    token_out_sym_not_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenOutSym_not_contains_nocase')
    token_out_sym_starts_with = sgqlc.types.Field(String, graphql_name='tokenOutSym_starts_with')
    token_out_sym_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenOutSym_starts_with_nocase')
    token_out_sym_not_starts_with = sgqlc.types.Field(String, graphql_name='tokenOutSym_not_starts_with')
    token_out_sym_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenOutSym_not_starts_with_nocase')
    token_out_sym_ends_with = sgqlc.types.Field(String, graphql_name='tokenOutSym_ends_with')
    token_out_sym_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenOutSym_ends_with_nocase')
    token_out_sym_not_ends_with = sgqlc.types.Field(String, graphql_name='tokenOutSym_not_ends_with')
    token_out_sym_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenOutSym_not_ends_with_nocase')
    token_amount_in = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountIn')
    token_amount_in_not = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountIn_not')
    token_amount_in_gt = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountIn_gt')
    token_amount_in_lt = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountIn_lt')
    token_amount_in_gte = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountIn_gte')
    token_amount_in_lte = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountIn_lte')
    token_amount_in_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tokenAmountIn_in')
    token_amount_in_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tokenAmountIn_not_in')
    token_amount_out = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountOut')
    token_amount_out_not = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountOut_not')
    token_amount_out_gt = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountOut_gt')
    token_amount_out_lt = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountOut_lt')
    token_amount_out_gte = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountOut_gte')
    token_amount_out_lte = sgqlc.types.Field(BigDecimal, graphql_name='tokenAmountOut_lte')
    token_amount_out_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tokenAmountOut_in')
    token_amount_out_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='tokenAmountOut_not_in')
    value_usd = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD')
    value_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_not')
    value_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_gt')
    value_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_lt')
    value_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_gte')
    value_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD_lte')
    value_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='valueUSD_in')
    value_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='valueUSD_not_in')
    pool_id = sgqlc.types.Field(String, graphql_name='poolId')
    pool_id_not = sgqlc.types.Field(String, graphql_name='poolId_not')
    pool_id_gt = sgqlc.types.Field(String, graphql_name='poolId_gt')
    pool_id_lt = sgqlc.types.Field(String, graphql_name='poolId_lt')
    pool_id_gte = sgqlc.types.Field(String, graphql_name='poolId_gte')
    pool_id_lte = sgqlc.types.Field(String, graphql_name='poolId_lte')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_in')
    pool_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_not_in')
    pool_id_contains = sgqlc.types.Field(String, graphql_name='poolId_contains')
    pool_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_contains_nocase')
    pool_id_not_contains = sgqlc.types.Field(String, graphql_name='poolId_not_contains')
    pool_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_contains_nocase')
    pool_id_starts_with = sgqlc.types.Field(String, graphql_name='poolId_starts_with')
    pool_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_starts_with_nocase')
    pool_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with')
    pool_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with_nocase')
    pool_id_ends_with = sgqlc.types.Field(String, graphql_name='poolId_ends_with')
    pool_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_ends_with_nocase')
    pool_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with')
    pool_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with_nocase')
    pool_id_ = sgqlc.types.Field(Pool_filter, graphql_name='poolId_')
    user_address = sgqlc.types.Field(String, graphql_name='userAddress')
    user_address_not = sgqlc.types.Field(String, graphql_name='userAddress_not')
    user_address_gt = sgqlc.types.Field(String, graphql_name='userAddress_gt')
    user_address_lt = sgqlc.types.Field(String, graphql_name='userAddress_lt')
    user_address_gte = sgqlc.types.Field(String, graphql_name='userAddress_gte')
    user_address_lte = sgqlc.types.Field(String, graphql_name='userAddress_lte')
    user_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userAddress_in')
    user_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userAddress_not_in')
    user_address_contains = sgqlc.types.Field(String, graphql_name='userAddress_contains')
    user_address_contains_nocase = sgqlc.types.Field(String, graphql_name='userAddress_contains_nocase')
    user_address_not_contains = sgqlc.types.Field(String, graphql_name='userAddress_not_contains')
    user_address_not_contains_nocase = sgqlc.types.Field(String, graphql_name='userAddress_not_contains_nocase')
    user_address_starts_with = sgqlc.types.Field(String, graphql_name='userAddress_starts_with')
    user_address_starts_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_starts_with_nocase')
    user_address_not_starts_with = sgqlc.types.Field(String, graphql_name='userAddress_not_starts_with')
    user_address_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_not_starts_with_nocase')
    user_address_ends_with = sgqlc.types.Field(String, graphql_name='userAddress_ends_with')
    user_address_ends_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_ends_with_nocase')
    user_address_not_ends_with = sgqlc.types.Field(String, graphql_name='userAddress_not_ends_with')
    user_address_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_not_ends_with_nocase')
    user_address_ = sgqlc.types.Field('User_filter', graphql_name='userAddress_')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(Int, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(Int, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(Int, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(Int, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(Int, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    tx = sgqlc.types.Field(Bytes, graphql_name='tx')
    tx_not = sgqlc.types.Field(Bytes, graphql_name='tx_not')
    tx_gt = sgqlc.types.Field(Bytes, graphql_name='tx_gt')
    tx_lt = sgqlc.types.Field(Bytes, graphql_name='tx_lt')
    tx_gte = sgqlc.types.Field(Bytes, graphql_name='tx_gte')
    tx_lte = sgqlc.types.Field(Bytes, graphql_name='tx_lte')
    tx_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tx_in')
    tx_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='tx_not_in')
    tx_contains = sgqlc.types.Field(Bytes, graphql_name='tx_contains')
    tx_not_contains = sgqlc.types.Field(Bytes, graphql_name='tx_not_contains')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Swap_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Swap_filter'), graphql_name='or')


class TokenPrice_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pool_id', 'pool_id_not', 'pool_id_gt', 'pool_id_lt', 'pool_id_gte', 'pool_id_lte', 'pool_id_in', 'pool_id_not_in', 'pool_id_contains', 'pool_id_contains_nocase', 'pool_id_not_contains', 'pool_id_not_contains_nocase', 'pool_id_starts_with', 'pool_id_starts_with_nocase', 'pool_id_not_starts_with', 'pool_id_not_starts_with_nocase', 'pool_id_ends_with', 'pool_id_ends_with_nocase', 'pool_id_not_ends_with', 'pool_id_not_ends_with_nocase', 'pool_id_', 'asset', 'asset_not', 'asset_gt', 'asset_lt', 'asset_gte', 'asset_lte', 'asset_in', 'asset_not_in', 'asset_contains', 'asset_not_contains', 'amount', 'amount_not', 'amount_gt', 'amount_lt', 'amount_gte', 'amount_lte', 'amount_in', 'amount_not_in', 'pricing_asset', 'pricing_asset_not', 'pricing_asset_gt', 'pricing_asset_lt', 'pricing_asset_gte', 'pricing_asset_lte', 'pricing_asset_in', 'pricing_asset_not_in', 'pricing_asset_contains', 'pricing_asset_not_contains', 'price', 'price_not', 'price_gt', 'price_lt', 'price_gte', 'price_lte', 'price_in', 'price_not_in', 'block', 'block_not', 'block_gt', 'block_lt', 'block_gte', 'block_lte', 'block_in', 'block_not_in', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pool_id = sgqlc.types.Field(String, graphql_name='poolId')
    pool_id_not = sgqlc.types.Field(String, graphql_name='poolId_not')
    pool_id_gt = sgqlc.types.Field(String, graphql_name='poolId_gt')
    pool_id_lt = sgqlc.types.Field(String, graphql_name='poolId_lt')
    pool_id_gte = sgqlc.types.Field(String, graphql_name='poolId_gte')
    pool_id_lte = sgqlc.types.Field(String, graphql_name='poolId_lte')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_in')
    pool_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolId_not_in')
    pool_id_contains = sgqlc.types.Field(String, graphql_name='poolId_contains')
    pool_id_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_contains_nocase')
    pool_id_not_contains = sgqlc.types.Field(String, graphql_name='poolId_not_contains')
    pool_id_not_contains_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_contains_nocase')
    pool_id_starts_with = sgqlc.types.Field(String, graphql_name='poolId_starts_with')
    pool_id_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_starts_with_nocase')
    pool_id_not_starts_with = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with')
    pool_id_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_starts_with_nocase')
    pool_id_ends_with = sgqlc.types.Field(String, graphql_name='poolId_ends_with')
    pool_id_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_ends_with_nocase')
    pool_id_not_ends_with = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with')
    pool_id_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='poolId_not_ends_with_nocase')
    pool_id_ = sgqlc.types.Field(Pool_filter, graphql_name='poolId_')
    asset = sgqlc.types.Field(Bytes, graphql_name='asset')
    asset_not = sgqlc.types.Field(Bytes, graphql_name='asset_not')
    asset_gt = sgqlc.types.Field(Bytes, graphql_name='asset_gt')
    asset_lt = sgqlc.types.Field(Bytes, graphql_name='asset_lt')
    asset_gte = sgqlc.types.Field(Bytes, graphql_name='asset_gte')
    asset_lte = sgqlc.types.Field(Bytes, graphql_name='asset_lte')
    asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='asset_in')
    asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='asset_not_in')
    asset_contains = sgqlc.types.Field(Bytes, graphql_name='asset_contains')
    asset_not_contains = sgqlc.types.Field(Bytes, graphql_name='asset_not_contains')
    amount = sgqlc.types.Field(BigDecimal, graphql_name='amount')
    amount_not = sgqlc.types.Field(BigDecimal, graphql_name='amount_not')
    amount_gt = sgqlc.types.Field(BigDecimal, graphql_name='amount_gt')
    amount_lt = sgqlc.types.Field(BigDecimal, graphql_name='amount_lt')
    amount_gte = sgqlc.types.Field(BigDecimal, graphql_name='amount_gte')
    amount_lte = sgqlc.types.Field(BigDecimal, graphql_name='amount_lte')
    amount_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount_in')
    amount_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='amount_not_in')
    pricing_asset = sgqlc.types.Field(Bytes, graphql_name='pricingAsset')
    pricing_asset_not = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_not')
    pricing_asset_gt = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_gt')
    pricing_asset_lt = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_lt')
    pricing_asset_gte = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_gte')
    pricing_asset_lte = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_lte')
    pricing_asset_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='pricingAsset_in')
    pricing_asset_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='pricingAsset_not_in')
    pricing_asset_contains = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_contains')
    pricing_asset_not_contains = sgqlc.types.Field(Bytes, graphql_name='pricingAsset_not_contains')
    price = sgqlc.types.Field(BigDecimal, graphql_name='price')
    price_not = sgqlc.types.Field(BigDecimal, graphql_name='price_not')
    price_gt = sgqlc.types.Field(BigDecimal, graphql_name='price_gt')
    price_lt = sgqlc.types.Field(BigDecimal, graphql_name='price_lt')
    price_gte = sgqlc.types.Field(BigDecimal, graphql_name='price_gte')
    price_lte = sgqlc.types.Field(BigDecimal, graphql_name='price_lte')
    price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='price_in')
    price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='price_not_in')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    block_not = sgqlc.types.Field(BigInt, graphql_name='block_not')
    block_gt = sgqlc.types.Field(BigInt, graphql_name='block_gt')
    block_lt = sgqlc.types.Field(BigInt, graphql_name='block_lt')
    block_gte = sgqlc.types.Field(BigInt, graphql_name='block_gte')
    block_lte = sgqlc.types.Field(BigInt, graphql_name='block_lte')
    block_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_in')
    block_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='block_not_in')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(Int, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(Int, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(Int, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(Int, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(Int, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('TokenPrice_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('TokenPrice_filter'), graphql_name='or')


class TokenSnapshot_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_contains_nocase', 'token_not_contains', 'token_not_contains_nocase', 'token_starts_with', 'token_starts_with_nocase', 'token_not_starts_with', 'token_not_starts_with_nocase', 'token_ends_with', 'token_ends_with_nocase', 'token_not_ends_with', 'token_not_ends_with_nocase', 'token_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'total_balance_usd', 'total_balance_usd_not', 'total_balance_usd_gt', 'total_balance_usd_lt', 'total_balance_usd_gte', 'total_balance_usd_lte', 'total_balance_usd_in', 'total_balance_usd_not_in', 'total_balance_notional', 'total_balance_notional_not', 'total_balance_notional_gt', 'total_balance_notional_lt', 'total_balance_notional_gte', 'total_balance_notional_lte', 'total_balance_notional_in', 'total_balance_notional_not_in', 'total_volume_usd', 'total_volume_usd_not', 'total_volume_usd_gt', 'total_volume_usd_lt', 'total_volume_usd_gte', 'total_volume_usd_lte', 'total_volume_usd_in', 'total_volume_usd_not_in', 'total_volume_notional', 'total_volume_notional_not', 'total_volume_notional_gt', 'total_volume_notional_lt', 'total_volume_notional_gte', 'total_volume_notional_lte', 'total_volume_notional_in', 'total_volume_notional_not_in', 'total_swap_count', 'total_swap_count_not', 'total_swap_count_gt', 'total_swap_count_lt', 'total_swap_count_gte', 'total_swap_count_lte', 'total_swap_count_in', 'total_swap_count_not_in', '_change_block', 'and_', 'or_')
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
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(Int, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(Int, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(Int, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(Int, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(Int, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_not_in')
    total_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD')
    total_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_not')
    total_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_gt')
    total_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_lt')
    total_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_gte')
    total_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_lte')
    total_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBalanceUSD_in')
    total_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBalanceUSD_not_in')
    total_balance_notional = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional')
    total_balance_notional_not = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_not')
    total_balance_notional_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_gt')
    total_balance_notional_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_lt')
    total_balance_notional_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_gte')
    total_balance_notional_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_lte')
    total_balance_notional_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBalanceNotional_in')
    total_balance_notional_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBalanceNotional_not_in')
    total_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD')
    total_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_not')
    total_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_gt')
    total_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_lt')
    total_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_gte')
    total_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_lte')
    total_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeUSD_in')
    total_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeUSD_not_in')
    total_volume_notional = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional')
    total_volume_notional_not = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_not')
    total_volume_notional_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_gt')
    total_volume_notional_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_lt')
    total_volume_notional_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_gte')
    total_volume_notional_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_lte')
    total_volume_notional_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeNotional_in')
    total_volume_notional_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeNotional_not_in')
    total_swap_count = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount')
    total_swap_count_not = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_not')
    total_swap_count_gt = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_gt')
    total_swap_count_lt = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_lt')
    total_swap_count_gte = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_gte')
    total_swap_count_lte = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_lte')
    total_swap_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSwapCount_in')
    total_swap_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSwapCount_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('TokenSnapshot_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('TokenSnapshot_filter'), graphql_name='or')


class Token_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'symbol', 'symbol_not', 'symbol_gt', 'symbol_lt', 'symbol_gte', 'symbol_lte', 'symbol_in', 'symbol_not_in', 'symbol_contains', 'symbol_contains_nocase', 'symbol_not_contains', 'symbol_not_contains_nocase', 'symbol_starts_with', 'symbol_starts_with_nocase', 'symbol_not_starts_with', 'symbol_not_starts_with_nocase', 'symbol_ends_with', 'symbol_ends_with_nocase', 'symbol_not_ends_with', 'symbol_not_ends_with_nocase', 'name', 'name_not', 'name_gt', 'name_lt', 'name_gte', 'name_lte', 'name_in', 'name_not_in', 'name_contains', 'name_contains_nocase', 'name_not_contains', 'name_not_contains_nocase', 'name_starts_with', 'name_starts_with_nocase', 'name_not_starts_with', 'name_not_starts_with_nocase', 'name_ends_with', 'name_ends_with_nocase', 'name_not_ends_with', 'name_not_ends_with_nocase', 'decimals', 'decimals_not', 'decimals_gt', 'decimals_lt', 'decimals_gte', 'decimals_lte', 'decimals_in', 'decimals_not_in', 'address', 'address_not', 'address_gt', 'address_lt', 'address_gte', 'address_lte', 'address_in', 'address_not_in', 'address_contains', 'address_contains_nocase', 'address_not_contains', 'address_not_contains_nocase', 'address_starts_with', 'address_starts_with_nocase', 'address_not_starts_with', 'address_not_starts_with_nocase', 'address_ends_with', 'address_ends_with_nocase', 'address_not_ends_with', 'address_not_ends_with_nocase', 'total_balance_usd', 'total_balance_usd_not', 'total_balance_usd_gt', 'total_balance_usd_lt', 'total_balance_usd_gte', 'total_balance_usd_lte', 'total_balance_usd_in', 'total_balance_usd_not_in', 'total_balance_notional', 'total_balance_notional_not', 'total_balance_notional_gt', 'total_balance_notional_lt', 'total_balance_notional_gte', 'total_balance_notional_lte', 'total_balance_notional_in', 'total_balance_notional_not_in', 'total_volume_usd', 'total_volume_usd_not', 'total_volume_usd_gt', 'total_volume_usd_lt', 'total_volume_usd_gte', 'total_volume_usd_lte', 'total_volume_usd_in', 'total_volume_usd_not_in', 'total_volume_notional', 'total_volume_notional_not', 'total_volume_notional_gt', 'total_volume_notional_lt', 'total_volume_notional_gte', 'total_volume_notional_lte', 'total_volume_notional_in', 'total_volume_notional_not_in', 'total_swap_count', 'total_swap_count_not', 'total_swap_count_gt', 'total_swap_count_lt', 'total_swap_count_gte', 'total_swap_count_lte', 'total_swap_count_in', 'total_swap_count_not_in', 'latest_price', 'latest_price_not', 'latest_price_gt', 'latest_price_lt', 'latest_price_gte', 'latest_price_lte', 'latest_price_in', 'latest_price_not_in', 'latest_price_contains', 'latest_price_contains_nocase', 'latest_price_not_contains', 'latest_price_not_contains_nocase', 'latest_price_starts_with', 'latest_price_starts_with_nocase', 'latest_price_not_starts_with', 'latest_price_not_starts_with_nocase', 'latest_price_ends_with', 'latest_price_ends_with_nocase', 'latest_price_not_ends_with', 'latest_price_not_ends_with_nocase', 'latest_price_', 'latest_usdprice', 'latest_usdprice_not', 'latest_usdprice_gt', 'latest_usdprice_lt', 'latest_usdprice_gte', 'latest_usdprice_lte', 'latest_usdprice_in', 'latest_usdprice_not_in', 'latest_usdprice_timestamp', 'latest_usdprice_timestamp_not', 'latest_usdprice_timestamp_gt', 'latest_usdprice_timestamp_lt', 'latest_usdprice_timestamp_gte', 'latest_usdprice_timestamp_lte', 'latest_usdprice_timestamp_in', 'latest_usdprice_timestamp_not_in', 'latest_fxprice', 'latest_fxprice_not', 'latest_fxprice_gt', 'latest_fxprice_lt', 'latest_fxprice_gte', 'latest_fxprice_lte', 'latest_fxprice_in', 'latest_fxprice_not_in', 'pool', 'pool_not', 'pool_gt', 'pool_lt', 'pool_gte', 'pool_lte', 'pool_in', 'pool_not_in', 'pool_contains', 'pool_contains_nocase', 'pool_not_contains', 'pool_not_contains_nocase', 'pool_starts_with', 'pool_starts_with_nocase', 'pool_not_starts_with', 'pool_not_starts_with_nocase', 'pool_ends_with', 'pool_ends_with_nocase', 'pool_not_ends_with', 'pool_not_ends_with_nocase', 'pool_', 'fx_oracle_decimals', 'fx_oracle_decimals_not', 'fx_oracle_decimals_gt', 'fx_oracle_decimals_lt', 'fx_oracle_decimals_gte', 'fx_oracle_decimals_lte', 'fx_oracle_decimals_in', 'fx_oracle_decimals_not_in', '_change_block', 'and_', 'or_')
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
    decimals = sgqlc.types.Field(Int, graphql_name='decimals')
    decimals_not = sgqlc.types.Field(Int, graphql_name='decimals_not')
    decimals_gt = sgqlc.types.Field(Int, graphql_name='decimals_gt')
    decimals_lt = sgqlc.types.Field(Int, graphql_name='decimals_lt')
    decimals_gte = sgqlc.types.Field(Int, graphql_name='decimals_gte')
    decimals_lte = sgqlc.types.Field(Int, graphql_name='decimals_lte')
    decimals_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='decimals_in')
    decimals_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='decimals_not_in')
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
    total_balance_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD')
    total_balance_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_not')
    total_balance_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_gt')
    total_balance_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_lt')
    total_balance_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_gte')
    total_balance_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceUSD_lte')
    total_balance_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBalanceUSD_in')
    total_balance_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBalanceUSD_not_in')
    total_balance_notional = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional')
    total_balance_notional_not = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_not')
    total_balance_notional_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_gt')
    total_balance_notional_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_lt')
    total_balance_notional_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_gte')
    total_balance_notional_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalBalanceNotional_lte')
    total_balance_notional_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBalanceNotional_in')
    total_balance_notional_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalBalanceNotional_not_in')
    total_volume_usd = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD')
    total_volume_usd_not = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_not')
    total_volume_usd_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_gt')
    total_volume_usd_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_lt')
    total_volume_usd_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_gte')
    total_volume_usd_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeUSD_lte')
    total_volume_usd_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeUSD_in')
    total_volume_usd_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeUSD_not_in')
    total_volume_notional = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional')
    total_volume_notional_not = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_not')
    total_volume_notional_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_gt')
    total_volume_notional_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_lt')
    total_volume_notional_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_gte')
    total_volume_notional_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalVolumeNotional_lte')
    total_volume_notional_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeNotional_in')
    total_volume_notional_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalVolumeNotional_not_in')
    total_swap_count = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount')
    total_swap_count_not = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_not')
    total_swap_count_gt = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_gt')
    total_swap_count_lt = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_lt')
    total_swap_count_gte = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_gte')
    total_swap_count_lte = sgqlc.types.Field(BigInt, graphql_name='totalSwapCount_lte')
    total_swap_count_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSwapCount_in')
    total_swap_count_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='totalSwapCount_not_in')
    latest_price = sgqlc.types.Field(String, graphql_name='latestPrice')
    latest_price_not = sgqlc.types.Field(String, graphql_name='latestPrice_not')
    latest_price_gt = sgqlc.types.Field(String, graphql_name='latestPrice_gt')
    latest_price_lt = sgqlc.types.Field(String, graphql_name='latestPrice_lt')
    latest_price_gte = sgqlc.types.Field(String, graphql_name='latestPrice_gte')
    latest_price_lte = sgqlc.types.Field(String, graphql_name='latestPrice_lte')
    latest_price_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='latestPrice_in')
    latest_price_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='latestPrice_not_in')
    latest_price_contains = sgqlc.types.Field(String, graphql_name='latestPrice_contains')
    latest_price_contains_nocase = sgqlc.types.Field(String, graphql_name='latestPrice_contains_nocase')
    latest_price_not_contains = sgqlc.types.Field(String, graphql_name='latestPrice_not_contains')
    latest_price_not_contains_nocase = sgqlc.types.Field(String, graphql_name='latestPrice_not_contains_nocase')
    latest_price_starts_with = sgqlc.types.Field(String, graphql_name='latestPrice_starts_with')
    latest_price_starts_with_nocase = sgqlc.types.Field(String, graphql_name='latestPrice_starts_with_nocase')
    latest_price_not_starts_with = sgqlc.types.Field(String, graphql_name='latestPrice_not_starts_with')
    latest_price_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='latestPrice_not_starts_with_nocase')
    latest_price_ends_with = sgqlc.types.Field(String, graphql_name='latestPrice_ends_with')
    latest_price_ends_with_nocase = sgqlc.types.Field(String, graphql_name='latestPrice_ends_with_nocase')
    latest_price_not_ends_with = sgqlc.types.Field(String, graphql_name='latestPrice_not_ends_with')
    latest_price_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='latestPrice_not_ends_with_nocase')
    latest_price_ = sgqlc.types.Field(LatestPrice_filter, graphql_name='latestPrice_')
    latest_usdprice = sgqlc.types.Field(BigDecimal, graphql_name='latestUSDPrice')
    latest_usdprice_not = sgqlc.types.Field(BigDecimal, graphql_name='latestUSDPrice_not')
    latest_usdprice_gt = sgqlc.types.Field(BigDecimal, graphql_name='latestUSDPrice_gt')
    latest_usdprice_lt = sgqlc.types.Field(BigDecimal, graphql_name='latestUSDPrice_lt')
    latest_usdprice_gte = sgqlc.types.Field(BigDecimal, graphql_name='latestUSDPrice_gte')
    latest_usdprice_lte = sgqlc.types.Field(BigDecimal, graphql_name='latestUSDPrice_lte')
    latest_usdprice_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='latestUSDPrice_in')
    latest_usdprice_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='latestUSDPrice_not_in')
    latest_usdprice_timestamp = sgqlc.types.Field(BigInt, graphql_name='latestUSDPriceTimestamp')
    latest_usdprice_timestamp_not = sgqlc.types.Field(BigInt, graphql_name='latestUSDPriceTimestamp_not')
    latest_usdprice_timestamp_gt = sgqlc.types.Field(BigInt, graphql_name='latestUSDPriceTimestamp_gt')
    latest_usdprice_timestamp_lt = sgqlc.types.Field(BigInt, graphql_name='latestUSDPriceTimestamp_lt')
    latest_usdprice_timestamp_gte = sgqlc.types.Field(BigInt, graphql_name='latestUSDPriceTimestamp_gte')
    latest_usdprice_timestamp_lte = sgqlc.types.Field(BigInt, graphql_name='latestUSDPriceTimestamp_lte')
    latest_usdprice_timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='latestUSDPriceTimestamp_in')
    latest_usdprice_timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigInt)), graphql_name='latestUSDPriceTimestamp_not_in')
    latest_fxprice = sgqlc.types.Field(BigDecimal, graphql_name='latestFXPrice')
    latest_fxprice_not = sgqlc.types.Field(BigDecimal, graphql_name='latestFXPrice_not')
    latest_fxprice_gt = sgqlc.types.Field(BigDecimal, graphql_name='latestFXPrice_gt')
    latest_fxprice_lt = sgqlc.types.Field(BigDecimal, graphql_name='latestFXPrice_lt')
    latest_fxprice_gte = sgqlc.types.Field(BigDecimal, graphql_name='latestFXPrice_gte')
    latest_fxprice_lte = sgqlc.types.Field(BigDecimal, graphql_name='latestFXPrice_lte')
    latest_fxprice_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='latestFXPrice_in')
    latest_fxprice_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='latestFXPrice_not_in')
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
    fx_oracle_decimals = sgqlc.types.Field(Int, graphql_name='fxOracleDecimals')
    fx_oracle_decimals_not = sgqlc.types.Field(Int, graphql_name='fxOracleDecimals_not')
    fx_oracle_decimals_gt = sgqlc.types.Field(Int, graphql_name='fxOracleDecimals_gt')
    fx_oracle_decimals_lt = sgqlc.types.Field(Int, graphql_name='fxOracleDecimals_lt')
    fx_oracle_decimals_gte = sgqlc.types.Field(Int, graphql_name='fxOracleDecimals_gte')
    fx_oracle_decimals_lte = sgqlc.types.Field(Int, graphql_name='fxOracleDecimals_lte')
    fx_oracle_decimals_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='fxOracleDecimals_in')
    fx_oracle_decimals_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='fxOracleDecimals_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('Token_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('Token_filter'), graphql_name='or')


class TradePairSnapshot_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'pair', 'pair_not', 'pair_gt', 'pair_lt', 'pair_gte', 'pair_lte', 'pair_in', 'pair_not_in', 'pair_contains', 'pair_contains_nocase', 'pair_not_contains', 'pair_not_contains_nocase', 'pair_starts_with', 'pair_starts_with_nocase', 'pair_not_starts_with', 'pair_not_starts_with_nocase', 'pair_ends_with', 'pair_ends_with_nocase', 'pair_not_ends_with', 'pair_not_ends_with_nocase', 'pair_', 'timestamp', 'timestamp_not', 'timestamp_gt', 'timestamp_lt', 'timestamp_gte', 'timestamp_lte', 'timestamp_in', 'timestamp_not_in', 'total_swap_volume', 'total_swap_volume_not', 'total_swap_volume_gt', 'total_swap_volume_lt', 'total_swap_volume_gte', 'total_swap_volume_lte', 'total_swap_volume_in', 'total_swap_volume_not_in', 'total_swap_fee', 'total_swap_fee_not', 'total_swap_fee_gt', 'total_swap_fee_lt', 'total_swap_fee_gte', 'total_swap_fee_lte', 'total_swap_fee_in', 'total_swap_fee_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    pair = sgqlc.types.Field(String, graphql_name='pair')
    pair_not = sgqlc.types.Field(String, graphql_name='pair_not')
    pair_gt = sgqlc.types.Field(String, graphql_name='pair_gt')
    pair_lt = sgqlc.types.Field(String, graphql_name='pair_lt')
    pair_gte = sgqlc.types.Field(String, graphql_name='pair_gte')
    pair_lte = sgqlc.types.Field(String, graphql_name='pair_lte')
    pair_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pair_in')
    pair_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pair_not_in')
    pair_contains = sgqlc.types.Field(String, graphql_name='pair_contains')
    pair_contains_nocase = sgqlc.types.Field(String, graphql_name='pair_contains_nocase')
    pair_not_contains = sgqlc.types.Field(String, graphql_name='pair_not_contains')
    pair_not_contains_nocase = sgqlc.types.Field(String, graphql_name='pair_not_contains_nocase')
    pair_starts_with = sgqlc.types.Field(String, graphql_name='pair_starts_with')
    pair_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pair_starts_with_nocase')
    pair_not_starts_with = sgqlc.types.Field(String, graphql_name='pair_not_starts_with')
    pair_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='pair_not_starts_with_nocase')
    pair_ends_with = sgqlc.types.Field(String, graphql_name='pair_ends_with')
    pair_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pair_ends_with_nocase')
    pair_not_ends_with = sgqlc.types.Field(String, graphql_name='pair_not_ends_with')
    pair_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='pair_not_ends_with_nocase')
    pair_ = sgqlc.types.Field('TradePair_filter', graphql_name='pair_')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')
    timestamp_not = sgqlc.types.Field(Int, graphql_name='timestamp_not')
    timestamp_gt = sgqlc.types.Field(Int, graphql_name='timestamp_gt')
    timestamp_lt = sgqlc.types.Field(Int, graphql_name='timestamp_lt')
    timestamp_gte = sgqlc.types.Field(Int, graphql_name='timestamp_gte')
    timestamp_lte = sgqlc.types.Field(Int, graphql_name='timestamp_lte')
    timestamp_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_in')
    timestamp_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='timestamp_not_in')
    total_swap_volume = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume')
    total_swap_volume_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_not')
    total_swap_volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gt')
    total_swap_volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lt')
    total_swap_volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gte')
    total_swap_volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lte')
    total_swap_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_in')
    total_swap_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_not_in')
    total_swap_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee')
    total_swap_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_not')
    total_swap_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gt')
    total_swap_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lt')
    total_swap_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gte')
    total_swap_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lte')
    total_swap_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_in')
    total_swap_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('TradePairSnapshot_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('TradePairSnapshot_filter'), graphql_name='or')


class TradePair_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'token0', 'token0_not', 'token0_gt', 'token0_lt', 'token0_gte', 'token0_lte', 'token0_in', 'token0_not_in', 'token0_contains', 'token0_contains_nocase', 'token0_not_contains', 'token0_not_contains_nocase', 'token0_starts_with', 'token0_starts_with_nocase', 'token0_not_starts_with', 'token0_not_starts_with_nocase', 'token0_ends_with', 'token0_ends_with_nocase', 'token0_not_ends_with', 'token0_not_ends_with_nocase', 'token0_', 'token1', 'token1_not', 'token1_gt', 'token1_lt', 'token1_gte', 'token1_lte', 'token1_in', 'token1_not_in', 'token1_contains', 'token1_contains_nocase', 'token1_not_contains', 'token1_not_contains_nocase', 'token1_starts_with', 'token1_starts_with_nocase', 'token1_not_starts_with', 'token1_not_starts_with_nocase', 'token1_ends_with', 'token1_ends_with_nocase', 'token1_not_ends_with', 'token1_not_ends_with_nocase', 'token1_', 'total_swap_volume', 'total_swap_volume_not', 'total_swap_volume_gt', 'total_swap_volume_lt', 'total_swap_volume_gte', 'total_swap_volume_lte', 'total_swap_volume_in', 'total_swap_volume_not_in', 'total_swap_fee', 'total_swap_fee_not', 'total_swap_fee_gt', 'total_swap_fee_lt', 'total_swap_fee_gte', 'total_swap_fee_lte', 'total_swap_fee_in', 'total_swap_fee_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
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
    token0_ = sgqlc.types.Field(Token_filter, graphql_name='token0_')
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
    token1_ = sgqlc.types.Field(Token_filter, graphql_name='token1_')
    total_swap_volume = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume')
    total_swap_volume_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_not')
    total_swap_volume_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gt')
    total_swap_volume_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lt')
    total_swap_volume_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_gte')
    total_swap_volume_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapVolume_lte')
    total_swap_volume_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_in')
    total_swap_volume_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapVolume_not_in')
    total_swap_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee')
    total_swap_fee_not = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_not')
    total_swap_fee_gt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gt')
    total_swap_fee_lt = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lt')
    total_swap_fee_gte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_gte')
    total_swap_fee_lte = sgqlc.types.Field(BigDecimal, graphql_name='totalSwapFee_lte')
    total_swap_fee_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_in')
    total_swap_fee_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='totalSwapFee_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('TradePair_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('TradePair_filter'), graphql_name='or')


class UserInternalBalance_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'user_address', 'user_address_not', 'user_address_gt', 'user_address_lt', 'user_address_gte', 'user_address_lte', 'user_address_in', 'user_address_not_in', 'user_address_contains', 'user_address_contains_nocase', 'user_address_not_contains', 'user_address_not_contains_nocase', 'user_address_starts_with', 'user_address_starts_with_nocase', 'user_address_not_starts_with', 'user_address_not_starts_with_nocase', 'user_address_ends_with', 'user_address_ends_with_nocase', 'user_address_not_ends_with', 'user_address_not_ends_with_nocase', 'user_address_', 'token', 'token_not', 'token_gt', 'token_lt', 'token_gte', 'token_lte', 'token_in', 'token_not_in', 'token_contains', 'token_not_contains', 'token_info', 'token_info_not', 'token_info_gt', 'token_info_lt', 'token_info_gte', 'token_info_lte', 'token_info_in', 'token_info_not_in', 'token_info_contains', 'token_info_contains_nocase', 'token_info_not_contains', 'token_info_not_contains_nocase', 'token_info_starts_with', 'token_info_starts_with_nocase', 'token_info_not_starts_with', 'token_info_not_starts_with_nocase', 'token_info_ends_with', 'token_info_ends_with_nocase', 'token_info_not_ends_with', 'token_info_not_ends_with_nocase', 'token_info_', 'balance', 'balance_not', 'balance_gt', 'balance_lt', 'balance_gte', 'balance_lte', 'balance_in', 'balance_not_in', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    user_address = sgqlc.types.Field(String, graphql_name='userAddress')
    user_address_not = sgqlc.types.Field(String, graphql_name='userAddress_not')
    user_address_gt = sgqlc.types.Field(String, graphql_name='userAddress_gt')
    user_address_lt = sgqlc.types.Field(String, graphql_name='userAddress_lt')
    user_address_gte = sgqlc.types.Field(String, graphql_name='userAddress_gte')
    user_address_lte = sgqlc.types.Field(String, graphql_name='userAddress_lte')
    user_address_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userAddress_in')
    user_address_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userAddress_not_in')
    user_address_contains = sgqlc.types.Field(String, graphql_name='userAddress_contains')
    user_address_contains_nocase = sgqlc.types.Field(String, graphql_name='userAddress_contains_nocase')
    user_address_not_contains = sgqlc.types.Field(String, graphql_name='userAddress_not_contains')
    user_address_not_contains_nocase = sgqlc.types.Field(String, graphql_name='userAddress_not_contains_nocase')
    user_address_starts_with = sgqlc.types.Field(String, graphql_name='userAddress_starts_with')
    user_address_starts_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_starts_with_nocase')
    user_address_not_starts_with = sgqlc.types.Field(String, graphql_name='userAddress_not_starts_with')
    user_address_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_not_starts_with_nocase')
    user_address_ends_with = sgqlc.types.Field(String, graphql_name='userAddress_ends_with')
    user_address_ends_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_ends_with_nocase')
    user_address_not_ends_with = sgqlc.types.Field(String, graphql_name='userAddress_not_ends_with')
    user_address_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='userAddress_not_ends_with_nocase')
    user_address_ = sgqlc.types.Field('User_filter', graphql_name='userAddress_')
    token = sgqlc.types.Field(Bytes, graphql_name='token')
    token_not = sgqlc.types.Field(Bytes, graphql_name='token_not')
    token_gt = sgqlc.types.Field(Bytes, graphql_name='token_gt')
    token_lt = sgqlc.types.Field(Bytes, graphql_name='token_lt')
    token_gte = sgqlc.types.Field(Bytes, graphql_name='token_gte')
    token_lte = sgqlc.types.Field(Bytes, graphql_name='token_lte')
    token_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='token_in')
    token_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Bytes)), graphql_name='token_not_in')
    token_contains = sgqlc.types.Field(Bytes, graphql_name='token_contains')
    token_not_contains = sgqlc.types.Field(Bytes, graphql_name='token_not_contains')
    token_info = sgqlc.types.Field(String, graphql_name='tokenInfo')
    token_info_not = sgqlc.types.Field(String, graphql_name='tokenInfo_not')
    token_info_gt = sgqlc.types.Field(String, graphql_name='tokenInfo_gt')
    token_info_lt = sgqlc.types.Field(String, graphql_name='tokenInfo_lt')
    token_info_gte = sgqlc.types.Field(String, graphql_name='tokenInfo_gte')
    token_info_lte = sgqlc.types.Field(String, graphql_name='tokenInfo_lte')
    token_info_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenInfo_in')
    token_info_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenInfo_not_in')
    token_info_contains = sgqlc.types.Field(String, graphql_name='tokenInfo_contains')
    token_info_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenInfo_contains_nocase')
    token_info_not_contains = sgqlc.types.Field(String, graphql_name='tokenInfo_not_contains')
    token_info_not_contains_nocase = sgqlc.types.Field(String, graphql_name='tokenInfo_not_contains_nocase')
    token_info_starts_with = sgqlc.types.Field(String, graphql_name='tokenInfo_starts_with')
    token_info_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenInfo_starts_with_nocase')
    token_info_not_starts_with = sgqlc.types.Field(String, graphql_name='tokenInfo_not_starts_with')
    token_info_not_starts_with_nocase = sgqlc.types.Field(String, graphql_name='tokenInfo_not_starts_with_nocase')
    token_info_ends_with = sgqlc.types.Field(String, graphql_name='tokenInfo_ends_with')
    token_info_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenInfo_ends_with_nocase')
    token_info_not_ends_with = sgqlc.types.Field(String, graphql_name='tokenInfo_not_ends_with')
    token_info_not_ends_with_nocase = sgqlc.types.Field(String, graphql_name='tokenInfo_not_ends_with_nocase')
    token_info_ = sgqlc.types.Field(Token_filter, graphql_name='tokenInfo_')
    balance = sgqlc.types.Field(BigDecimal, graphql_name='balance')
    balance_not = sgqlc.types.Field(BigDecimal, graphql_name='balance_not')
    balance_gt = sgqlc.types.Field(BigDecimal, graphql_name='balance_gt')
    balance_lt = sgqlc.types.Field(BigDecimal, graphql_name='balance_lt')
    balance_gte = sgqlc.types.Field(BigDecimal, graphql_name='balance_gte')
    balance_lte = sgqlc.types.Field(BigDecimal, graphql_name='balance_lte')
    balance_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_in')
    balance_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal)), graphql_name='balance_not_in')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('UserInternalBalance_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('UserInternalBalance_filter'), graphql_name='or')


class User_filter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'id_not', 'id_gt', 'id_lt', 'id_gte', 'id_lte', 'id_in', 'id_not_in', 'shares_owned_', 'swaps_', 'user_internal_balances_', '_change_block', 'and_', 'or_')
    id = sgqlc.types.Field(ID, graphql_name='id')
    id_not = sgqlc.types.Field(ID, graphql_name='id_not')
    id_gt = sgqlc.types.Field(ID, graphql_name='id_gt')
    id_lt = sgqlc.types.Field(ID, graphql_name='id_lt')
    id_gte = sgqlc.types.Field(ID, graphql_name='id_gte')
    id_lte = sgqlc.types.Field(ID, graphql_name='id_lte')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_in')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id_not_in')
    shares_owned_ = sgqlc.types.Field(PoolShare_filter, graphql_name='sharesOwned_')
    swaps_ = sgqlc.types.Field(Swap_filter, graphql_name='swaps_')
    user_internal_balances_ = sgqlc.types.Field(UserInternalBalance_filter, graphql_name='userInternalBalances_')
    _change_block = sgqlc.types.Field(BlockChangedFilter, graphql_name='_change_block')
    and_ = sgqlc.types.Field(sgqlc.types.list_of('User_filter'), graphql_name='and')
    or_ = sgqlc.types.Field(sgqlc.types.list_of('User_filter'), graphql_name='or')



########################################################################
# Output Objects and Interfaces
########################################################################
class AmpUpdate(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_id', 'scheduled_timestamp', 'start_timestamp', 'end_timestamp', 'start_amp', 'end_amp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null('Pool'), graphql_name='poolId')
    scheduled_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='scheduledTimestamp')
    start_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='startTimestamp')
    end_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='endTimestamp')
    start_amp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='startAmp')
    end_amp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='endAmp')


class Balancer(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_count', 'pools', 'snapshots', 'total_liquidity', 'total_swap_count', 'total_swap_volume', 'total_swap_fee', 'total_protocol_fee', 'protocol_fees_collector')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='poolCount')
    pools = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Pool')), graphql_name='pools', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Pool_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Pool_filter, graphql_name='where', default=None)),
))
    )
    snapshots = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('BalancerSnapshot')), graphql_name='snapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(BalancerSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(BalancerSnapshot_filter, graphql_name='where', default=None)),
))
    )
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidity')
    total_swap_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='totalSwapCount')
    total_swap_volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapVolume')
    total_swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapFee')
    total_protocol_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee')
    protocol_fees_collector = sgqlc.types.Field(Bytes, graphql_name='protocolFeesCollector')


class BalancerSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'vault', 'timestamp', 'pool_count', 'total_liquidity', 'total_swap_count', 'total_swap_volume', 'total_swap_fee', 'total_protocol_fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    vault = sgqlc.types.Field(sgqlc.types.non_null(Balancer), graphql_name='vault')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    pool_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='poolCount')
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidity')
    total_swap_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='totalSwapCount')
    total_swap_volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapVolume')
    total_swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapFee')
    total_protocol_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee')


class CircuitBreaker(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool', 'token', 'bpt_price', 'lower_bound_percentage', 'upper_bound_percentage')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool = sgqlc.types.Field(sgqlc.types.non_null('Pool'), graphql_name='pool')
    token = sgqlc.types.Field(sgqlc.types.non_null('PoolToken'), graphql_name='token')
    bpt_price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='bptPrice')
    lower_bound_percentage = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='lowerBoundPercentage')
    upper_bound_percentage = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='upperBoundPercentage')


class FXOracle(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'tokens')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bytes))), graphql_name='tokens')


class GradualWeightUpdate(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_id', 'scheduled_timestamp', 'start_timestamp', 'end_timestamp', 'start_weights', 'end_weights')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null('Pool'), graphql_name='poolId')
    scheduled_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='scheduledTimestamp')
    start_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='startTimestamp')
    end_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='endTimestamp')
    start_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='startWeights')
    end_weights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigInt))), graphql_name='endWeights')


class JoinExit(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'type', 'sender', 'amounts', 'value_usd', 'pool', 'user', 'timestamp', 'tx', 'block')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(InvestType), graphql_name='type')
    sender = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='sender')
    amounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal))), graphql_name='amounts')
    value_usd = sgqlc.types.Field(BigDecimal, graphql_name='valueUSD')
    pool = sgqlc.types.Field(sgqlc.types.non_null('Pool'), graphql_name='pool')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    tx = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='tx')
    block = sgqlc.types.Field(BigInt, graphql_name='block')


class LatestPrice(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'asset', 'pricing_asset', 'pool_id', 'price', 'block')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    asset = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='asset')
    pricing_asset = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='pricingAsset')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null('Pool'), graphql_name='poolId')
    price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='price')
    block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='block')


class ManagementOperation(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'type', 'cash_delta', 'managed_delta', 'pool_token_id', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    type = sgqlc.types.Field(sgqlc.types.non_null(OperationType), graphql_name='type')
    cash_delta = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cashDelta')
    managed_delta = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='managedDelta')
    pool_token_id = sgqlc.types.Field(sgqlc.types.non_null('PoolToken'), graphql_name='poolTokenId')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')


class Pool(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'address', 'pool_type', 'pool_type_version', 'factory', 'strategy_type', 'oracle_enabled', 'symbol', 'name', 'swap_enabled', 'swap_enabled_internal', 'swap_enabled_curation_signal', 'swap_fee', 'owner', 'is_paused', 'total_weight', 'total_swap_volume', 'total_swap_fee', 'total_liquidity', 'total_liquidity_sans_bpt', 'total_shares', 'total_protocol_fee', 'create_time', 'swaps_count', 'holders_count', 'vault_id', 'tx', 'tokens_list', 'tokens', 'joins_exits', 'swaps', 'shares', 'snapshots', 'historical_values', 'weight_updates', 'amp', 'latest_amp_update', 'amp_updates', 'price_rate_providers', 'principal_token', 'base_token', 'expiry_time', 'unit_seconds', 'management_fee', 'join_exit_enabled', 'must_allowlist_lps', 'management_aum_fee', 'total_aum_fee_collected_in_bpt', 'circuit_breakers', 'main_index', 'wrapped_index', 'lower_target', 'upper_target', 'sqrt_alpha', 'sqrt_beta', 'root3_alpha', 'c', 's', 'tau_alpha_x', 'tau_alpha_y', 'tau_beta_x', 'tau_beta_y', 'u', 'v', 'w', 'z', 'd_sq', 'alpha', 'beta', 'lambda_', 'delta', 'epsilon', 'is_in_recovery_mode', 'protocol_swap_fee_cache', 'protocol_yield_fee_cache', 'protocol_aum_fee_cache', 'total_protocol_fee_paid_in_bpt', 'last_join_exit_amp', 'last_post_join_exit_invariant', 'protocol_id', 'protocol_id_data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    pool_type = sgqlc.types.Field(String, graphql_name='poolType')
    pool_type_version = sgqlc.types.Field(Int, graphql_name='poolTypeVersion')
    factory = sgqlc.types.Field(Bytes, graphql_name='factory')
    strategy_type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='strategyType')
    oracle_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='oracleEnabled')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    name = sgqlc.types.Field(String, graphql_name='name')
    swap_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='swapEnabled')
    swap_enabled_internal = sgqlc.types.Field(Boolean, graphql_name='swapEnabledInternal')
    swap_enabled_curation_signal = sgqlc.types.Field(Boolean, graphql_name='swapEnabledCurationSignal')
    swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapFee')
    owner = sgqlc.types.Field(Bytes, graphql_name='owner')
    is_paused = sgqlc.types.Field(Boolean, graphql_name='isPaused')
    total_weight = sgqlc.types.Field(BigDecimal, graphql_name='totalWeight')
    total_swap_volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapVolume')
    total_swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapFee')
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidity')
    total_liquidity_sans_bpt = sgqlc.types.Field(BigDecimal, graphql_name='totalLiquiditySansBPT')
    total_shares = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalShares')
    total_protocol_fee = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFee')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createTime')
    swaps_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='swapsCount')
    holders_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='holdersCount')
    vault_id = sgqlc.types.Field(sgqlc.types.non_null(Balancer), graphql_name='vaultID')
    tx = sgqlc.types.Field(Bytes, graphql_name='tx')
    tokens_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bytes))), graphql_name='tokensList')
    tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PoolToken')), graphql_name='tokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolToken_filter, graphql_name='where', default=None)),
))
    )
    joins_exits = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(JoinExit)), graphql_name='joinsExits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(JoinExit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(JoinExit_filter, graphql_name='where', default=None)),
))
    )
    swaps = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Swap')), graphql_name='swaps', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Swap_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Swap_filter, graphql_name='where', default=None)),
))
    )
    shares = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PoolShare')), graphql_name='shares', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolShare_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolShare_filter, graphql_name='where', default=None)),
))
    )
    snapshots = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PoolSnapshot')), graphql_name='snapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolSnapshot_filter, graphql_name='where', default=None)),
))
    )
    historical_values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PoolHistoricalLiquidity')), graphql_name='historicalValues', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolHistoricalLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolHistoricalLiquidity_filter, graphql_name='where', default=None)),
))
    )
    weight_updates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GradualWeightUpdate)), graphql_name='weightUpdates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GradualWeightUpdate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GradualWeightUpdate_filter, graphql_name='where', default=None)),
))
    )
    amp = sgqlc.types.Field(BigInt, graphql_name='amp')
    latest_amp_update = sgqlc.types.Field(AmpUpdate, graphql_name='latestAmpUpdate')
    amp_updates = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AmpUpdate)), graphql_name='ampUpdates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(AmpUpdate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(AmpUpdate_filter, graphql_name='where', default=None)),
))
    )
    price_rate_providers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PriceRateProvider')), graphql_name='priceRateProviders', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PriceRateProvider_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PriceRateProvider_filter, graphql_name='where', default=None)),
))
    )
    principal_token = sgqlc.types.Field(Bytes, graphql_name='principalToken')
    base_token = sgqlc.types.Field(Bytes, graphql_name='baseToken')
    expiry_time = sgqlc.types.Field(BigInt, graphql_name='expiryTime')
    unit_seconds = sgqlc.types.Field(BigInt, graphql_name='unitSeconds')
    management_fee = sgqlc.types.Field(BigDecimal, graphql_name='managementFee')
    join_exit_enabled = sgqlc.types.Field(Boolean, graphql_name='joinExitEnabled')
    must_allowlist_lps = sgqlc.types.Field(Boolean, graphql_name='mustAllowlistLPs')
    management_aum_fee = sgqlc.types.Field(BigDecimal, graphql_name='managementAumFee')
    total_aum_fee_collected_in_bpt = sgqlc.types.Field(BigDecimal, graphql_name='totalAumFeeCollectedInBPT')
    circuit_breakers = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CircuitBreaker)), graphql_name='circuitBreakers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(CircuitBreaker_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(CircuitBreaker_filter, graphql_name='where', default=None)),
))
    )
    main_index = sgqlc.types.Field(Int, graphql_name='mainIndex')
    wrapped_index = sgqlc.types.Field(Int, graphql_name='wrappedIndex')
    lower_target = sgqlc.types.Field(BigDecimal, graphql_name='lowerTarget')
    upper_target = sgqlc.types.Field(BigDecimal, graphql_name='upperTarget')
    sqrt_alpha = sgqlc.types.Field(BigDecimal, graphql_name='sqrtAlpha')
    sqrt_beta = sgqlc.types.Field(BigDecimal, graphql_name='sqrtBeta')
    root3_alpha = sgqlc.types.Field(BigDecimal, graphql_name='root3Alpha')
    c = sgqlc.types.Field(BigDecimal, graphql_name='c')
    s = sgqlc.types.Field(BigDecimal, graphql_name='s')
    tau_alpha_x = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaX')
    tau_alpha_y = sgqlc.types.Field(BigDecimal, graphql_name='tauAlphaY')
    tau_beta_x = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaX')
    tau_beta_y = sgqlc.types.Field(BigDecimal, graphql_name='tauBetaY')
    u = sgqlc.types.Field(BigDecimal, graphql_name='u')
    v = sgqlc.types.Field(BigDecimal, graphql_name='v')
    w = sgqlc.types.Field(BigDecimal, graphql_name='w')
    z = sgqlc.types.Field(BigDecimal, graphql_name='z')
    d_sq = sgqlc.types.Field(BigDecimal, graphql_name='dSq')
    alpha = sgqlc.types.Field(BigDecimal, graphql_name='alpha')
    beta = sgqlc.types.Field(BigDecimal, graphql_name='beta')
    lambda_ = sgqlc.types.Field(BigDecimal, graphql_name='lambda')
    delta = sgqlc.types.Field(BigDecimal, graphql_name='delta')
    epsilon = sgqlc.types.Field(BigDecimal, graphql_name='epsilon')
    is_in_recovery_mode = sgqlc.types.Field(Boolean, graphql_name='isInRecoveryMode')
    protocol_swap_fee_cache = sgqlc.types.Field(BigDecimal, graphql_name='protocolSwapFeeCache')
    protocol_yield_fee_cache = sgqlc.types.Field(BigDecimal, graphql_name='protocolYieldFeeCache')
    protocol_aum_fee_cache = sgqlc.types.Field(BigDecimal, graphql_name='protocolAumFeeCache')
    total_protocol_fee_paid_in_bpt = sgqlc.types.Field(BigDecimal, graphql_name='totalProtocolFeePaidInBPT')
    last_join_exit_amp = sgqlc.types.Field(BigInt, graphql_name='lastJoinExitAmp')
    last_post_join_exit_invariant = sgqlc.types.Field(BigDecimal, graphql_name='lastPostJoinExitInvariant')
    protocol_id = sgqlc.types.Field(Int, graphql_name='protocolId')
    protocol_id_data = sgqlc.types.Field('ProtocolIdData', graphql_name='protocolIdData')


class PoolContract(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')


class PoolHistoricalLiquidity(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_id', 'pool_total_shares', 'pool_liquidity', 'pool_share_value', 'pricing_asset', 'block')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='poolId')
    pool_total_shares = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='poolTotalShares')
    pool_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='poolLiquidity')
    pool_share_value = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='poolShareValue')
    pricing_asset = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='pricingAsset')
    block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='block')


class PoolShare(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'user_address', 'pool_id', 'balance')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user_address = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='userAddress')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='poolId')
    balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='balance')


class PoolSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool', 'amounts', 'total_shares', 'swap_volume', 'protocol_fee', 'swap_fees', 'liquidity', 'swaps_count', 'holders_count', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')
    amounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BigDecimal))), graphql_name='amounts')
    total_shares = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalShares')
    swap_volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapVolume')
    protocol_fee = sgqlc.types.Field(BigDecimal, graphql_name='protocolFee')
    swap_fees = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapFees')
    liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='liquidity')
    swaps_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='swapsCount')
    holders_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='holdersCount')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')


class PoolToken(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_id', 'token', 'asset_manager', 'symbol', 'name', 'decimals', 'index', 'address', 'old_price_rate', 'price_rate', 'balance', 'paid_protocol_fees', 'cash_balance', 'managed_balance', 'managements', 'weight', 'is_exempt_from_yield_protocol_fee', 'circuit_breaker')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_id = sgqlc.types.Field(Pool, graphql_name='poolId')
    token = sgqlc.types.Field(sgqlc.types.non_null('Token'), graphql_name='token')
    asset_manager = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='assetManager')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    index = sgqlc.types.Field(Int, graphql_name='index')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    old_price_rate = sgqlc.types.Field(BigDecimal, graphql_name='oldPriceRate')
    price_rate = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='priceRate')
    balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='balance')
    paid_protocol_fees = sgqlc.types.Field(BigDecimal, graphql_name='paidProtocolFees')
    cash_balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='cashBalance')
    managed_balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='managedBalance')
    managements = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ManagementOperation)), graphql_name='managements', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ManagementOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ManagementOperation_filter, graphql_name='where', default=None)),
))
    )
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')
    is_exempt_from_yield_protocol_fee = sgqlc.types.Field(Boolean, graphql_name='isExemptFromYieldProtocolFee')
    circuit_breaker = sgqlc.types.Field(CircuitBreaker, graphql_name='circuitBreaker')


class PriceRateProvider(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_id', 'token', 'address', 'rate', 'last_cached', 'cache_duration', 'cache_expiry')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='poolId')
    token = sgqlc.types.Field(sgqlc.types.non_null(PoolToken), graphql_name='token')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    rate = sgqlc.types.Field(BigDecimal, graphql_name='rate')
    last_cached = sgqlc.types.Field(Int, graphql_name='lastCached')
    cache_duration = sgqlc.types.Field(Int, graphql_name='cacheDuration')
    cache_expiry = sgqlc.types.Field(Int, graphql_name='cacheExpiry')


class ProtocolIdData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Query(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('balancer', 'balancers', 'pool', 'pools', 'pool_contract', 'pool_contracts', 'pool_token', 'pool_tokens', 'price_rate_provider', 'price_rate_providers', 'circuit_breaker', 'circuit_breakers', 'pool_share', 'pool_shares', 'user', 'users', 'user_internal_balance', 'user_internal_balances', 'gradual_weight_update', 'gradual_weight_updates', 'amp_update', 'amp_updates', 'swap_fee_update', 'swap_fee_updates', 'swap', 'swaps', 'join_exit', 'join_exits', 'latest_price', 'latest_prices', 'pool_historical_liquidity', 'pool_historical_liquidities', 'token_price', 'token_prices', 'management_operation', 'management_operations', 'pool_snapshot', 'pool_snapshots', 'token', 'tokens', 'token_snapshot', 'token_snapshots', 'trade_pair', 'trade_pairs', 'trade_pair_snapshot', 'trade_pair_snapshots', 'balancer_snapshot', 'balancer_snapshots', 'protocol_id_data', 'protocol_id_datas', 'fxoracle', 'fxoracles', '_meta')
    balancer = sgqlc.types.Field(Balancer, graphql_name='balancer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    balancers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Balancer))), graphql_name='balancers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Balancer_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Balancer_filter, graphql_name='where', default=None)),
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
    pool_contract = sgqlc.types.Field(PoolContract, graphql_name='poolContract', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_contracts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolContract))), graphql_name='poolContracts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolContract_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolContract_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_token = sgqlc.types.Field(PoolToken, graphql_name='poolToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolToken))), graphql_name='poolTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    price_rate_provider = sgqlc.types.Field(PriceRateProvider, graphql_name='priceRateProvider', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    price_rate_providers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PriceRateProvider))), graphql_name='priceRateProviders', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PriceRateProvider_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PriceRateProvider_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    circuit_breaker = sgqlc.types.Field(CircuitBreaker, graphql_name='circuitBreaker', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    circuit_breakers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CircuitBreaker))), graphql_name='circuitBreakers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(CircuitBreaker_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(CircuitBreaker_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_share = sgqlc.types.Field(PoolShare, graphql_name='poolShare', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_shares = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolShare))), graphql_name='poolShares', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolShare_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolShare_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='users', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(User_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(User_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    user_internal_balance = sgqlc.types.Field('UserInternalBalance', graphql_name='userInternalBalance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    user_internal_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserInternalBalance'))), graphql_name='userInternalBalances', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UserInternalBalance_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UserInternalBalance_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gradual_weight_update = sgqlc.types.Field(GradualWeightUpdate, graphql_name='gradualWeightUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gradual_weight_updates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GradualWeightUpdate))), graphql_name='gradualWeightUpdates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GradualWeightUpdate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GradualWeightUpdate_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    amp_update = sgqlc.types.Field(AmpUpdate, graphql_name='ampUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    amp_updates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AmpUpdate))), graphql_name='ampUpdates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(AmpUpdate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(AmpUpdate_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    swap_fee_update = sgqlc.types.Field('SwapFeeUpdate', graphql_name='swapFeeUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    swap_fee_updates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SwapFeeUpdate'))), graphql_name='swapFeeUpdates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(SwapFeeUpdate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(SwapFeeUpdate_filter, graphql_name='where', default=None)),
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
    join_exit = sgqlc.types.Field(JoinExit, graphql_name='joinExit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    join_exits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JoinExit))), graphql_name='joinExits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(JoinExit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(JoinExit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    latest_price = sgqlc.types.Field(LatestPrice, graphql_name='latestPrice', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    latest_prices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LatestPrice))), graphql_name='latestPrices', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LatestPrice_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LatestPrice_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_historical_liquidity = sgqlc.types.Field(PoolHistoricalLiquidity, graphql_name='poolHistoricalLiquidity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_historical_liquidities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolHistoricalLiquidity))), graphql_name='poolHistoricalLiquidities', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolHistoricalLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolHistoricalLiquidity_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_price = sgqlc.types.Field('TokenPrice', graphql_name='tokenPrice', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_prices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TokenPrice'))), graphql_name='tokenPrices', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TokenPrice_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TokenPrice_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    management_operation = sgqlc.types.Field(ManagementOperation, graphql_name='managementOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    management_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ManagementOperation))), graphql_name='managementOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ManagementOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ManagementOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_snapshot = sgqlc.types.Field(PoolSnapshot, graphql_name='poolSnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolSnapshot))), graphql_name='poolSnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolSnapshot_filter, graphql_name='where', default=None)),
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
    token_snapshot = sgqlc.types.Field('TokenSnapshot', graphql_name='tokenSnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TokenSnapshot'))), graphql_name='tokenSnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TokenSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TokenSnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_pair = sgqlc.types.Field('TradePair', graphql_name='tradePair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_pairs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TradePair'))), graphql_name='tradePairs', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TradePair_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TradePair_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_pair_snapshot = sgqlc.types.Field('TradePairSnapshot', graphql_name='tradePairSnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_pair_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TradePairSnapshot'))), graphql_name='tradePairSnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TradePairSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TradePairSnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    balancer_snapshot = sgqlc.types.Field(BalancerSnapshot, graphql_name='balancerSnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    balancer_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BalancerSnapshot))), graphql_name='balancerSnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(BalancerSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(BalancerSnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocol_id_data = sgqlc.types.Field(ProtocolIdData, graphql_name='protocolIdData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocol_id_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolIdData))), graphql_name='protocolIdDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ProtocolIdData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ProtocolIdData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    fxoracle = sgqlc.types.Field(FXOracle, graphql_name='fxoracle', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    fxoracles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FXOracle))), graphql_name='fxoracles', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FXOracle_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FXOracle_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    _meta = sgqlc.types.Field('_Meta_', graphql_name='_meta', args=sgqlc.types.ArgDict((
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
))
    )


class Subscription(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('balancer', 'balancers', 'pool', 'pools', 'pool_contract', 'pool_contracts', 'pool_token', 'pool_tokens', 'price_rate_provider', 'price_rate_providers', 'circuit_breaker', 'circuit_breakers', 'pool_share', 'pool_shares', 'user', 'users', 'user_internal_balance', 'user_internal_balances', 'gradual_weight_update', 'gradual_weight_updates', 'amp_update', 'amp_updates', 'swap_fee_update', 'swap_fee_updates', 'swap', 'swaps', 'join_exit', 'join_exits', 'latest_price', 'latest_prices', 'pool_historical_liquidity', 'pool_historical_liquidities', 'token_price', 'token_prices', 'management_operation', 'management_operations', 'pool_snapshot', 'pool_snapshots', 'token', 'tokens', 'token_snapshot', 'token_snapshots', 'trade_pair', 'trade_pairs', 'trade_pair_snapshot', 'trade_pair_snapshots', 'balancer_snapshot', 'balancer_snapshots', 'protocol_id_data', 'protocol_id_datas', 'fxoracle', 'fxoracles', '_meta')
    balancer = sgqlc.types.Field(Balancer, graphql_name='balancer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    balancers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Balancer))), graphql_name='balancers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Balancer_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Balancer_filter, graphql_name='where', default=None)),
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
    pool_contract = sgqlc.types.Field(PoolContract, graphql_name='poolContract', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_contracts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolContract))), graphql_name='poolContracts', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolContract_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolContract_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_token = sgqlc.types.Field(PoolToken, graphql_name='poolToken', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolToken))), graphql_name='poolTokens', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolToken_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolToken_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    price_rate_provider = sgqlc.types.Field(PriceRateProvider, graphql_name='priceRateProvider', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    price_rate_providers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PriceRateProvider))), graphql_name='priceRateProviders', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PriceRateProvider_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PriceRateProvider_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    circuit_breaker = sgqlc.types.Field(CircuitBreaker, graphql_name='circuitBreaker', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    circuit_breakers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CircuitBreaker))), graphql_name='circuitBreakers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(CircuitBreaker_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(CircuitBreaker_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_share = sgqlc.types.Field(PoolShare, graphql_name='poolShare', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_shares = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolShare))), graphql_name='poolShares', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolShare_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolShare_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='users', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(User_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(User_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    user_internal_balance = sgqlc.types.Field('UserInternalBalance', graphql_name='userInternalBalance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    user_internal_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserInternalBalance'))), graphql_name='userInternalBalances', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UserInternalBalance_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UserInternalBalance_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gradual_weight_update = sgqlc.types.Field(GradualWeightUpdate, graphql_name='gradualWeightUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    gradual_weight_updates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GradualWeightUpdate))), graphql_name='gradualWeightUpdates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(GradualWeightUpdate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(GradualWeightUpdate_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    amp_update = sgqlc.types.Field(AmpUpdate, graphql_name='ampUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    amp_updates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AmpUpdate))), graphql_name='ampUpdates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(AmpUpdate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(AmpUpdate_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    swap_fee_update = sgqlc.types.Field('SwapFeeUpdate', graphql_name='swapFeeUpdate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    swap_fee_updates = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SwapFeeUpdate'))), graphql_name='swapFeeUpdates', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(SwapFeeUpdate_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(SwapFeeUpdate_filter, graphql_name='where', default=None)),
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
    join_exit = sgqlc.types.Field(JoinExit, graphql_name='joinExit', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    join_exits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(JoinExit))), graphql_name='joinExits', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(JoinExit_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(JoinExit_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    latest_price = sgqlc.types.Field(LatestPrice, graphql_name='latestPrice', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    latest_prices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LatestPrice))), graphql_name='latestPrices', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(LatestPrice_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(LatestPrice_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_historical_liquidity = sgqlc.types.Field(PoolHistoricalLiquidity, graphql_name='poolHistoricalLiquidity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_historical_liquidities = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolHistoricalLiquidity))), graphql_name='poolHistoricalLiquidities', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolHistoricalLiquidity_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolHistoricalLiquidity_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_price = sgqlc.types.Field('TokenPrice', graphql_name='tokenPrice', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_prices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TokenPrice'))), graphql_name='tokenPrices', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TokenPrice_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TokenPrice_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    management_operation = sgqlc.types.Field(ManagementOperation, graphql_name='managementOperation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    management_operations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ManagementOperation))), graphql_name='managementOperations', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ManagementOperation_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ManagementOperation_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_snapshot = sgqlc.types.Field(PoolSnapshot, graphql_name='poolSnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    pool_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PoolSnapshot))), graphql_name='poolSnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolSnapshot_filter, graphql_name='where', default=None)),
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
    token_snapshot = sgqlc.types.Field('TokenSnapshot', graphql_name='tokenSnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    token_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TokenSnapshot'))), graphql_name='tokenSnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TokenSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TokenSnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_pair = sgqlc.types.Field('TradePair', graphql_name='tradePair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_pairs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TradePair'))), graphql_name='tradePairs', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TradePair_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TradePair_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_pair_snapshot = sgqlc.types.Field('TradePairSnapshot', graphql_name='tradePairSnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    trade_pair_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TradePairSnapshot'))), graphql_name='tradePairSnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(TradePairSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(TradePairSnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    balancer_snapshot = sgqlc.types.Field(BalancerSnapshot, graphql_name='balancerSnapshot', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    balancer_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BalancerSnapshot))), graphql_name='balancerSnapshots', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(BalancerSnapshot_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(BalancerSnapshot_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocol_id_data = sgqlc.types.Field(ProtocolIdData, graphql_name='protocolIdData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    protocol_id_datas = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProtocolIdData))), graphql_name='protocolIdDatas', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(ProtocolIdData_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(ProtocolIdData_filter, graphql_name='where', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    fxoracle = sgqlc.types.Field(FXOracle, graphql_name='fxoracle', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('block', sgqlc.types.Arg(Block_height, graphql_name='block', default=None)),
        ('subgraph_error', sgqlc.types.Arg(sgqlc.types.non_null(_SubgraphErrorPolicy_), graphql_name='subgraphError', default='deny')),
))
    )
    fxoracles = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FXOracle))), graphql_name='fxoracles', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(FXOracle_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(FXOracle_filter, graphql_name='where', default=None)),
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
    __field_names__ = ('id', 'caller', 'token_in', 'token_in_sym', 'token_out', 'token_out_sym', 'token_amount_in', 'token_amount_out', 'value_usd', 'pool_id', 'user_address', 'timestamp', 'block', 'tx')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    caller = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='caller')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='tokenIn')
    token_in_sym = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenInSym')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='tokenOut')
    token_out_sym = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenOutSym')
    token_amount_in = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='tokenAmountIn')
    token_amount_out = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='tokenAmountOut')
    value_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='valueUSD')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='poolId')
    user_address = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='userAddress')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    block = sgqlc.types.Field(BigInt, graphql_name='block')
    tx = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='tx')


class SwapFeeUpdate(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool', 'scheduled_timestamp', 'start_timestamp', 'end_timestamp', 'start_swap_fee_percentage', 'end_swap_fee_percentage')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='pool')
    scheduled_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='scheduledTimestamp')
    start_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='startTimestamp')
    end_timestamp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='endTimestamp')
    start_swap_fee_percentage = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='startSwapFeePercentage')
    end_swap_fee_percentage = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='endSwapFeePercentage')


class Token(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'symbol', 'name', 'decimals', 'address', 'total_balance_usd', 'total_balance_notional', 'total_volume_usd', 'total_volume_notional', 'total_swap_count', 'latest_price', 'latest_usdprice', 'latest_usdprice_timestamp', 'latest_fxprice', 'pool', 'fx_oracle_decimals')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    symbol = sgqlc.types.Field(String, graphql_name='symbol')
    name = sgqlc.types.Field(String, graphql_name='name')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    total_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBalanceUSD')
    total_balance_notional = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBalanceNotional')
    total_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalVolumeUSD')
    total_volume_notional = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalVolumeNotional')
    total_swap_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='totalSwapCount')
    latest_price = sgqlc.types.Field(LatestPrice, graphql_name='latestPrice')
    latest_usdprice = sgqlc.types.Field(BigDecimal, graphql_name='latestUSDPrice')
    latest_usdprice_timestamp = sgqlc.types.Field(BigInt, graphql_name='latestUSDPriceTimestamp')
    latest_fxprice = sgqlc.types.Field(BigDecimal, graphql_name='latestFXPrice')
    pool = sgqlc.types.Field(Pool, graphql_name='pool')
    fx_oracle_decimals = sgqlc.types.Field(Int, graphql_name='fxOracleDecimals')


class TokenPrice(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool_id', 'asset', 'amount', 'pricing_asset', 'price', 'block', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(Pool), graphql_name='poolId')
    asset = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='asset')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='amount')
    pricing_asset = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='pricingAsset')
    price = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='price')
    block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='block')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')


class TokenSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'token', 'timestamp', 'total_balance_usd', 'total_balance_notional', 'total_volume_usd', 'total_volume_notional', 'total_swap_count')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    token = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='token')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    total_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBalanceUSD')
    total_balance_notional = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBalanceNotional')
    total_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalVolumeUSD')
    total_volume_notional = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalVolumeNotional')
    total_swap_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='totalSwapCount')


class TradePair(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'token0', 'token1', 'total_swap_volume', 'total_swap_fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    token0 = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='token0')
    token1 = sgqlc.types.Field(sgqlc.types.non_null(Token), graphql_name='token1')
    total_swap_volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapVolume')
    total_swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapFee')


class TradePairSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pair', 'timestamp', 'total_swap_volume', 'total_swap_fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pair = sgqlc.types.Field(sgqlc.types.non_null(TradePair), graphql_name='pair')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    total_swap_volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapVolume')
    total_swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSwapFee')


class User(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'shares_owned', 'swaps', 'user_internal_balances')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    shares_owned = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PoolShare)), graphql_name='sharesOwned', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(PoolShare_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(PoolShare_filter, graphql_name='where', default=None)),
))
    )
    swaps = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Swap)), graphql_name='swaps', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(Swap_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(Swap_filter, graphql_name='where', default=None)),
))
    )
    user_internal_balances = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserInternalBalance')), graphql_name='userInternalBalances', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=100)),
        ('order_by', sgqlc.types.Arg(UserInternalBalance_orderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(OrderDirection, graphql_name='orderDirection', default=None)),
        ('where', sgqlc.types.Arg(UserInternalBalance_filter, graphql_name='where', default=None)),
))
    )


class UserInternalBalance(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'user_address', 'token', 'token_info', 'balance')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    user_address = sgqlc.types.Field(User, graphql_name='userAddress')
    token = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='token')
    token_info = sgqlc.types.Field(Token, graphql_name='tokenInfo')
    balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='balance')


class _Block_(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('hash', 'number', 'timestamp')
    hash = sgqlc.types.Field(Bytes, graphql_name='hash')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    timestamp = sgqlc.types.Field(Int, graphql_name='timestamp')


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

