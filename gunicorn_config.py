from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

def child_exit(server, worker):
    """Handler for gunicorn 'worker_exit' signal to allow prometheus metrics
    to be properly handled in a multiprocess environment.
    """
    GunicornInternalPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)
