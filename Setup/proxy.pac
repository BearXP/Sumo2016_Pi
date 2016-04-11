//pacfile for 203.12.244.3 from 41554_2914:2_9612
function FindProxyForURL(url, host)
{
    /* Convert the host parameter to lowercase
       to facilitate case insensitive matching.
    */
    host = host.toLowerCase();


    /* Don't proxy local hostnames */
    if (isPlainHostName(host))
    {
        return 'DIRECT';
    }

    /* always proxy on normal service address/port for the login host */
    if (shExpMatch(host, '*proxy-login.blackspider.com'))
    {
        return 'PROXY ipv4.203.12.244.3.webdefence.global.blackspider.com:8081';
    }

    /* Don't proxy local domains */
    var domain_list = new Array("leica-microsystems.com",
"login.danaherconnect.com",
"leicams.com",
"insightplus.optus.com.au",
"geotrust-timestamp-gslb.geotrust.net",
"webex.com",
"talk2m.com",
"leicabio.com",
"*.azurewebsites.windows.net",
"vsl.com.au",
"vision-bio.com",
"invetech.com.au",
"download.global.blackspider.com",
"aib.edu.au",
"safetyshare77.com",
"mydanaher.com",
"danaherprocurement.com",
"danaherconnect.com",
"gilbarco.com",
"cloudapp.net",
"seaconworldwide.com",
"ato.gov.au",
"htgmolecular.com",
"timestamp.geotrust.com",
"igus-cad.com",
"partcommunity.com",
"cadclick.com",
"autodiscover.leicabiosystems.com",
"autodiscover.danahermail.com",
"autodiscover-s.outlook.com");
    for (d in domain_list)
    {
        if ( dnsDomainIs(host, "." + domain_list[d] ) || host == domain_list[d] )
        {
            return 'DIRECT';
        }
    }

    /* Don't proxy portal addresses */
    if ((host == 'www.blackspider.com') ||
dnsDomainIs(host, '.mailcontrol.com') ||
(host == 'home.webdefence.global.blackspider.com') ||
(host == 'webdefence.global.blackspider.com') ||
(host == 'hybrid-web.global.blackspider.com') ||
(host == 'pac.webdefence.global.blackspider.com') ||
(host == 'pac.hybrid-web.global.blackspider.com') ||
(host == 'download.global.blackspider.com') ||
(host == 'mobile.websense.net') ||
(host == 'mdm.websense.net') ||
(host == 'admin.websense.net') ||
(host == 'status.websense.net') ||
(host == 'mobile.forcepoint.net') ||
(host == 'mdm.forcepoint.net') ||
(host == 'admin.forcepoint.net') ||
(host == 'status.forcepoint.net') ||
(host == 'epevents.blackspider.com'))
    {
        return 'DIRECT';
    }

    /* Don't proxy Windows Update */
    if ((host == "download.microsoft.com") ||
(host == "ntservicepack.microsoft.com") ||
(host == "cdm.microsoft.com") ||
(host == "officecdn.microsoft.com.edgesuite.net") ||
(host == "wustat.windows.com") ||
(host == "windowsupdate.microsoft.com") ||
(dnsDomainIs(host, ".windowsupdate.microsoft.com")) ||
(host == "update.microsoft.com") ||
(dnsDomainIs(host, ".update.microsoft.com")) ||
(dnsDomainIs(host, ".windowsupdate.com")) ||
(dnsDomainIs(host, ".v4.download.windowsupdate.com")) ||
(dnsDomainIs(host, ".mp.microsoft.com")) ||
(dnsDomainIs(host, ".dl.ws.microsoft.com")))
    {
        return 'DIRECT';
    }

    /* Don't proxy Office 365 */
    var domain_pattern_list = new Array();
    for (d in domain_pattern_list)
    {
        if (shExpMatch(host, domain_pattern_list[d]))
        {
            return 'DIRECT';
        }
    }

    /* Don't proxy redirects to SSO gateway */
    if (false)
    {
        return 'DIRECT';
    }

    /* Handle SSO redirector requests for roaming users */
    if (false)
    {
        return 'DIRECT';
    }

    /* Query page should always resolve to the proxy - even if it's treated as a local address */
    if (isResolvable(host) & !(shExpMatch(url, 'http://query.webdefence.global.blackspider.com/*')))
    {
        var hostIP = dnsResolve(host);

        /* Don't proxy non-routable addresses (RFC 3330) */
        if (isInNet(hostIP, '0.0.0.0', '255.0.0.0') ||
isInNet(hostIP, '10.0.0.0', '255.0.0.0') ||
isInNet(hostIP, '127.0.0.0', '255.0.0.0') ||
isInNet(hostIP, '169.254.0.0', '255.255.0.0') ||
isInNet(hostIP, '172.16.0.0', '255.240.0.0') ||
isInNet(hostIP, '192.0.2.0', '255.255.255.0') ||
isInNet(hostIP, '192.88.99.0', '255.255.255.0') ||
isInNet(hostIP, '192.168.0.0', '255.255.0.0') ||
isInNet(hostIP, '198.18.0.0', '255.254.0.0') ||
isInNet(hostIP, '224.0.0.0', '240.0.0.0') ||
isInNet(hostIP, '240.0.0.0', '240.0.0.0'))
        {
            return 'DIRECT';
        }

        /* Don't proxy local addresses */
        if (isInNet(hostIP, "203.12.244.50", "255.255.255.255") ||
isInNet(hostIP, "184.106.33.41", "255.255.255.255") ||
isInNet(hostIP, "193.221.131.0", "255.255.255.0") ||
isInNet(hostIP, "10.10.250.17", "255.255.255.255"))
        {
            return 'DIRECT';
        }
    }

    if (url.substring(0, 6) == 'https:')
    {
        var pats = new Array("");
        for (i in pats)
        {
            if (shExpMatch(host, pats[i].toLowerCase()))
            {
                // non-SSL-terminate hosts must use the normal address/port
                return 'PROXY ipv4.203.12.244.3.webdefence.global.blackspider.com:8081';
            }
        }
    }
    if (url.substring(0, 5) == 'http:' || url.substring(0, 6) == 'https:')
    {
        return 'PROXY ipv4.203.12.244.3.webdefence.global.blackspider.com:8081';
    }
    if (url.substring(0, 4) == 'ftp:')
    {
        // ftp must use the normal address/port
        return 'PROXY ipv4.203.12.244.3.webdefence.global.blackspider.com:8081';
    }
    return 'DIRECT';
}
