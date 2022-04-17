'use strict';

var showPanel = false;
var showPanelCount = 0;

// var showPanelPermission = true;
// var openPermissionPanelCounter = 0;
var showPanelSupport = false;
var openSupportPanelCounter = 0;
var browserLanguage = chrome.i18n.getUILanguage().split('-')[1];

if (browserLanguage === undefined) {
    browserLanguage = chrome.i18n.getUILanguage().split('-')[0].toLowerCase();
} else {
    browserLanguage = browserLanguage.toLowerCase()
}



chrome.storage.local.get(['showPanel'], function (fetched) {
    if (fetched.showPanel !== undefined) {
        var result = Math.abs(fetched.showPanel - Date.now()) / 1000;
        var days = Math.floor(result / 86400);
        var minutes = Math.floor(result / 60) % 60;
        // 
        
        if (days === 3) {
            showPanel = true;
            chrome.storage.local.get(['showPanelCount'], function (data) {
                if (data.showPanelCount !== undefined) {
                    chrome.storage.local.set({ 'showPanelCount': data.showPanelCount + 1 });
                } else {
                    chrome.storage.local.set({ 'showPanelCount': 0 });
                }
            });
        }
    } else {
        chrome.storage.local.set({ 'showPanel': Date.now() });
    }
});

// // Check open permission panel
// // Display 2 times only before a date
// chrome.storage.local.get(['installDate'], function (data) {
//     if (data.installDate !== undefined) {
//         var result = Math.abs(data.installDate - Date.now()) / 1000;
//         var days = Math.floor(result / 86400);
//         var minutes = Math.floor(result / 60) % 60;
//         // 
        
//         // for open permission panel
//         if (days < 100000) {
//             chrome.storage.local.get(['openPanelCount'], function (data) {
//                 if (data.openPanelCount !== undefined) {
//                     openPermissionPanelCounter = data.openPanelCount;
//                     chrome.storage.local.set({openPanelCount: openPermissionPanelCounter + 1}, function () {});
//                 } else {
//                     openPermissionPanelCounter = 1;
//                     chrome.storage.local.set({openPanelCount: openPermissionPanelCounter}, function () {});
//                 }
//             });
//         } else {
//             openPermissionPanelCounter = 4;
//             chrome.storage.local.set({openPanelCount: openPermissionPanelCounter}, function () {});
//         }
//     }
// });

// Check open support panel
// display 2 times after 14 days
chrome.storage.local.get(['supportDate'], function (data) {
    if (data.supportDate !== undefined) {
        
        var result = Math.abs(data.supportDate - Date.now()) / 1000;
        var days = Math.floor(result / 86400);
        var minutes = Math.floor(result / 60) % 60;

        // show panel only if browser langugage is set to FR, ES or UK
        if (browserLanguage == "de" || browserLanguage == "es" || browserLanguage == "fr" || browserLanguage == "nl") {
            if (days >= 14) { // show after 14 days
                showPanelSupport = true;
                chrome.storage.local.get(['openSupportPanelCount'], function (data3) {
                    if (data3.openSupportPanelCount !== undefined) {
                        openSupportPanelCounter = data3.openSupportPanelCount;
                        chrome.storage.local.set({openSupportPanelCount: openSupportPanelCounter + 1}, function () {});
                    } else {
                        openSupportPanelCounter = 1;
                        chrome.storage.local.set({openSupportPanelCount: openSupportPanelCounter}, function () {});
                    }
                });
            }   
        } else {
            showPanelSupport = false;
            openSupportPanelCounter = 4;
        }
        
    } else {
        chrome.storage.local.set({supportDate: Date.now()}, function () {});
    }
});



chrome.runtime.onMessage.addListener(function listener(request, sender, sendResponse) {
    /*  Get Browser Name and Version*/
    const getBrowserNameAndVersion = () => {
        var ua = navigator.userAgent,
            tem,
            M = ua.match(/(vivaldi|opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*([0-9|\.]+)/i) || [];
        if (/trident/i.test(M[1])) {
            tem = /\brv[ :]+([0-9|\.]+)/g.exec(ua) || [];
            return 'IE ' + (tem[1] || '');
        }
        if (M[1] === 'Firefox') {
            tem = ua.match(/\b(PaleMoon)\/([0-9|\.]+)/);
            if (tem != null) return tem.slice(1).join(' ');
        }
        if (M[1] === 'Chrome') {
            tem = ua.match(/\b(OPR|Edge|Edg)\/([0-9|\.]+)/);
            if (tem != null) return tem.slice(1).join(' ').replace('OPR', 'Opera').replace('Edg', 'Edge');
        }
        M = M[2] ? [M[1], M[2]] : [navigator.appName, navigator.appVersion, '-?'];
        if ((tem = ua.match(/version\/([0-9|\.]+)/i)) != null) M.splice(1, 1, tem[1]);
        return M.join(' ');
    }

    var BrowserFamily = getBrowserNameAndVersion().split(" ")[0];

    if (request.url) {
        

        var frameContainer = document.querySelectorAll('#sts_frame_container').length;

        if (frameContainer < 1) {
            var frame = document.createElement('div');
            frame.setAttribute("id", "sts_frame_container");
            frame.style.cssText = "all: unset; position: fixed; top: 5px; right: 10px; width: auto; height: auto; background-color: transparent; z-index: 99999999; border-radius: 4px;";

            var close = document.createElement('div');
            close.setAttribute('id', 'x-close');
            close.appendChild(document.createTextNode("✖"));
            close.style.cssText = 'all: unset; position: absolute; top: 8px; right: 20px; width: auto; height: auto; background-color: transparent; z-index: 9999999; color: #666666; cursor: pointer; font-size: 12px; font-weight: bold; font-family: InterUI, sans-serif;';
            frame.appendChild(close);

            var iframe = document.createElement('iframe');
            iframe.setAttribute('frameborder', '0');
            iframe.setAttribute('id', 'tst_iframe');
            iframe.src = request.url;
            iframe.style.cssText = "width: 390px; max-width: 390px; height:680px;";
            frame.appendChild(iframe);

            close.addEventListener('click', function() {
                var parentDiv = document.querySelector("#sts_frame_container");
                var permissionPanelDiv = document.querySelector("#sts_permission_panel");
                if (parentDiv) {
                    parentDiv.parentNode.removeChild(parentDiv);
                    // chrome.storage.local.set({[(request.tabId).toString()]: {'openTab': false}}, function() {});
                }
                if (permissionPanelDiv) {
                    permissionPanelDiv.remove();
                }
                var panelDiv = document.querySelector("#sts_panel");
                if (panelDiv) {
                    panelDiv.parentNode.removeChild(panelDiv);
                }
                chrome.runtime.sendMessage({
                    what: 'ActionType',
                    name: 'CloseButton',
                    clicked: 'icon'
                });
            });

            /* Panel Survey */
            if (showPanel) {
                chrome.storage.local.get(['showPanelCount'], function (data) {
                    
                    if (data.showPanelCount == undefined || data.showPanelCount < 1) {
                        var panel = document.createElement("div");
                        panel.setAttribute("id", "sts_panel");
                        panel.style.cssText = "all: unset; position: fixed; top: 5px; right: 389px; width: auto; height: 634px; background-color: #fff; z-index: 99999996; border-radius: 1px; text-align: center; padding: 0; border: solid 1px #e6e6e6";
                        var p1 = document.createElement("div");
                        p1.setAttribute("id", "sts_panel_title");
                        p1.style.cssText = "all: unset; padding: 10px 0; font-size: 22px; display: block; margin: 70px 70px 20px;";
                        p1.appendChild(document.createTextNode("Make Web Pro Better!"));
                        var p2 = document.createElement("div");
                        p2.setAttribute("id", "sts_panel_sentence");
                        p2.style.cssText = "all: unset; padding: 10px 0; font-size: 16px; display: block;";
                        p2.appendChild(document.createTextNode("Take this short survey"));
                        var p3 = document.createElement("div");
                        p3.setAttribute("id", "sts_panel_sentence");
                        p3.style.cssText = "all: unset; padding: 10px 0; font-size: 16px; display: block;";
                        p3.appendChild(document.createTextNode("Chance to win $100 Amazon Gift card"));
                        var p4 = document.createElement("a");
                        p4.setAttribute("id", "sts_panel_sentence");
                        p4.style.cssText = "all: unset; font-size: 16px; display: block; cursor: pointer; color: #ffffff; width: 120px; height: auto; box-shadow: 0 1px 1px 0 rgba(0, 52, 87, 0.2); border: solid 1px #007fff; background: #0099ff; margin: 50px auto; padding: 10px 20px;";
                        p4.setAttribute("href", "https://www.surveymonkey.com/r/HKNWXTD");
                        p4.setAttribute("target", "_blank");
                        p4.appendChild(document.createTextNode("Start Survey"));
                        var panel_close = document.createElement('div');
                        panel_close.setAttribute('id', 'panel-close');
                        panel_close.appendChild(document.createTextNode("✖"));
                        panel_close.style.cssText = 'all: unset; position: absolute; top: 8px; right: 10px; width: auto; height: auto; background-color: transparent; z-index: 9999999; color: #666666; cursor: pointer; font-size: 12px; font-weight: bold; font-family: InterUI, sans-serif;';
                        panel.append(p1, p2, p3, p4, panel_close);

                        panel_close.addEventListener('click', function() {
                            var panelDiv = document.querySelector("#sts_panel");
                            if (panelDiv) {
                                panelDiv.parentNode.removeChild(panelDiv);
                            }
                        });
                        document.body.appendChild(panel);
                    }
                });
            }

            
            
            /* Support panel */
            if (showPanelSupport === true) {
                if (openSupportPanelCounter < 2) {
                    var supportPanel = document.createElement("div");
                    supportPanel.setAttribute("class", "prem-panel");
                    supportPanel.style.cssText = "all: unset; position: fixed; top: 16px; right: 389px; height: 614px; width: 351px; background-color: #fff; z-index: 99999996; border-radius: 1px; text-align: center; padding: 0; border: solid 1px #e6e6e6";


                    var supportPanelTop = document.createElement("div");
                    supportPanelTop.setAttribute("class", "pm-top-panel");
                    supportPanelTop.style.cssText = "height: 295px; background: 0 0 no-repeat url(" +  chrome.extension.getURL("img/popup/support-header-img.png") + "); width:100%;";


                    var supportPanelContent = document.createElement("div");
                    supportPanelContent.setAttribute("class", "pm-content-panel");
                    supportPanelContent.style.cssText = "padding: 35px 40px; box-sizing: border-box; font: 17px/1.47 Arial, sans-serif;";

                    var supportPanelContentH2 = document.createElement("H2");
                    supportPanelContentH2.style.cssText = "margin: 0 0 19px; font: bold 24px/1.100 Arial,sans-serif;";
                    // supportPanelContentH2.appendChild(document.createTextNode("Need Support?"));

                    var supportPanelContentP = document.createElement("P");
                    // supportPanelContentP.appendChild(document.createTextNode("Need help downloading torrents? For additional assistance, you can reach us : +44 2033 842368"));

                    var supportPanelContentBtn = document.createElement("a");
                    supportPanelContentBtn.setAttribute("id", "");
                    supportPanelContentBtn.setAttribute("class", "btn-blue");
                    supportPanelContentBtn.style.cssText = "display: block; background: #0099FF; color: #fff; border-radius: 2px; text-align: center; font: bold 16px/42px Arial; letter-spacing: -0.4px; color: #FFFFFF; text-shadow: 0px 1px 0px #00497980; opacity: 1; height: 42px; width: 220px; text-align: center; margin: 30px auto 0; text-decoration: none;";
                    supportPanelContentBtn.setAttribute("href", "https://www.torrentscanner.co/support/tech-premium-support/");
                    supportPanelContentBtn.setAttribute("target", "_blank");
                    // supportPanelContentBtn.appendChild(document.createTextNode("CALL NOW"));

                    var closeLink = document.createElement("a");
                    closeLink.setAttribute("id", "sts_support_link");
                    closeLink.setAttribute("href", "javascript:void(0);");
                    // closeLink.appendChild(document.createTextNode("No thanks"));
                    closeLink.style.cssText = "all: unset; display: block; font-size: 11px; line-height: 15px; font-family: Arial, sans-serif; margin: 0 auto; text-align: center; color: #000; text-decoration: underline; cursor: pointer;";

                    if (browserLanguage == "fr") {
                        supportPanelContentH2.appendChild(document.createTextNode("Besoin d’assistance ?"));
                        supportPanelContentP.appendChild(document.createTextNode("Besoin d'aide pour utiliser cette extension ? Pour obtenir de l’assistance, contactez-nous au : +33 5 82 84 04 07"));
                        supportPanelContentBtn.appendChild(document.createTextNode("Appelez maintenant"));
                        closeLink.appendChild(document.createTextNode("Non merci"));
                    } else if (browserLanguage == "es") {
                        supportPanelContentH2.appendChild(document.createTextNode("¿Necesita ayuda?"));
                        supportPanelContentP.appendChild(document.createTextNode("¿Necesitas ayuda para usar esta extensión? Para ayuda adicional, puede contactarnos: +34 951 203 077"));
                        supportPanelContentBtn.appendChild(document.createTextNode("Llame ahora"));
                        closeLink.appendChild(document.createTextNode("no, gracias"));
                    } else if (browserLanguage == "de") {
                        supportPanelContentH2.appendChild(document.createTextNode("Benötigen Sie Unterstützung?"));
                        supportPanelContentP.appendChild(document.createTextNode("Benötigen Sie Hilfe bei der Verwendung dieser Erweiterung? Für weitere Unterstützung erreichen Sie uns unter: +49 692 991 7686"));
                        supportPanelContentBtn.appendChild(document.createTextNode("Jetzt anrufen"));
                        closeLink.appendChild(document.createTextNode("Nein Danke"));
                    } else if (browserLanguage == "nl") {
                        supportPanelContentH2.appendChild(document.createTextNode("Hulp nodig?"));
                        supportPanelContentP.appendChild(document.createTextNode("Hulp nodig bij het gebruik van deze extensie? Als je verder nog hulp nodig hebt, kun je ons bereiken op: +31 85 888 1207"));
                        supportPanelContentBtn.appendChild(document.createTextNode("Nu bellen"));
                        closeLink.appendChild(document.createTextNode("Nee, dank u wel"));
                    } else {
                        supportPanelContentH2.appendChild(document.createTextNode("Need Support?"));
                        supportPanelContentP.appendChild(document.createTextNode("Need help using this extension? For additional assistance, you can reach us : +0203 384 2368"));
                        supportPanelContentBtn.appendChild(document.createTextNode("CALL NOW"));
                        closeLink.appendChild(document.createTextNode("No thanks"));
                    }

                    supportPanelContent.append(supportPanelContentH2, supportPanelContentP, supportPanelContentBtn);
                    supportPanel.append(supportPanelTop, supportPanelContent, closeLink);

                    document.body.appendChild(supportPanel);

                    // no thanks button clicked
                    document.querySelector('#sts_support_link').addEventListener('click', function () {
                        

                        if (supportPanel) {
                            supportPanel.remove();
                            chrome.storage.local.set({openSupportPanelCount: 5}, function () {});
                        }
                    });

                    chrome.runtime.sendMessage({
                        what: '_gaEvent',
                        category: 'Tech Premium',
                        action: 'Open',
                        label: 'tech-premium-panel-open'
                    }, (data) => {});
                }
                
            }
            /* End Support Panel */
            document.body.appendChild(frame);

            if (window.innerHeight < 660 && window.innerHeight > 540) {
                document.querySelector('#tst_iframe').style.height = "595px";
            }

            if (window.innerHeight < 540) {
                document.querySelector('#tst_iframe').style.height = "475px";
            }
        }
    } 

    // if (!request.openTab) {
    //     var frameContainer = document.querySelector('#sts_frame_container');
    //     if (frameContainer) {
    //         frameContainer.parentNode.removeChild(frameContainer);
    //         chrome.storage.local.set({[(request.tabId).toString()]: {'openTab': false}}, function() {});
    //     }
    // }
    chrome.runtime.onMessage.removeListener(listener);
});