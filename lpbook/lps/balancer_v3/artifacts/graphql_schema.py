import sgqlc.types
import sgqlc.types.datetime


graphql_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AmountHumanReadable(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class BigDecimal(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class BigInt(sgqlc.types.Scalar):
    __schema__ = graphql_schema


Boolean = sgqlc.types.Boolean

class Bytes(sgqlc.types.Scalar):
    __schema__ = graphql_schema


Date = sgqlc.types.datetime.Date

Float = sgqlc.types.Float

class GqlBigNumber(sgqlc.types.Scalar):
    __schema__ = graphql_schema


class GqlChain(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('ARBITRUM', 'AVALANCHE', 'BASE', 'FANTOM', 'FRAXTAL', 'GNOSIS', 'MAINNET', 'MODE', 'OPTIMISM', 'POLYGON', 'SEPOLIA', 'SONIC', 'ZKEVM')


class GqlHookType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('DIRECTIONAL_FEE', 'EXIT_FEE', 'FEE_TAKING', 'LOTTERY', 'MEV_TAX', 'NFTLIQUIDITY_POSITION', 'STABLE_SURGE', 'UNKNOWN', 'VEBAL_DISCOUNT')


class GqlPoolAprItemType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('AURA', 'DYNAMIC_SWAP_FEE_24H', 'IB_YIELD', 'LOCKING', 'MABEETS_EMISSIONS', 'MERKL', 'NESTED', 'STAKING', 'STAKING_BOOST', 'SURPLUS_24H', 'SURPLUS_30D', 'SURPLUS_7D', 'SWAP_FEE_24H', 'SWAP_FEE_30D', 'SWAP_FEE_7D', 'VEBAL_EMISSIONS', 'VOTING')


class GqlPoolEventType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('ADD', 'REMOVE', 'SWAP')


class GqlPoolEventsDataRange(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('NINETY_DAYS', 'SEVEN_DAYS', 'THIRTY_DAYS')


class GqlPoolFilterCategory(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('BLACK_LISTED', 'INCENTIVIZED', 'LRT', 'POINTS', 'POINTS_EIGENLAYER', 'POINTS_GYRO', 'POINTS_KELP', 'POINTS_RENZO', 'POINTS_SWELL', 'SUPERFEST')


class GqlPoolJoinExitType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('Exit', 'Join')


class GqlPoolNestingType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('HAS_ONLY_PHANTOM_BPT', 'HAS_SOME_PHANTOM_BPT', 'NO_NESTING')


class GqlPoolOrderBy(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('apr', 'fees24h', 'totalLiquidity', 'totalShares', 'userbalanceUsd', 'volume24h')


class GqlPoolOrderDirection(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('asc', 'desc')


class GqlPoolSnapshotDataRange(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('ALL_TIME', 'NINETY_DAYS', 'ONE_HUNDRED_EIGHTY_DAYS', 'ONE_YEAR', 'THIRTY_DAYS')


class GqlPoolStakingGaugeStatus(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('ACTIVE', 'KILLED', 'PREFERRED')


class GqlPoolStakingType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('AURA', 'FRESH_BEETS', 'GAUGE', 'MASTER_CHEF', 'RELIQUARY', 'VEBAL')


class GqlPoolType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('COMPOSABLE_STABLE', 'COW_AMM', 'ELEMENT', 'FX', 'GYRO', 'GYRO3', 'GYROE', 'INVESTMENT', 'LIQUIDITY_BOOTSTRAPPING', 'META_STABLE', 'PHANTOM_STABLE', 'QUANT_AMM_WEIGHTED', 'STABLE', 'UNKNOWN', 'WEIGHTED')


class GqlSftmxStakingSnapshotDataRange(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('ALL_TIME', 'NINETY_DAYS', 'ONE_HUNDRED_EIGHTY_DAYS', 'ONE_YEAR', 'THIRTY_DAYS')


class GqlSorSwapType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('EXACT_IN', 'EXACT_OUT')


class GqlStakedSonicSnapshotDataRange(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('ALL_TIME', 'NINETY_DAYS', 'ONE_HUNDRED_EIGHTY_DAYS', 'ONE_YEAR', 'THIRTY_DAYS')


class GqlTokenChartDataRange(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('ALL', 'NINETY_DAY', 'ONE_HUNDRED_EIGHTY_DAY', 'ONE_YEAR', 'SEVEN_DAY', 'THIRTY_DAY')


class GqlTokenType(sgqlc.types.Enum):
    __schema__ = graphql_schema
    __choices__ = ('BPT', 'ERC4626', 'PHANTOM_BPT', 'WHITE_LISTED')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JSON(sgqlc.types.Scalar):
    __schema__ = graphql_schema


String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################
class GqlAggregatorPoolFilter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('chain_in', 'chain_not_in', 'create_time', 'id_in', 'id_not_in', 'include_hooks', 'min_tvl', 'pool_type_in', 'pool_type_not_in', 'protocol_version_in', 'tokens_in', 'tokens_not_in')
    chain_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chainIn')
    chain_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chainNotIn')
    create_time = sgqlc.types.Field('GqlPoolTimePeriod', graphql_name='createTime')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='idIn')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='idNotIn')
    include_hooks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlHookType)), graphql_name='includeHooks')
    min_tvl = sgqlc.types.Field(Float, graphql_name='minTvl')
    pool_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolType)), graphql_name='poolTypeIn')
    pool_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolType)), graphql_name='poolTypeNotIn')
    protocol_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='protocolVersionIn')
    tokens_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokensIn')
    tokens_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokensNotIn')


class GqlPoolEventsFilter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('chain_in', 'pool_id_in', 'range', 'type_in', 'user_address', 'value_usd_gt', 'value_usd_gte')
    chain_in = sgqlc.types.Field(sgqlc.types.list_of(GqlChain), graphql_name='chainIn')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='poolIdIn')
    range = sgqlc.types.Field(GqlPoolEventsDataRange, graphql_name='range')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(GqlPoolEventType), graphql_name='typeIn')
    user_address = sgqlc.types.Field(String, graphql_name='userAddress')
    value_usd_gt = sgqlc.types.Field(Float, graphql_name='valueUSD_gt')
    value_usd_gte = sgqlc.types.Field(Float, graphql_name='valueUSD_gte')


class GqlPoolFilter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('chain_in', 'chain_not_in', 'create_time', 'id_in', 'id_not_in', 'min_tvl', 'pool_type_in', 'pool_type_not_in', 'protocol_version_in', 'tag_in', 'tag_not_in', 'tokens_in', 'tokens_not_in', 'user_address')
    chain_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chainIn')
    chain_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chainNotIn')
    create_time = sgqlc.types.Field('GqlPoolTimePeriod', graphql_name='createTime')
    id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='idIn')
    id_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='idNotIn')
    min_tvl = sgqlc.types.Field(Float, graphql_name='minTvl')
    pool_type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolType)), graphql_name='poolTypeIn')
    pool_type_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolType)), graphql_name='poolTypeNotIn')
    protocol_version_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='protocolVersionIn')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tagNotIn')
    tokens_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokensIn')
    tokens_not_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokensNotIn')
    user_address = sgqlc.types.Field(String, graphql_name='userAddress')


class GqlPoolJoinExitFilter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('chain_in', 'pool_id_in')
    chain_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chainIn')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolIdIn')


class GqlPoolSwapFilter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('chain_in', 'pool_id_in', 'token_in_in', 'token_out_in')
    chain_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chainIn')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolIdIn')
    token_in_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenInIn')
    token_out_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenOutIn')


class GqlPoolTimePeriod(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('gt', 'lt')
    gt = sgqlc.types.Field(Int, graphql_name='gt')
    lt = sgqlc.types.Field(Int, graphql_name='lt')


class GqlSwapCallDataInput(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('deadline', 'receiver', 'sender', 'slippage_percentage')
    deadline = sgqlc.types.Field(Int, graphql_name='deadline')
    receiver = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='receiver')
    sender = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sender')
    slippage_percentage = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slippagePercentage')


class GqlTokenAmountHumanReadable(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'amount')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='amount')


class GqlTokenFilter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('tokens_in', 'type_in')
    tokens_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokensIn')
    type_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlTokenType)), graphql_name='typeIn')


class GqlUserSwapVolumeFilter(sgqlc.types.Input):
    __schema__ = graphql_schema
    __field_names__ = ('pool_id_in', 'token_in_in', 'token_out_in')
    pool_id_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolIdIn')
    token_in_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenInIn')
    token_out_in = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='tokenOutIn')



########################################################################
# Output Objects and Interfaces
########################################################################
class GqlPoolBase(sgqlc.types.Interface):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'categories', 'chain', 'create_time', 'decimals', 'dynamic_data', 'factory', 'has_any_allowed_buffer', 'has_erc4626', 'has_nested_erc4626', 'hook', 'id', 'liquidity_management', 'name', 'pause_manager', 'pool_creator', 'pool_tokens', 'protocol_version', 'staking', 'swap_fee_manager', 'symbol', 'tags', 'type', 'user_balance', 'version')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    categories = sgqlc.types.Field(sgqlc.types.list_of(GqlPoolFilterCategory), graphql_name='categories')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createTime')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    dynamic_data = sgqlc.types.Field(sgqlc.types.non_null('GqlPoolDynamicData'), graphql_name='dynamicData')
    factory = sgqlc.types.Field(Bytes, graphql_name='factory')
    has_any_allowed_buffer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasAnyAllowedBuffer')
    has_erc4626 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasErc4626')
    has_nested_erc4626 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNestedErc4626')
    hook = sgqlc.types.Field('GqlHook', graphql_name='hook')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    liquidity_management = sgqlc.types.Field('LiquidityManagement', graphql_name='liquidityManagement')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pause_manager = sgqlc.types.Field(Bytes, graphql_name='pauseManager')
    pool_creator = sgqlc.types.Field(Bytes, graphql_name='poolCreator')
    pool_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolTokenDetail'))), graphql_name='poolTokens')
    protocol_version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='protocolVersion')
    staking = sgqlc.types.Field('GqlPoolStaking', graphql_name='staking')
    swap_fee_manager = sgqlc.types.Field(Bytes, graphql_name='swapFeeManager')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolType), graphql_name='type')
    user_balance = sgqlc.types.Field('GqlPoolUserBalance', graphql_name='userBalance')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')


class GqlPoolEvent(sgqlc.types.Interface):
    __schema__ = graphql_schema
    __field_names__ = ('block_number', 'block_timestamp', 'chain', 'id', 'log_index', 'pool_id', 'sender', 'timestamp', 'tx', 'type', 'user_address', 'value_usd')
    block_number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='blockNumber')
    block_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='blockTimestamp')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    log_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='logIndex')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolId')
    sender = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sender')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    tx = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tx')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolEventType), graphql_name='type')
    user_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userAddress')
    value_usd = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='valueUSD')


class GqlPoolTokenBase(sgqlc.types.Interface):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'balance', 'decimals', 'id', 'index', 'name', 'price_rate', 'price_rate_provider', 'symbol', 'total_balance', 'weight')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='balance')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    price_rate = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='priceRate')
    price_rate_provider = sgqlc.types.Field(String, graphql_name='priceRateProvider')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    total_balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalBalance')
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')


class Erc4626ReviewData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('can_use_buffer_for_swaps', 'review_file', 'summary', 'use_underlying_for_add_remove', 'use_wrapped_for_add_remove', 'warnings')
    can_use_buffer_for_swaps = sgqlc.types.Field(Boolean, graphql_name='canUseBufferForSwaps')
    review_file = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reviewFile')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    use_underlying_for_add_remove = sgqlc.types.Field(Boolean, graphql_name='useUnderlyingForAddRemove')
    use_wrapped_for_add_remove = sgqlc.types.Field(Boolean, graphql_name='useWrappedForAddRemove')
    warnings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='warnings')


class ExitFeeHookParams(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('exit_fee_percentage',)
    exit_fee_percentage = sgqlc.types.Field(String, graphql_name='exitFeePercentage')


class FeeTakingHookParams(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('add_liquidity_fee_percentage', 'remove_liquidity_fee_percentage', 'swap_fee_percentage')
    add_liquidity_fee_percentage = sgqlc.types.Field(String, graphql_name='addLiquidityFeePercentage')
    remove_liquidity_fee_percentage = sgqlc.types.Field(String, graphql_name='removeLiquidityFeePercentage')
    swap_fee_percentage = sgqlc.types.Field(String, graphql_name='swapFeePercentage')


class GqlBalancePoolAprItem(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('apr', 'id', 'sub_items', 'title')
    apr = sgqlc.types.Field(sgqlc.types.non_null('GqlPoolAprValue'), graphql_name='apr')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    sub_items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GqlBalancePoolAprSubItem')), graphql_name='subItems')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class GqlBalancePoolAprSubItem(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('apr', 'id', 'title')
    apr = sgqlc.types.Field(sgqlc.types.non_null('GqlPoolAprValue'), graphql_name='apr')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class GqlFeaturePoolGroupItemExternalLink(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('button_text', 'button_url', 'id', 'image')
    button_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='buttonText')
    button_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='buttonUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='image')


class GqlHistoricalTokenPrice(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'chain', 'prices')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    prices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlHistoricalTokenPriceEntry'))), graphql_name='prices')


class GqlHistoricalTokenPriceEntry(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('price', 'timestamp', 'updated_at', 'updated_by')
    price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='price')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='timestamp')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='updatedAt')
    updated_by = sgqlc.types.Field(String, graphql_name='updatedBy')


class GqlHook(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'config', 'params', 'review_data', 'type')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    config = sgqlc.types.Field('HookConfig', graphql_name='config')
    params = sgqlc.types.Field('HookParams', graphql_name='params')
    review_data = sgqlc.types.Field('GqlHookReviewData', graphql_name='reviewData')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlHookType), graphql_name='type')


class GqlHookData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('add_liquidity_fee_percentage', 'max_surge_fee_percentage', 'remove_liquidity_fee_percentage', 'surge_threshold_percentage', 'swap_fee_percentage')
    add_liquidity_fee_percentage = sgqlc.types.Field(String, graphql_name='addLiquidityFeePercentage')
    max_surge_fee_percentage = sgqlc.types.Field(String, graphql_name='maxSurgeFeePercentage')
    remove_liquidity_fee_percentage = sgqlc.types.Field(String, graphql_name='removeLiquidityFeePercentage')
    surge_threshold_percentage = sgqlc.types.Field(String, graphql_name='surgeThresholdPercentage')
    swap_fee_percentage = sgqlc.types.Field(String, graphql_name='swapFeePercentage')


class GqlHookReviewData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('review_file', 'summary', 'warnings')
    review_file = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reviewFile')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    warnings = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='warnings')


class GqlLatestSyncedBlocks(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('pool_sync_block', 'user_stake_sync_block', 'user_wallet_sync_block')
    pool_sync_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='poolSyncBlock')
    user_stake_sync_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='userStakeSyncBlock')
    user_wallet_sync_block = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='userWalletSyncBlock')


class GqlNestedPool(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'bpt_price_rate', 'create_time', 'factory', 'hook', 'id', 'liquidity_management', 'name', 'nested_liquidity', 'nested_percentage', 'nested_shares', 'pause_manager', 'pool_creator', 'swap_fee', 'swap_fee_manager', 'symbol', 'tokens', 'total_liquidity', 'total_shares', 'type', 'version')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    bpt_price_rate = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='bptPriceRate')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createTime')
    factory = sgqlc.types.Field(Bytes, graphql_name='factory')
    hook = sgqlc.types.Field(GqlHook, graphql_name='hook')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    liquidity_management = sgqlc.types.Field('LiquidityManagement', graphql_name='liquidityManagement')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nested_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='nestedLiquidity')
    nested_percentage = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='nestedPercentage')
    nested_shares = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='nestedShares')
    pause_manager = sgqlc.types.Field(Bytes, graphql_name='pauseManager')
    pool_creator = sgqlc.types.Field(Bytes, graphql_name='poolCreator')
    swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapFee')
    swap_fee_manager = sgqlc.types.Field(Bytes, graphql_name='swapFeeManager')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolTokenDetail'))), graphql_name='tokens')
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidity')
    total_shares = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalShares')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolType), graphql_name='type')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')


class GqlPoolAggregator(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'alpha', 'amp', 'beta', 'c', 'chain', 'create_time', 'd_sq', 'decimals', 'delta', 'dynamic_data', 'epsilon', 'factory', 'hook', 'id', 'lambda_', 'liquidity_management', 'name', 'pause_manager', 'pool_creator', 'pool_tokens', 'protocol_version', 'quant_amm_weighted_params', 'root3_alpha', 's', 'sqrt_alpha', 'sqrt_beta', 'swap_fee_manager', 'symbol', 'tau_alpha_x', 'tau_alpha_y', 'tau_beta_x', 'tau_beta_y', 'type', 'u', 'v', 'version', 'w', 'z')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    alpha = sgqlc.types.Field(String, graphql_name='alpha')
    amp = sgqlc.types.Field(BigInt, graphql_name='amp')
    beta = sgqlc.types.Field(String, graphql_name='beta')
    c = sgqlc.types.Field(String, graphql_name='c')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createTime')
    d_sq = sgqlc.types.Field(String, graphql_name='dSq')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    delta = sgqlc.types.Field(String, graphql_name='delta')
    dynamic_data = sgqlc.types.Field(sgqlc.types.non_null('GqlPoolDynamicData'), graphql_name='dynamicData')
    epsilon = sgqlc.types.Field(String, graphql_name='epsilon')
    factory = sgqlc.types.Field(Bytes, graphql_name='factory')
    hook = sgqlc.types.Field(GqlHook, graphql_name='hook')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    lambda_ = sgqlc.types.Field(String, graphql_name='lambda')
    liquidity_management = sgqlc.types.Field('LiquidityManagement', graphql_name='liquidityManagement')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pause_manager = sgqlc.types.Field(Bytes, graphql_name='pauseManager')
    pool_creator = sgqlc.types.Field(Bytes, graphql_name='poolCreator')
    pool_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolTokenDetail'))), graphql_name='poolTokens')
    protocol_version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='protocolVersion')
    quant_amm_weighted_params = sgqlc.types.Field('QuantAmmWeightedParams', graphql_name='quantAmmWeightedParams')
    root3_alpha = sgqlc.types.Field(String, graphql_name='root3Alpha')
    s = sgqlc.types.Field(String, graphql_name='s')
    sqrt_alpha = sgqlc.types.Field(String, graphql_name='sqrtAlpha')
    sqrt_beta = sgqlc.types.Field(String, graphql_name='sqrtBeta')
    swap_fee_manager = sgqlc.types.Field(Bytes, graphql_name='swapFeeManager')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    tau_alpha_x = sgqlc.types.Field(String, graphql_name='tauAlphaX')
    tau_alpha_y = sgqlc.types.Field(String, graphql_name='tauAlphaY')
    tau_beta_x = sgqlc.types.Field(String, graphql_name='tauBetaX')
    tau_beta_y = sgqlc.types.Field(String, graphql_name='tauBetaY')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolType), graphql_name='type')
    u = sgqlc.types.Field(String, graphql_name='u')
    v = sgqlc.types.Field(String, graphql_name='v')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')
    w = sgqlc.types.Field(String, graphql_name='w')
    z = sgqlc.types.Field(String, graphql_name='z')


class GqlPoolApr(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('apr', 'has_reward_apr', 'items', 'native_reward_apr', 'swap_apr', 'third_party_apr')
    apr = sgqlc.types.Field(sgqlc.types.non_null('GqlPoolAprValue'), graphql_name='apr')
    has_reward_apr = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasRewardApr')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlBalancePoolAprItem))), graphql_name='items')
    native_reward_apr = sgqlc.types.Field(sgqlc.types.non_null('GqlPoolAprValue'), graphql_name='nativeRewardApr')
    swap_apr = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapApr')
    third_party_apr = sgqlc.types.Field(sgqlc.types.non_null('GqlPoolAprValue'), graphql_name='thirdPartyApr')


class GqlPoolAprItem(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('apr', 'id', 'reward_token_address', 'reward_token_symbol', 'type')
    apr = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='apr')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reward_token_address = sgqlc.types.Field(String, graphql_name='rewardTokenAddress')
    reward_token_symbol = sgqlc.types.Field(String, graphql_name='rewardTokenSymbol')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolAprItemType), graphql_name='type')


class GqlPoolAprRange(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('max', 'min')
    max = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='max')
    min = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='min')


class GqlPoolAprTotal(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('total',)
    total = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='total')


class GqlPoolBatchSwap(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('chain', 'id', 'swaps', 'timestamp', 'token_amount_in', 'token_amount_out', 'token_in', 'token_in_price', 'token_out', 'token_out_price', 'tx', 'user_address', 'value_usd')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    swaps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolBatchSwapSwap'))), graphql_name='swaps')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    token_amount_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAmountIn')
    token_amount_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAmountOut')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenIn')
    token_in_price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='tokenInPrice')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenOut')
    token_out_price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='tokenOutPrice')
    tx = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tx')
    user_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userAddress')
    value_usd = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='valueUSD')


class GqlPoolBatchSwapPool(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'tokens')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tokens')


class GqlPoolBatchSwapSwap(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'pool', 'timestamp', 'token_amount_in', 'token_amount_out', 'token_in', 'token_out', 'tx', 'user_address', 'value_usd')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool = sgqlc.types.Field(sgqlc.types.non_null('PoolForBatchSwap'), graphql_name='pool')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    token_amount_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAmountIn')
    token_amount_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAmountOut')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenIn')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenOut')
    tx = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tx')
    user_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userAddress')
    value_usd = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='valueUSD')


class GqlPoolComposableStableNested(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'amp', 'bpt_price_rate', 'categories', 'create_time', 'factory', 'id', 'name', 'pause_manager', 'pool_creator', 'swap_fee', 'swap_fee_manager', 'symbol', 'tags', 'total_liquidity', 'total_shares', 'type', 'version')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    amp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amp')
    bpt_price_rate = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='bptPriceRate')
    categories = sgqlc.types.Field(sgqlc.types.list_of(GqlPoolFilterCategory), graphql_name='categories')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createTime')
    factory = sgqlc.types.Field(Bytes, graphql_name='factory')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pause_manager = sgqlc.types.Field(Bytes, graphql_name='pauseManager')
    pool_creator = sgqlc.types.Field(Bytes, graphql_name='poolCreator')
    swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapFee')
    swap_fee_manager = sgqlc.types.Field(Bytes, graphql_name='swapFeeManager')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidity')
    total_shares = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalShares')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolType), graphql_name='type')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')


class GqlPoolDynamicData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('aggregate_swap_fee', 'aggregate_yield_fee', 'apr_items', 'fees24h', 'fees24h_ath', 'fees24h_ath_timestamp', 'fees24h_atl', 'fees24h_atl_timestamp', 'fees48h', 'holders_count', 'is_in_recovery_mode', 'is_paused', 'lifetime_swap_fees', 'lifetime_volume', 'pool_id', 'protocol_fees24h', 'protocol_fees48h', 'protocol_yield_capture24h', 'protocol_yield_capture48h', 'share_price_ath', 'share_price_ath_timestamp', 'share_price_atl', 'share_price_atl_timestamp', 'surplus24h', 'surplus48h', 'swap_enabled', 'swap_fee', 'swaps_count', 'total_liquidity', 'total_liquidity24h_ago', 'total_liquidity_ath', 'total_liquidity_ath_timestamp', 'total_liquidity_atl', 'total_liquidity_atl_timestamp', 'total_shares', 'total_shares24h_ago', 'total_supply', 'volume24h', 'volume24h_ath', 'volume24h_ath_timestamp', 'volume24h_atl', 'volume24h_atl_timestamp', 'volume48h', 'yield_capture24h', 'yield_capture48h')
    aggregate_swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='aggregateSwapFee')
    aggregate_yield_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='aggregateYieldFee')
    apr_items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolAprItem))), graphql_name='aprItems')
    fees24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='fees24h')
    fees24h_ath = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='fees24hAth')
    fees24h_ath_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fees24hAthTimestamp')
    fees24h_atl = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='fees24hAtl')
    fees24h_atl_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='fees24hAtlTimestamp')
    fees48h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='fees48h')
    holders_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='holdersCount')
    is_in_recovery_mode = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInRecoveryMode')
    is_paused = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPaused')
    lifetime_swap_fees = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='lifetimeSwapFees')
    lifetime_volume = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='lifetimeVolume')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='poolId')
    protocol_fees24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='protocolFees24h')
    protocol_fees48h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='protocolFees48h')
    protocol_yield_capture24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='protocolYieldCapture24h')
    protocol_yield_capture48h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='protocolYieldCapture48h')
    share_price_ath = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='sharePriceAth')
    share_price_ath_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sharePriceAthTimestamp')
    share_price_atl = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='sharePriceAtl')
    share_price_atl_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='sharePriceAtlTimestamp')
    surplus24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='surplus24h')
    surplus48h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='surplus48h')
    swap_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='swapEnabled')
    swap_fee = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapFee')
    swaps_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='swapsCount')
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidity')
    total_liquidity24h_ago = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidity24hAgo')
    total_liquidity_ath = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidityAth')
    total_liquidity_ath_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalLiquidityAthTimestamp')
    total_liquidity_atl = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidityAtl')
    total_liquidity_atl_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalLiquidityAtlTimestamp')
    total_shares = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalShares')
    total_shares24h_ago = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalShares24hAgo')
    total_supply = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalSupply')
    volume24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volume24h')
    volume24h_ath = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volume24hAth')
    volume24h_ath_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='volume24hAthTimestamp')
    volume24h_atl = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volume24hAtl')
    volume24h_atl_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='volume24hAtlTimestamp')
    volume48h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='volume48h')
    yield_capture24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='yieldCapture24h')
    yield_capture48h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='yieldCapture48h')


class GqlPoolEventAmount(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'amount', 'value_usd')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    amount = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='amount')
    value_usd = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='valueUSD')


class GqlPoolFeaturedPool(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('description', 'pool', 'pool_id', 'primary')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    pool = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolBase), graphql_name='pool')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='poolId')
    primary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='primary')


class GqlPoolFeaturedPoolGroup(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('icon', 'id', 'items', 'title')
    icon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='icon')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    items = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolFeaturedPoolGroupItem'))), graphql_name='items')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class GqlPoolInvestConfig(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('options', 'proportional_enabled', 'single_asset_enabled')
    options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolInvestOption'))), graphql_name='options')
    proportional_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='proportionalEnabled')
    single_asset_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='singleAssetEnabled')


class GqlPoolInvestOption(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('pool_token_address', 'pool_token_index', 'token_options')
    pool_token_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolTokenAddress')
    pool_token_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='poolTokenIndex')
    token_options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolToken'))), graphql_name='tokenOptions')


class GqlPoolJoinExit(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('amounts', 'chain', 'id', 'pool_id', 'sender', 'timestamp', 'tx', 'type', 'value_usd')
    amounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolJoinExitAmount'))), graphql_name='amounts')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolId')
    sender = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sender')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    tx = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tx')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolJoinExitType), graphql_name='type')
    value_usd = sgqlc.types.Field(String, graphql_name='valueUSD')


class GqlPoolJoinExitAmount(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'amount')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    amount = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='amount')


class GqlPoolMinimal(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'categories', 'chain', 'create_time', 'decimals', 'dynamic_data', 'factory', 'has_any_allowed_buffer', 'has_erc4626', 'has_nested_erc4626', 'hook', 'id', 'incentivized', 'liquidity_management', 'name', 'pause_manager', 'pool_creator', 'pool_tokens', 'protocol_version', 'staking', 'swap_fee_manager', 'symbol', 'tags', 'type', 'user_balance', 'version')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    categories = sgqlc.types.Field(sgqlc.types.list_of(GqlPoolFilterCategory), graphql_name='categories')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createTime')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    dynamic_data = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolDynamicData), graphql_name='dynamicData')
    factory = sgqlc.types.Field(Bytes, graphql_name='factory')
    has_any_allowed_buffer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasAnyAllowedBuffer')
    has_erc4626 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasErc4626')
    has_nested_erc4626 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNestedErc4626')
    hook = sgqlc.types.Field(GqlHook, graphql_name='hook')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    incentivized = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='incentivized')
    liquidity_management = sgqlc.types.Field('LiquidityManagement', graphql_name='liquidityManagement')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pause_manager = sgqlc.types.Field(Bytes, graphql_name='pauseManager')
    pool_creator = sgqlc.types.Field(Bytes, graphql_name='poolCreator')
    pool_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolTokenDetail'))), graphql_name='poolTokens')
    protocol_version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='protocolVersion')
    staking = sgqlc.types.Field('GqlPoolStaking', graphql_name='staking')
    swap_fee_manager = sgqlc.types.Field(Bytes, graphql_name='swapFeeManager')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolType), graphql_name='type')
    user_balance = sgqlc.types.Field('GqlPoolUserBalance', graphql_name='userBalance')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')


class GqlPoolMutationResult(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('chain', 'error', 'success', 'type')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    error = sgqlc.types.Field(String, graphql_name='error')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class GqlPoolSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('amounts', 'chain', 'fees24h', 'holders_count', 'id', 'pool_id', 'share_price', 'surplus24h', 'swaps_count', 'timestamp', 'total_liquidity', 'total_shares', 'total_surplus', 'total_swap_fee', 'total_swap_volume', 'volume24h')
    amounts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='amounts')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    fees24h = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fees24h')
    holders_count = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='holdersCount')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolId')
    share_price = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sharePrice')
    surplus24h = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='surplus24h')
    swaps_count = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='swapsCount')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalLiquidity')
    total_shares = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalShares')
    total_surplus = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalSurplus')
    total_swap_fee = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalSwapFee')
    total_swap_volume = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalSwapVolume')
    volume24h = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='volume24h')


class GqlPoolStaking(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'aura', 'chain', 'farm', 'gauge', 'id', 'reliquary', 'type', 'vebal')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    aura = sgqlc.types.Field('GqlPoolStakingAura', graphql_name='aura')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    farm = sgqlc.types.Field('GqlPoolStakingMasterChefFarm', graphql_name='farm')
    gauge = sgqlc.types.Field('GqlPoolStakingGauge', graphql_name='gauge')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reliquary = sgqlc.types.Field('GqlPoolStakingReliquaryFarm', graphql_name='reliquary')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolStakingType), graphql_name='type')
    vebal = sgqlc.types.Field('GqlPoolStakingVebal', graphql_name='vebal')


class GqlPoolStakingAura(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('apr', 'aura_pool_address', 'aura_pool_id', 'id', 'is_shutdown')
    apr = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='apr')
    aura_pool_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='auraPoolAddress')
    aura_pool_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='auraPoolId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_shutdown = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isShutdown')


class GqlPoolStakingFarmRewarder(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'id', 'reward_per_second', 'token_address')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reward_per_second = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rewardPerSecond')
    token_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAddress')


class GqlPoolStakingGauge(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('gauge_address', 'id', 'other_gauges', 'rewards', 'status', 'version', 'working_supply')
    gauge_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='gaugeAddress')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    other_gauges = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolStakingOtherGauge')), graphql_name='otherGauges')
    rewards = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolStakingGaugeReward'))), graphql_name='rewards')
    status = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolStakingGaugeStatus), graphql_name='status')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')
    working_supply = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='workingSupply')


class GqlPoolStakingGaugeReward(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'reward_per_second', 'token_address')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reward_per_second = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rewardPerSecond')
    token_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAddress')


class GqlPoolStakingMasterChefFarm(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('beets_per_block', 'id', 'rewarders')
    beets_per_block = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='beetsPerBlock')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    rewarders = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolStakingFarmRewarder)), graphql_name='rewarders')


class GqlPoolStakingOtherGauge(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('gauge_address', 'id', 'rewards', 'status', 'version')
    gauge_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='gaugeAddress')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    rewards = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolStakingGaugeReward))), graphql_name='rewards')
    status = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolStakingGaugeStatus), graphql_name='status')
    version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='version')


class GqlPoolStakingReliquaryFarm(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('beets_per_second', 'id', 'levels', 'total_balance', 'total_weighted_balance')
    beets_per_second = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='beetsPerSecond')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolStakingReliquaryFarmLevel')), graphql_name='levels')
    total_balance = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalBalance')
    total_weighted_balance = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalWeightedBalance')


class GqlPoolStakingReliquaryFarmLevel(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('allocation_points', 'apr', 'balance', 'id', 'level', 'required_maturity')
    allocation_points = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='allocationPoints')
    apr = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='apr')
    balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='balance')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')
    required_maturity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='requiredMaturity')


class GqlPoolStakingVebal(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'vebal_address')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    vebal_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vebalAddress')


class GqlPoolSwap(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('chain', 'id', 'pool_id', 'timestamp', 'token_amount_in', 'token_amount_out', 'token_in', 'token_out', 'tx', 'user_address', 'value_usd')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolId')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    token_amount_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAmountIn')
    token_amount_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAmountOut')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenIn')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenOut')
    tx = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tx')
    user_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userAddress')
    value_usd = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='valueUSD')


class GqlPoolTokenDetail(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'balance', 'balance_usd', 'can_use_buffer_for_swaps', 'chain', 'chain_id', 'coingecko_id', 'decimals', 'erc4626_review_data', 'has_nested_pool', 'id', 'index', 'is_allowed', 'is_erc4626', 'is_exempt_from_protocol_yield_fee', 'logo_uri', 'name', 'nested_pool', 'price_rate', 'price_rate_provider', 'price_rate_provider_data', 'scaling_factor', 'symbol', 'underlying_token', 'use_underlying_for_add_remove', 'use_wrapped_for_add_remove', 'weight')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    balance = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='balance')
    balance_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='balanceUSD')
    can_use_buffer_for_swaps = sgqlc.types.Field(Boolean, graphql_name='canUseBufferForSwaps')
    chain = sgqlc.types.Field(GqlChain, graphql_name='chain')
    chain_id = sgqlc.types.Field(Int, graphql_name='chainId')
    coingecko_id = sgqlc.types.Field(String, graphql_name='coingeckoId')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    erc4626_review_data = sgqlc.types.Field(Erc4626ReviewData, graphql_name='erc4626ReviewData')
    has_nested_pool = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNestedPool')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='index')
    is_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllowed')
    is_erc4626 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isErc4626')
    is_exempt_from_protocol_yield_fee = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isExemptFromProtocolYieldFee')
    logo_uri = sgqlc.types.Field(String, graphql_name='logoURI')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nested_pool = sgqlc.types.Field(GqlNestedPool, graphql_name='nestedPool')
    price_rate = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='priceRate')
    price_rate_provider = sgqlc.types.Field(String, graphql_name='priceRateProvider')
    price_rate_provider_data = sgqlc.types.Field('GqlPriceRateProviderData', graphql_name='priceRateProviderData')
    scaling_factor = sgqlc.types.Field(BigDecimal, graphql_name='scalingFactor')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    underlying_token = sgqlc.types.Field('GqlToken', graphql_name='underlyingToken')
    use_underlying_for_add_remove = sgqlc.types.Field(Boolean, graphql_name='useUnderlyingForAddRemove')
    use_wrapped_for_add_remove = sgqlc.types.Field(Boolean, graphql_name='useWrappedForAddRemove')
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')


class GqlPoolTokenDisplay(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'id', 'name', 'nested_tokens', 'symbol', 'weight')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nested_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolTokenDisplay')), graphql_name='nestedTokens')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')


class GqlPoolTokenExpanded(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'decimals', 'id', 'is_erc4626', 'is_main_token', 'is_nested', 'is_phantom_bpt', 'name', 'symbol', 'weight')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_erc4626 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isErc4626')
    is_main_token = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMainToken')
    is_nested = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isNested')
    is_phantom_bpt = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPhantomBpt')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    weight = sgqlc.types.Field(String, graphql_name='weight')


class GqlPoolUserBalance(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('staked_balances', 'total_balance', 'total_balance_usd', 'wallet_balance', 'wallet_balance_usd')
    staked_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlUserStakedBalance'))), graphql_name='stakedBalances')
    total_balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalBalance')
    total_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='totalBalanceUsd')
    wallet_balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='walletBalance')
    wallet_balance_usd = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='walletBalanceUsd')


class GqlPoolUserSwapVolume(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('swap_volume_usd', 'user_address')
    swap_volume_usd = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapVolumeUSD')
    user_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userAddress')


class GqlPoolWithdrawConfig(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('options', 'proportional_enabled', 'single_asset_enabled')
    options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolWithdrawOption'))), graphql_name='options')
    proportional_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='proportionalEnabled')
    single_asset_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='singleAssetEnabled')


class GqlPoolWithdrawOption(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('pool_token_address', 'pool_token_index', 'token_options')
    pool_token_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolTokenAddress')
    pool_token_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='poolTokenIndex')
    token_options = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlPoolToken'))), graphql_name='tokenOptions')


class GqlPriceImpact(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('error', 'price_impact')
    error = sgqlc.types.Field(String, graphql_name='error')
    price_impact = sgqlc.types.Field(AmountHumanReadable, graphql_name='priceImpact')


class GqlPriceRateProviderData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'factory', 'name', 'review_file', 'reviewed', 'summary', 'upgradeable_components', 'warnings')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    factory = sgqlc.types.Field(String, graphql_name='factory')
    name = sgqlc.types.Field(String, graphql_name='name')
    review_file = sgqlc.types.Field(String, graphql_name='reviewFile')
    reviewed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='reviewed')
    summary = sgqlc.types.Field(String, graphql_name='summary')
    upgradeable_components = sgqlc.types.Field(sgqlc.types.list_of('GqlPriceRateProviderUpgradeableComponent'), graphql_name='upgradeableComponents')
    warnings = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='warnings')


class GqlPriceRateProviderUpgradeableComponent(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('entry_point', 'implementation_reviewed')
    entry_point = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='entryPoint')
    implementation_reviewed = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='implementationReviewed')


class GqlProtocolMetricsAggregated(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('chains', 'num_liquidity_providers', 'pool_count', 'swap_fee24h', 'swap_volume24h', 'total_liquidity', 'yield_capture24h')
    chains = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlProtocolMetricsChain'))), graphql_name='chains')
    num_liquidity_providers = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='numLiquidityProviders')
    pool_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='poolCount')
    swap_fee24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapFee24h')
    swap_volume24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapVolume24h')
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidity')
    yield_capture24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='yieldCapture24h')


class GqlProtocolMetricsChain(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('chain_id', 'num_liquidity_providers', 'pool_count', 'swap_fee24h', 'swap_volume24h', 'total_liquidity', 'yield_capture24h')
    chain_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chainId')
    num_liquidity_providers = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='numLiquidityProviders')
    pool_count = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='poolCount')
    swap_fee24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapFee24h')
    swap_volume24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapVolume24h')
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='totalLiquidity')
    yield_capture24h = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='yieldCapture24h')


class GqlRelicSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('balance', 'entry_timestamp', 'farm_id', 'level', 'relic_id')
    balance = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='balance')
    entry_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='entryTimestamp')
    farm_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='farmId')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')
    relic_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='relicId')


class GqlReliquaryFarmLevelSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('balance', 'id', 'level')
    balance = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='balance')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    level = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='level')


class GqlReliquaryFarmSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('daily_deposited', 'daily_withdrawn', 'farm_id', 'id', 'level_balances', 'relic_count', 'timestamp', 'token_balances', 'total_balance', 'total_liquidity', 'user_count')
    daily_deposited = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dailyDeposited')
    daily_withdrawn = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dailyWithdrawn')
    farm_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='farmId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    level_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlReliquaryFarmLevelSnapshot))), graphql_name='levelBalances')
    relic_count = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relicCount')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    token_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlReliquaryTokenBalanceSnapshot'))), graphql_name='tokenBalances')
    total_balance = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalBalance')
    total_liquidity = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='totalLiquidity')
    user_count = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userCount')


class GqlReliquaryTokenBalanceSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'balance', 'decimals', 'id', 'name', 'symbol')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    balance = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='balance')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')


class GqlSftmxStakingData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('exchange_rate', 'maintenance_paused', 'max_deposit_limit', 'min_deposit_limit', 'number_of_vaults', 'staking_apr', 'total_ftm_amount', 'total_ftm_amount_in_pool', 'total_ftm_amount_staked', 'undelegate_paused', 'vaults', 'withdraw_paused', 'withdrawal_delay')
    exchange_rate = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='exchangeRate')
    maintenance_paused = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='maintenancePaused')
    max_deposit_limit = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='maxDepositLimit')
    min_deposit_limit = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='minDepositLimit')
    number_of_vaults = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='numberOfVaults')
    staking_apr = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stakingApr')
    total_ftm_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalFtmAmount')
    total_ftm_amount_in_pool = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalFtmAmountInPool')
    total_ftm_amount_staked = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalFtmAmountStaked')
    undelegate_paused = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='undelegatePaused')
    vaults = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlSftmxStakingVault'))), graphql_name='vaults')
    withdraw_paused = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='withdrawPaused')
    withdrawal_delay = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='withdrawalDelay')


class GqlSftmxStakingSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('exchange_rate', 'id', 'timestamp', 'total_ftm_amount', 'total_ftm_amount_in_pool', 'total_ftm_amount_staked')
    exchange_rate = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='exchangeRate')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    total_ftm_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalFtmAmount')
    total_ftm_amount_in_pool = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalFtmAmountInPool')
    total_ftm_amount_staked = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalFtmAmountStaked')


class GqlSftmxStakingVault(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('ftm_amount_staked', 'is_matured', 'unlock_timestamp', 'validator_address', 'validator_id', 'vault_address', 'vault_index')
    ftm_amount_staked = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='ftmAmountStaked')
    is_matured = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMatured')
    unlock_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='unlockTimestamp')
    validator_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='validatorAddress')
    validator_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='validatorId')
    vault_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vaultAddress')
    vault_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='vaultIndex')


class GqlSftmxWithdrawalRequests(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('amount_sftmx', 'id', 'is_withdrawn', 'request_timestamp', 'user')
    amount_sftmx = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='amountSftmx')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    is_withdrawn = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isWithdrawn')
    request_timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='requestTimestamp')
    user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='user')


class GqlSorCallData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('call_data', 'max_amount_in_raw', 'min_amount_out_raw', 'to', 'value')
    call_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='callData')
    max_amount_in_raw = sgqlc.types.Field(String, graphql_name='maxAmountInRaw')
    min_amount_out_raw = sgqlc.types.Field(String, graphql_name='minAmountOutRaw')
    to = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='to')
    value = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='value')


class GqlSorGetSwapPaths(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('effective_price', 'effective_price_reversed', 'paths', 'price_impact', 'protocol_version', 'return_amount', 'return_amount_raw', 'routes', 'swap_amount', 'swap_amount_raw', 'swap_type', 'swaps', 'token_addresses', 'token_in', 'token_in_amount', 'token_out', 'token_out_amount')
    effective_price = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='effectivePrice')
    effective_price_reversed = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='effectivePriceReversed')
    paths = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlSorPath'))), graphql_name='paths')
    price_impact = sgqlc.types.Field(sgqlc.types.non_null(GqlPriceImpact), graphql_name='priceImpact')
    protocol_version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='protocolVersion')
    return_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='returnAmount')
    return_amount_raw = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='returnAmountRaw')
    routes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlSorSwapRoute'))), graphql_name='routes')
    swap_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='swapAmount')
    swap_amount_raw = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='swapAmountRaw')
    swap_type = sgqlc.types.Field(sgqlc.types.non_null(GqlSorSwapType), graphql_name='swapType')
    swaps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlSorSwap'))), graphql_name='swaps')
    token_addresses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tokenAddresses')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenIn')
    token_in_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='tokenInAmount')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenOut')
    token_out_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='tokenOutAmount')


class GqlSorPath(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('input_amount_raw', 'is_buffer', 'output_amount_raw', 'pools', 'protocol_version', 'tokens')
    input_amount_raw = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inputAmountRaw')
    is_buffer = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Boolean))), graphql_name='isBuffer')
    output_amount_raw = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='outputAmountRaw')
    pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='pools')
    protocol_version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='protocolVersion')
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Token'))), graphql_name='tokens')


class GqlSorSwap(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('amount', 'asset_in_index', 'asset_out_index', 'pool_id', 'user_data')
    amount = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='amount')
    asset_in_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='assetInIndex')
    asset_out_index = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='assetOutIndex')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolId')
    user_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userData')


class GqlSorSwapRoute(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('hops', 'share', 'token_in', 'token_in_amount', 'token_out', 'token_out_amount')
    hops = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlSorSwapRouteHop'))), graphql_name='hops')
    share = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='share')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenIn')
    token_in_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='tokenInAmount')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenOut')
    token_out_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='tokenOutAmount')


class GqlSorSwapRouteHop(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('pool', 'pool_id', 'token_in', 'token_in_amount', 'token_out', 'token_out_amount')
    pool = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolMinimal), graphql_name='pool')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolId')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenIn')
    token_in_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='tokenInAmount')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenOut')
    token_out_amount = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='tokenOutAmount')


class GqlStakedSonicData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('delegated_validators', 'exchange_rate', 'protocol_fee24h', 'rewards_claimed24h', 'staking_apr', 'total_assets', 'total_assets_delegated', 'total_assets_pool')
    delegated_validators = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GqlStakedSonicDelegatedValidator'))), graphql_name='delegatedValidators')
    exchange_rate = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='exchangeRate')
    protocol_fee24h = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='protocolFee24h')
    rewards_claimed24h = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rewardsClaimed24h')
    staking_apr = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stakingApr')
    total_assets = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalAssets')
    total_assets_delegated = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalAssetsDelegated')
    total_assets_pool = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalAssetsPool')


class GqlStakedSonicDelegatedValidator(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('assets_delegated', 'validator_id')
    assets_delegated = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='assetsDelegated')
    validator_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='validatorId')


class GqlStakedSonicSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('exchange_rate', 'id', 'protocol_fee24h', 'rewards_claimed24h', 'timestamp', 'total_assets', 'total_assets_delegated', 'total_assets_pool')
    exchange_rate = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='exchangeRate')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol_fee24h = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='protocolFee24h')
    rewards_claimed24h = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='rewardsClaimed24h')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')
    total_assets = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalAssets')
    total_assets_delegated = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalAssetsDelegated')
    total_assets_pool = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalAssetsPool')


class GqlToken(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'chain', 'chain_id', 'coingecko_id', 'decimals', 'description', 'discord_url', 'erc4626_review_data', 'is_buffer_allowed', 'is_erc4626', 'logo_uri', 'name', 'price_rate_provider_data', 'priority', 'symbol', 'telegram_url', 'tradable', 'twitter_username', 'types', 'underlying_token_address', 'website_url')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    chain_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='chainId')
    coingecko_id = sgqlc.types.Field(String, graphql_name='coingeckoId')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')
    description = sgqlc.types.Field(String, graphql_name='description')
    discord_url = sgqlc.types.Field(String, graphql_name='discordUrl')
    erc4626_review_data = sgqlc.types.Field(Erc4626ReviewData, graphql_name='erc4626ReviewData')
    is_buffer_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBufferAllowed')
    is_erc4626 = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isErc4626')
    logo_uri = sgqlc.types.Field(String, graphql_name='logoURI')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    price_rate_provider_data = sgqlc.types.Field(GqlPriceRateProviderData, graphql_name='priceRateProviderData')
    priority = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='priority')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    telegram_url = sgqlc.types.Field(String, graphql_name='telegramUrl')
    tradable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='tradable')
    twitter_username = sgqlc.types.Field(String, graphql_name='twitterUsername')
    types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(GqlTokenType)), graphql_name='types')
    underlying_token_address = sgqlc.types.Field(String, graphql_name='underlyingTokenAddress')
    website_url = sgqlc.types.Field(String, graphql_name='websiteUrl')


class GqlTokenCandlestickChartDataItem(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('close', 'high', 'id', 'low', 'open', 'timestamp')
    close = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='close')
    high = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='high')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    low = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='low')
    open = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='open')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')


class GqlTokenData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('description', 'discord_url', 'id', 'telegram_url', 'token_address', 'twitter_username', 'website_url')
    description = sgqlc.types.Field(String, graphql_name='description')
    discord_url = sgqlc.types.Field(String, graphql_name='discordUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    telegram_url = sgqlc.types.Field(String, graphql_name='telegramUrl')
    token_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAddress')
    twitter_username = sgqlc.types.Field(String, graphql_name='twitterUsername')
    website_url = sgqlc.types.Field(String, graphql_name='websiteUrl')


class GqlTokenDynamicData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('ath', 'atl', 'fdv', 'high24h', 'id', 'low24h', 'market_cap', 'price', 'price_change24h', 'price_change_percent7d', 'price_change_percent14d', 'price_change_percent24h', 'price_change_percent30d', 'token_address', 'updated_at')
    ath = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='ath')
    atl = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='atl')
    fdv = sgqlc.types.Field(String, graphql_name='fdv')
    high24h = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='high24h')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    low24h = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='low24h')
    market_cap = sgqlc.types.Field(String, graphql_name='marketCap')
    price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='price')
    price_change24h = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='priceChange24h')
    price_change_percent7d = sgqlc.types.Field(Float, graphql_name='priceChangePercent7d')
    price_change_percent14d = sgqlc.types.Field(Float, graphql_name='priceChangePercent14d')
    price_change_percent24h = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='priceChangePercent24h')
    price_change_percent30d = sgqlc.types.Field(Float, graphql_name='priceChangePercent30d')
    token_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAddress')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='updatedAt')


class GqlTokenMutationResult(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('chain', 'error', 'success')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    error = sgqlc.types.Field(String, graphql_name='error')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')


class GqlTokenPrice(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'chain', 'price', 'updated_at', 'updated_by')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='price')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='updatedAt')
    updated_by = sgqlc.types.Field(String, graphql_name='updatedBy')


class GqlTokenPriceChartDataItem(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'price', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    price = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='price')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')


class GqlUserFbeetsBalance(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('id', 'staked_balance', 'total_balance', 'wallet_balance')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    staked_balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='stakedBalance')
    total_balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalBalance')
    wallet_balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='walletBalance')


class GqlUserPoolBalance(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('chain', 'pool_id', 'staked_balance', 'token_address', 'token_price', 'total_balance', 'wallet_balance')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    pool_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolId')
    staked_balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='stakedBalance')
    token_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenAddress')
    token_price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='tokenPrice')
    total_balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='totalBalance')
    wallet_balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='walletBalance')


class GqlUserStakedBalance(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('balance', 'balance_usd', 'staking_id', 'staking_type')
    balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='balance')
    balance_usd = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='balanceUsd')
    staking_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='stakingId')
    staking_type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolStakingType), graphql_name='stakingType')


class GqlVeBalBalance(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('balance', 'chain', 'locked', 'locked_usd')
    balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='balance')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    locked = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='locked')
    locked_usd = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='lockedUsd')


class GqlVeBalLockSnapshot(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('balance', 'bias', 'slope', 'timestamp')
    balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='balance')
    bias = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bias')
    slope = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slope')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='timestamp')


class GqlVeBalUserData(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('balance', 'lock_snapshots', 'locked', 'locked_usd', 'rank')
    balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='balance')
    lock_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlVeBalLockSnapshot))), graphql_name='lockSnapshots')
    locked = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='locked')
    locked_usd = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='lockedUsd')
    rank = sgqlc.types.Field(Int, graphql_name='rank')


class GqlVotingGauge(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('added_timestamp', 'address', 'child_gauge_address', 'is_killed', 'relative_weight', 'relative_weight_cap')
    added_timestamp = sgqlc.types.Field(Int, graphql_name='addedTimestamp')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    child_gauge_address = sgqlc.types.Field(Bytes, graphql_name='childGaugeAddress')
    is_killed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isKilled')
    relative_weight = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='relativeWeight')
    relative_weight_cap = sgqlc.types.Field(String, graphql_name='relativeWeightCap')


class GqlVotingGaugeToken(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'logo_uri', 'symbol', 'underlying_token_address', 'weight')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    logo_uri = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='logoURI')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    underlying_token_address = sgqlc.types.Field(String, graphql_name='underlyingTokenAddress')
    weight = sgqlc.types.Field(String, graphql_name='weight')


class GqlVotingPool(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'chain', 'gauge', 'id', 'protocol_version', 'symbol', 'tokens', 'type')
    address = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='address')
    chain = sgqlc.types.Field(sgqlc.types.non_null(GqlChain), graphql_name='chain')
    gauge = sgqlc.types.Field(sgqlc.types.non_null(GqlVotingGauge), graphql_name='gauge')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    protocol_version = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='protocolVersion')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlVotingGaugeToken))), graphql_name='tokens')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolType), graphql_name='type')


class HookConfig(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('enable_hook_adjusted_amounts', 'should_call_after_add_liquidity', 'should_call_after_initialize', 'should_call_after_remove_liquidity', 'should_call_after_swap', 'should_call_before_add_liquidity', 'should_call_before_initialize', 'should_call_before_remove_liquidity', 'should_call_before_swap', 'should_call_compute_dynamic_swap_fee')
    enable_hook_adjusted_amounts = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='enableHookAdjustedAmounts')
    should_call_after_add_liquidity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shouldCallAfterAddLiquidity')
    should_call_after_initialize = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shouldCallAfterInitialize')
    should_call_after_remove_liquidity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shouldCallAfterRemoveLiquidity')
    should_call_after_swap = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shouldCallAfterSwap')
    should_call_before_add_liquidity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shouldCallBeforeAddLiquidity')
    should_call_before_initialize = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shouldCallBeforeInitialize')
    should_call_before_remove_liquidity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shouldCallBeforeRemoveLiquidity')
    should_call_before_swap = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shouldCallBeforeSwap')
    should_call_compute_dynamic_swap_fee = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='shouldCallComputeDynamicSwapFee')


class LiquidityManagement(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('disable_unbalanced_liquidity', 'enable_add_liquidity_custom', 'enable_donation', 'enable_remove_liquidity_custom')
    disable_unbalanced_liquidity = sgqlc.types.Field(Boolean, graphql_name='disableUnbalancedLiquidity')
    enable_add_liquidity_custom = sgqlc.types.Field(Boolean, graphql_name='enableAddLiquidityCustom')
    enable_donation = sgqlc.types.Field(Boolean, graphql_name='enableDonation')
    enable_remove_liquidity_custom = sgqlc.types.Field(Boolean, graphql_name='enableRemoveLiquidityCustom')


class MevTaxHookParams(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('max_mev_swap_fee_percentage', 'mev_tax_multiplier', 'mev_tax_threshold')
    max_mev_swap_fee_percentage = sgqlc.types.Field(String, graphql_name='maxMevSwapFeePercentage')
    mev_tax_multiplier = sgqlc.types.Field(String, graphql_name='mevTaxMultiplier')
    mev_tax_threshold = sgqlc.types.Field(String, graphql_name='mevTaxThreshold')


class Mutation(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('beets_pool_load_reliquary_snapshots_for_all_farms', 'beets_sync_fbeets_ratio', 'pool_load_on_chain_data_for_all_pools', 'pool_load_snapshots_for_pools', 'pool_reload_all_pool_aprs', 'pool_reload_pools', 'pool_reload_staking_for_all_pools', 'pool_sync_all_cow_snapshots', 'pool_sync_all_pools_from_subgraph', 'pool_sync_fx_quote_tokens', 'pool_update_lifetime_values_for_all_pools', 'pool_update_liquidity_values_for_all_pools', 'protocol_cache_metrics', 'sftmx_sync_staking_data', 'sftmx_sync_withdrawal_requests', 'token_delete_token_type', 'token_reload_all_token_types', 'token_reload_erc4626_tokens', 'token_reload_token_prices', 'token_sync_latest_fx_prices', 'token_sync_token_definitions', 'user_init_staked_balances', 'user_init_wallet_balances_for_all_pools', 'user_init_wallet_balances_for_pool', 'user_sync_balance', 'user_sync_balance_all_pools', 'user_sync_changed_staked_balances', 'user_sync_changed_wallet_balances_for_all_pools', 've_bal_sync_all_user_balances', 've_bal_sync_total_supply')
    beets_pool_load_reliquary_snapshots_for_all_farms = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='beetsPoolLoadReliquarySnapshotsForAllFarms', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(sgqlc.types.non_null(GqlChain), graphql_name='chain', default=None)),
))
    )
    beets_sync_fbeets_ratio = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='beetsSyncFbeetsRatio')
    pool_load_on_chain_data_for_all_pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolMutationResult))), graphql_name='poolLoadOnChainDataForAllPools', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain))), graphql_name='chains', default=None)),
))
    )
    pool_load_snapshots_for_pools = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolLoadSnapshotsForPools', args=sgqlc.types.ArgDict((
        ('pool_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='poolIds', default=None)),
        ('reload', sgqlc.types.Arg(Boolean, graphql_name='reload', default=None)),
))
    )
    pool_reload_all_pool_aprs = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolReloadAllPoolAprs', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(sgqlc.types.non_null(GqlChain), graphql_name='chain', default=None)),
))
    )
    pool_reload_pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolMutationResult))), graphql_name='poolReloadPools', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain))), graphql_name='chains', default=None)),
))
    )
    pool_reload_staking_for_all_pools = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolReloadStakingForAllPools', args=sgqlc.types.ArgDict((
        ('staking_types', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolStakingType))), graphql_name='stakingTypes', default=None)),
))
    )
    pool_sync_all_cow_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolMutationResult))), graphql_name='poolSyncAllCowSnapshots', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain))), graphql_name='chains', default=None)),
))
    )
    pool_sync_all_pools_from_subgraph = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='poolSyncAllPoolsFromSubgraph')
    pool_sync_fx_quote_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolMutationResult))), graphql_name='poolSyncFxQuoteTokens', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain))), graphql_name='chains', default=None)),
))
    )
    pool_update_lifetime_values_for_all_pools = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolUpdateLifetimeValuesForAllPools')
    pool_update_liquidity_values_for_all_pools = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolUpdateLiquidityValuesForAllPools')
    protocol_cache_metrics = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='protocolCacheMetrics')
    sftmx_sync_staking_data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sftmxSyncStakingData')
    sftmx_sync_withdrawal_requests = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sftmxSyncWithdrawalRequests')
    token_delete_token_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenDeleteTokenType', args=sgqlc.types.ArgDict((
        ('token_address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tokenAddress', default=None)),
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(GqlTokenType), graphql_name='type', default=None)),
))
    )
    token_reload_all_token_types = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenReloadAllTokenTypes')
    token_reload_erc4626_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlTokenMutationResult))), graphql_name='tokenReloadErc4626Tokens', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain))), graphql_name='chains', default=None)),
))
    )
    token_reload_token_prices = sgqlc.types.Field(Boolean, graphql_name='tokenReloadTokenPrices', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain))), graphql_name='chains', default=None)),
))
    )
    token_sync_latest_fx_prices = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenSyncLatestFxPrices', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(sgqlc.types.non_null(GqlChain), graphql_name='chain', default=None)),
))
    )
    token_sync_token_definitions = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tokenSyncTokenDefinitions')
    user_init_staked_balances = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userInitStakedBalances', args=sgqlc.types.ArgDict((
        ('staking_types', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolStakingType))), graphql_name='stakingTypes', default=None)),
))
    )
    user_init_wallet_balances_for_all_pools = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userInitWalletBalancesForAllPools', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
))
    )
    user_init_wallet_balances_for_pool = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userInitWalletBalancesForPool', args=sgqlc.types.ArgDict((
        ('pool_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='poolId', default=None)),
))
    )
    user_sync_balance = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userSyncBalance', args=sgqlc.types.ArgDict((
        ('pool_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='poolId', default=None)),
))
    )
    user_sync_balance_all_pools = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userSyncBalanceAllPools')
    user_sync_changed_staked_balances = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userSyncChangedStakedBalances')
    user_sync_changed_wallet_balances_for_all_pools = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userSyncChangedWalletBalancesForAllPools')
    ve_bal_sync_all_user_balances = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='veBalSyncAllUserBalances')
    ve_bal_sync_total_supply = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='veBalSyncTotalSupply')


class PoolForBatchSwap(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('all_tokens', 'id', 'name', 'symbol', 'type')
    all_tokens = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TokenForBatchSwapPool')), graphql_name='allTokens')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    symbol = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='symbol')
    type = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolType), graphql_name='type')


class QuantAMMWeightedDetail(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('category', 'name', 'type', 'value')
    category = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='category')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class QuantAmmWeightedParams(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('absolute_weight_guard_rail', 'details', 'epsilon_max', 'lambda_', 'last_interpolation_time_possible', 'last_update_interval_time', 'max_trade_size_ratio', 'oracle_staleness_threshold', 'pool_registry', 'update_interval', 'weight_block_multipliers', 'weights_at_last_update_interval')
    absolute_weight_guard_rail = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='absoluteWeightGuardRail')
    details = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(QuantAMMWeightedDetail))), graphql_name='details')
    epsilon_max = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='epsilonMax')
    lambda_ = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='lambda')
    last_interpolation_time_possible = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastInterpolationTimePossible')
    last_update_interval_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lastUpdateIntervalTime')
    max_trade_size_ratio = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='maxTradeSizeRatio')
    oracle_staleness_threshold = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oracleStalenessThreshold')
    pool_registry = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='poolRegistry')
    update_interval = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='updateInterval')
    weight_block_multipliers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='weightBlockMultipliers')
    weights_at_last_update_interval = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='weightsAtLastUpdateInterval')


class Query(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('aggregator_pools', 'beets_get_fbeets_ratio', 'beets_pool_get_reliquary_farm_snapshots', 'latest_synced_blocks', 'pool_events', 'pool_get_events', 'pool_get_featured_pools', 'pool_get_pool', 'pool_get_pools', 'pool_get_pools_count', 'pool_get_snapshots', 'protocol_metrics_aggregated', 'protocol_metrics_chain', 'sftmx_get_staking_data', 'sftmx_get_staking_snapshots', 'sftmx_get_withdrawal_requests', 'sor_get_swap_paths', 'sts_get_gql_staked_sonic_data', 'sts_get_staked_sonic_snapshots', 'token_get_current_prices', 'token_get_historical_prices', 'token_get_relative_price_chart_data', 'token_get_token_dynamic_data', 'token_get_tokens', 'token_get_tokens_dynamic_data', 'user_get_fbeets_balance', 'user_get_pool_balances', 'user_get_pool_join_exits', 'user_get_staking', 'user_get_swaps', 've_bal_get_total_supply', 've_bal_get_user', 've_bal_get_user_balance', 've_bal_get_user_balances', 've_bal_get_voting_list')
    aggregator_pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolAggregator))), graphql_name='aggregatorPools', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('order_by', sgqlc.types.Arg(GqlPoolOrderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(GqlPoolOrderDirection, graphql_name='orderDirection', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('where', sgqlc.types.Arg(GqlAggregatorPoolFilter, graphql_name='where', default=None)),
))
    )
    beets_get_fbeets_ratio = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='beetsGetFbeetsRatio')
    beets_pool_get_reliquary_farm_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlReliquaryFarmSnapshot))), graphql_name='beetsPoolGetReliquaryFarmSnapshots', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('range', sgqlc.types.Arg(sgqlc.types.non_null(GqlPoolSnapshotDataRange), graphql_name='range', default=None)),
))
    )
    latest_synced_blocks = sgqlc.types.Field(sgqlc.types.non_null(GqlLatestSyncedBlocks), graphql_name='latestSyncedBlocks')
    pool_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolEvent))), graphql_name='poolEvents', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('where', sgqlc.types.Arg(GqlPoolEventsFilter, graphql_name='where', default=None)),
))
    )
    pool_get_events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolEvent))), graphql_name='poolGetEvents', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(sgqlc.types.non_null(GqlChain), graphql_name='chain', default=None)),
        ('pool_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='poolId', default=None)),
        ('range', sgqlc.types.Arg(sgqlc.types.non_null(GqlPoolEventsDataRange), graphql_name='range', default=None)),
        ('type_in', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolEventType))), graphql_name='typeIn', default=None)),
        ('user_address', sgqlc.types.Arg(String, graphql_name='userAddress', default=None)),
))
    )
    pool_get_featured_pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolFeaturedPool))), graphql_name='poolGetFeaturedPools', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain))), graphql_name='chains', default=None)),
))
    )
    pool_get_pool = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolBase), graphql_name='poolGetPool', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('user_address', sgqlc.types.Arg(String, graphql_name='userAddress', default=None)),
))
    )
    pool_get_pools = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolMinimal))), graphql_name='poolGetPools', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('order_by', sgqlc.types.Arg(GqlPoolOrderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(GqlPoolOrderDirection, graphql_name='orderDirection', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('text_search', sgqlc.types.Arg(String, graphql_name='textSearch', default=None)),
        ('where', sgqlc.types.Arg(GqlPoolFilter, graphql_name='where', default=None)),
))
    )
    pool_get_pools_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='poolGetPoolsCount', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('order_by', sgqlc.types.Arg(GqlPoolOrderBy, graphql_name='orderBy', default=None)),
        ('order_direction', sgqlc.types.Arg(GqlPoolOrderDirection, graphql_name='orderDirection', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('text_search', sgqlc.types.Arg(String, graphql_name='textSearch', default=None)),
        ('where', sgqlc.types.Arg(GqlPoolFilter, graphql_name='where', default=None)),
))
    )
    pool_get_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolSnapshot))), graphql_name='poolGetSnapshots', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='id', default=None)),
        ('range', sgqlc.types.Arg(sgqlc.types.non_null(GqlPoolSnapshotDataRange), graphql_name='range', default=None)),
))
    )
    protocol_metrics_aggregated = sgqlc.types.Field(sgqlc.types.non_null(GqlProtocolMetricsAggregated), graphql_name='protocolMetricsAggregated', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chains', default=None)),
))
    )
    protocol_metrics_chain = sgqlc.types.Field(sgqlc.types.non_null(GqlProtocolMetricsChain), graphql_name='protocolMetricsChain', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
))
    )
    sftmx_get_staking_data = sgqlc.types.Field(sgqlc.types.non_null(GqlSftmxStakingData), graphql_name='sftmxGetStakingData')
    sftmx_get_staking_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlSftmxStakingSnapshot))), graphql_name='sftmxGetStakingSnapshots', args=sgqlc.types.ArgDict((
        ('range', sgqlc.types.Arg(sgqlc.types.non_null(GqlSftmxStakingSnapshotDataRange), graphql_name='range', default=None)),
))
    )
    sftmx_get_withdrawal_requests = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlSftmxWithdrawalRequests))), graphql_name='sftmxGetWithdrawalRequests', args=sgqlc.types.ArgDict((
        ('user', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='user', default=None)),
))
    )
    sor_get_swap_paths = sgqlc.types.Field(sgqlc.types.non_null(GqlSorGetSwapPaths), graphql_name='sorGetSwapPaths', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(sgqlc.types.non_null(GqlChain), graphql_name='chain', default=None)),
        ('consider_pools_with_hooks', sgqlc.types.Arg(Boolean, graphql_name='considerPoolsWithHooks', default=None)),
        ('pool_ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='poolIds', default=None)),
        ('swap_amount', sgqlc.types.Arg(sgqlc.types.non_null(AmountHumanReadable), graphql_name='swapAmount', default=None)),
        ('swap_type', sgqlc.types.Arg(sgqlc.types.non_null(GqlSorSwapType), graphql_name='swapType', default=None)),
        ('token_in', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tokenIn', default=None)),
        ('token_out', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tokenOut', default=None)),
        ('use_protocol_version', sgqlc.types.Arg(Int, graphql_name='useProtocolVersion', default=None)),
))
    )
    sts_get_gql_staked_sonic_data = sgqlc.types.Field(sgqlc.types.non_null(GqlStakedSonicData), graphql_name='stsGetGqlStakedSonicData')
    sts_get_staked_sonic_snapshots = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlStakedSonicSnapshot))), graphql_name='stsGetStakedSonicSnapshots', args=sgqlc.types.ArgDict((
        ('range', sgqlc.types.Arg(sgqlc.types.non_null(GqlStakedSonicSnapshotDataRange), graphql_name='range', default=None)),
))
    )
    token_get_current_prices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlTokenPrice))), graphql_name='tokenGetCurrentPrices', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chains', default=None)),
))
    )
    token_get_historical_prices = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlHistoricalTokenPrice))), graphql_name='tokenGetHistoricalPrices', args=sgqlc.types.ArgDict((
        ('addresses', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='addresses', default=None)),
        ('chain', sgqlc.types.Arg(sgqlc.types.non_null(GqlChain), graphql_name='chain', default=None)),
        ('range', sgqlc.types.Arg(sgqlc.types.non_null(GqlTokenChartDataRange), graphql_name='range', default=None)),
))
    )
    token_get_relative_price_chart_data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlTokenPriceChartDataItem))), graphql_name='tokenGetRelativePriceChartData', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
        ('range', sgqlc.types.Arg(sgqlc.types.non_null(GqlTokenChartDataRange), graphql_name='range', default=None)),
        ('token_in', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tokenIn', default=None)),
        ('token_out', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tokenOut', default=None)),
))
    )
    token_get_token_dynamic_data = sgqlc.types.Field(GqlTokenDynamicData, graphql_name='tokenGetTokenDynamicData', args=sgqlc.types.ArgDict((
        ('address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='address', default=None)),
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
))
    )
    token_get_tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlToken))), graphql_name='tokenGetTokens', args=sgqlc.types.ArgDict((
        ('chains', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chains', default=None)),
        ('where', sgqlc.types.Arg(GqlTokenFilter, graphql_name='where', default=None)),
))
    )
    token_get_tokens_dynamic_data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlTokenDynamicData))), graphql_name='tokenGetTokensDynamicData', args=sgqlc.types.ArgDict((
        ('addresses', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='addresses', default=None)),
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
))
    )
    user_get_fbeets_balance = sgqlc.types.Field(sgqlc.types.non_null(GqlUserFbeetsBalance), graphql_name='userGetFbeetsBalance')
    user_get_pool_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlUserPoolBalance))), graphql_name='userGetPoolBalances', args=sgqlc.types.ArgDict((
        ('address', sgqlc.types.Arg(String, graphql_name='address', default=None)),
        ('chains', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chains', default=None)),
))
    )
    user_get_pool_join_exits = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolJoinExit))), graphql_name='userGetPoolJoinExits', args=sgqlc.types.ArgDict((
        ('address', sgqlc.types.Arg(String, graphql_name='address', default=None)),
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=10)),
        ('pool_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='poolId', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
))
    )
    user_get_staking = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolStaking))), graphql_name='userGetStaking', args=sgqlc.types.ArgDict((
        ('address', sgqlc.types.Arg(String, graphql_name='address', default=None)),
        ('chains', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chains', default=None)),
))
    )
    user_get_swaps = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolSwap))), graphql_name='userGetSwaps', args=sgqlc.types.ArgDict((
        ('address', sgqlc.types.Arg(String, graphql_name='address', default=None)),
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=10)),
        ('pool_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='poolId', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=0)),
))
    )
    ve_bal_get_total_supply = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='veBalGetTotalSupply', args=sgqlc.types.ArgDict((
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
))
    )
    ve_bal_get_user = sgqlc.types.Field(sgqlc.types.non_null(GqlVeBalUserData), graphql_name='veBalGetUser', args=sgqlc.types.ArgDict((
        ('address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='address', default=None)),
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
))
    )
    ve_bal_get_user_balance = sgqlc.types.Field(sgqlc.types.non_null(AmountHumanReadable), graphql_name='veBalGetUserBalance', args=sgqlc.types.ArgDict((
        ('address', sgqlc.types.Arg(String, graphql_name='address', default=None)),
        ('chain', sgqlc.types.Arg(GqlChain, graphql_name='chain', default=None)),
))
    )
    ve_bal_get_user_balances = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlVeBalBalance))), graphql_name='veBalGetUserBalances', args=sgqlc.types.ArgDict((
        ('address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='address', default=None)),
        ('chains', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(GqlChain)), graphql_name='chains', default=None)),
))
    )
    ve_bal_get_voting_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlVotingPool))), graphql_name='veBalGetVotingList', args=sgqlc.types.ArgDict((
        ('include_killed', sgqlc.types.Arg(Boolean, graphql_name='includeKilled', default=None)),
))
    )


class StableSurgeHookParams(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('max_surge_fee_percentage', 'surge_threshold_percentage')
    max_surge_fee_percentage = sgqlc.types.Field(String, graphql_name='maxSurgeFeePercentage')
    surge_threshold_percentage = sgqlc.types.Field(String, graphql_name='surgeThresholdPercentage')


class Token(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'decimals')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    decimals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='decimals')


class TokenForBatchSwapPool(sgqlc.types.Type):
    __schema__ = graphql_schema
    __field_names__ = ('address', 'is_nested', 'is_phantom_bpt', 'weight')
    address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='address')
    is_nested = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isNested')
    is_phantom_bpt = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPhantomBpt')
    weight = sgqlc.types.Field(BigDecimal, graphql_name='weight')


class GqlPoolAddRemoveEventV3(sgqlc.types.Type, GqlPoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('tokens',)
    tokens = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(GqlPoolEventAmount))), graphql_name='tokens')


class GqlPoolComposableStable(sgqlc.types.Type, GqlPoolBase):
    __schema__ = graphql_schema
    __field_names__ = ('amp', 'bpt_price_rate')
    amp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amp')
    bpt_price_rate = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='bptPriceRate')


class GqlPoolElement(sgqlc.types.Type, GqlPoolBase):
    __schema__ = graphql_schema
    __field_names__ = ('base_token', 'principal_token', 'unit_seconds')
    base_token = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='baseToken')
    principal_token = sgqlc.types.Field(sgqlc.types.non_null(Bytes), graphql_name='principalToken')
    unit_seconds = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='unitSeconds')


class GqlPoolFx(sgqlc.types.Type, GqlPoolBase):
    __schema__ = graphql_schema
    __field_names__ = ('alpha', 'beta', 'delta', 'epsilon', 'lambda_')
    alpha = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alpha')
    beta = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='beta')
    delta = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='delta')
    epsilon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='epsilon')
    lambda_ = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lambda')


class GqlPoolGyro(sgqlc.types.Type, GqlPoolBase):
    __schema__ = graphql_schema
    __field_names__ = ('alpha', 'beta', 'c', 'd_sq', 'lambda_', 'root3_alpha', 's', 'sqrt_alpha', 'sqrt_beta', 'tau_alpha_x', 'tau_alpha_y', 'tau_beta_x', 'tau_beta_y', 'u', 'v', 'w', 'z')
    alpha = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alpha')
    beta = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='beta')
    c = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='c')
    d_sq = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='dSq')
    lambda_ = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='lambda')
    root3_alpha = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='root3Alpha')
    s = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='s')
    sqrt_alpha = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sqrtAlpha')
    sqrt_beta = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='sqrtBeta')
    tau_alpha_x = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tauAlphaX')
    tau_alpha_y = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tauAlphaY')
    tau_beta_x = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tauBetaX')
    tau_beta_y = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tauBetaY')
    u = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='u')
    v = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='v')
    w = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='w')
    z = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='z')


class GqlPoolLiquidityBootstrapping(sgqlc.types.Type, GqlPoolBase):
    __schema__ = graphql_schema
    __field_names__ = ()


class GqlPoolMetaStable(sgqlc.types.Type, GqlPoolBase):
    __schema__ = graphql_schema
    __field_names__ = ('amp',)
    amp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amp')


class GqlPoolQuantAmmWeighted(sgqlc.types.Type, GqlPoolBase):
    __schema__ = graphql_schema
    __field_names__ = ('quant_amm_weighted_params',)
    quant_amm_weighted_params = sgqlc.types.Field(QuantAmmWeightedParams, graphql_name='quantAmmWeightedParams')


class GqlPoolStable(sgqlc.types.Type, GqlPoolBase):
    __schema__ = graphql_schema
    __field_names__ = ('amp', 'bpt_price_rate')
    amp = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amp')
    bpt_price_rate = sgqlc.types.Field(sgqlc.types.non_null(BigDecimal), graphql_name='bptPriceRate')


class GqlPoolSwapEventCowAmm(sgqlc.types.Type, GqlPoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('fee', 'surplus', 'token_in', 'token_out')
    fee = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolEventAmount), graphql_name='fee')
    surplus = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolEventAmount), graphql_name='surplus')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolEventAmount), graphql_name='tokenIn')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolEventAmount), graphql_name='tokenOut')


class GqlPoolSwapEventV3(sgqlc.types.Type, GqlPoolEvent):
    __schema__ = graphql_schema
    __field_names__ = ('fee', 'token_in', 'token_out')
    fee = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolEventAmount), graphql_name='fee')
    token_in = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolEventAmount), graphql_name='tokenIn')
    token_out = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolEventAmount), graphql_name='tokenOut')


class GqlPoolToken(sgqlc.types.Type, GqlPoolTokenBase):
    __schema__ = graphql_schema
    __field_names__ = ()


class GqlPoolTokenComposableStable(sgqlc.types.Type, GqlPoolTokenBase):
    __schema__ = graphql_schema
    __field_names__ = ('pool',)
    pool = sgqlc.types.Field(sgqlc.types.non_null(GqlPoolComposableStableNested), graphql_name='pool')


class GqlPoolWeighted(sgqlc.types.Type, GqlPoolBase):
    __schema__ = graphql_schema
    __field_names__ = ()



########################################################################
# Unions
########################################################################
class GqlPoolAprValue(sgqlc.types.Union):
    __schema__ = graphql_schema
    __types__ = (GqlPoolAprRange, GqlPoolAprTotal)


class GqlPoolFeaturedPoolGroupItem(sgqlc.types.Union):
    __schema__ = graphql_schema
    __types__ = (GqlFeaturePoolGroupItemExternalLink, GqlPoolMinimal)


class GqlPoolNestedUnion(sgqlc.types.Union):
    __schema__ = graphql_schema
    __types__ = (GqlPoolComposableStableNested,)


class GqlPoolTokenComposableStableNestedUnion(sgqlc.types.Union):
    __schema__ = graphql_schema
    __types__ = (GqlPoolToken,)


class GqlPoolTokenUnion(sgqlc.types.Union):
    __schema__ = graphql_schema
    __types__ = (GqlPoolToken, GqlPoolTokenComposableStable)


class GqlPoolUnion(sgqlc.types.Union):
    __schema__ = graphql_schema
    __types__ = (GqlPoolComposableStable, GqlPoolElement, GqlPoolFx, GqlPoolGyro, GqlPoolLiquidityBootstrapping, GqlPoolMetaStable, GqlPoolQuantAmmWeighted, GqlPoolStable, GqlPoolWeighted)


class HookParams(sgqlc.types.Union):
    __schema__ = graphql_schema
    __types__ = (ExitFeeHookParams, FeeTakingHookParams, MevTaxHookParams, StableSurgeHookParams)



########################################################################
# Schema Entry Points
########################################################################
graphql_schema.query_type = Query
graphql_schema.mutation_type = Mutation
graphql_schema.subscription_type = None

