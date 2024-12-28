from prometheus_client import Counter, Gauge, Summary


refresh_driver_error = Counter('lpbook_refresh_driver_error', 'Driver refresh errors.', ['protocol'])
lps_trading_tokens_time = Summary('lpbook_lps_trading_tokens_time', 'Time for serving lps_trading_tokens endpoint.')
order_lps_time = Summary('lpbook_order_lps_time', 'Time for serving order_lps endpoint.')
blacklisted_lps = Gauge('lpbook_blacklisted_lp', 'Best objective/quasilabs objective.', ['lp_id'])
error = Counter('lpbook_error', 'Errors in LPBook.', ['error_type'])
