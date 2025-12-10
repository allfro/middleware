<%
    from middlewared.utils.origin import HA_HEARTBEAT_IPS
    if render_ctx['failover.status'] == 'SINGLE':
        raise FileShouldNotExist
%>

${'\n'.join(HA_HEARTBEAT_IPS)}
