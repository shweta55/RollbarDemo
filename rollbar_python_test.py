import rollbar

rollbar.init('42c52e40db79498c8ca8694fef842d2f')

try:
    a = 0
    b = 10 / a
    rollbar.report_message('Rollbar is configured correctly')
except:
    rollbar.report_exc_info()