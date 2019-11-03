webpackJsonp([4], {
    0: function(t, e, n) {
        n(21),
        t.exports = n(639)
    },
    639: function(t, e, n) {
        function i(t) {
            return t && t.__esModule ? t : {
                default: t
            }
        }
        function a(t) {
            return function() {
                var e = t.apply(this, arguments);
                return new Promise(function(t, n) {
                    function i(a, s) {
                        try {
                            var o = e[a](s)
                              , r = o.value
                        } catch (t) {
                            return void n(t)
                        }
                        return o.done ? void t(r) : Promise.resolve(r).then(function(t) {
                            i("next", t)
                        }, function(t) {
                            i("throw", t)
                        })
                    }
                    return i("next")
                }
                )
            }
        }
        function s(t) {
            if (Array.isArray(t)) {
                for (var e = 0, n = Array(t.length); e < t.length; e++)
                    n[e] = t[e];
                return n
            }
            return Array.from(t)
        }
        var o, r, d = function() {
            function t(t, e) {
                var n = []
                  , i = !0
                  , a = !1
                  , s = void 0;
                try {
                    for (var o, r = t[Symbol.iterator](); !(i = (o = r.next()).done) && (n.push(o.value),
                    !e || n.length !== e); i = !0)
                        ;
                } catch (t) {
                    a = !0,
                    s = t
                } finally {
                    try {
                        !i && r.return && r.return()
                    } finally {
                        if (a)
                            throw s
                    }
                }
                return n
            }
            return function(e, n) {
                if (Array.isArray(e))
                    return e;
                if (Symbol.iterator in Object(e))
                    return t(e, n);
                throw new TypeError("Invalid attempt to destructure non-iterable instance")
            }
        }();
        n(348);
        var h = n(349);
        i(h);
        o = [n(353), n(356), n(350), n(357), n(361), n(414), n(431), n(362), n(448), n(442), n(449), n(450), n(453), n(632), n(454), n(459), n(466), n(455), n(467), n(468), n(475), n(507), n(543), n(602), n(620), n(622), n(624), n(626), n(627), n(628)],
        r = function(t, e, n, i, o, r, h, u, c, v, l, g, f, p, b, m, w, y, C, S, x, T, I, M, V, R, z, A, D, P) {
            var _ = i.Router.extend({
                initialize: function() {
                    this.createRoutes([[":unique_name(/)", "tabPage"], [":unique_name#", "tabPage"], [":unique_name/home", "tabPage"], [":unique_name/agenda/session/:session", "session"], [":unique_name/agenda/:day", "agenda"], [":unique_name/page/:id(/*path)", "tabPage"], ["*missedRoute", "missedRoute"]]);
                    var e = {
                        event: u("bootstrap-data-event"),
                        me: u("bootstrap-data-me"),
                        config: u("bootstrap-data-config"),
                        siteSections: u("bootstrap-data-siteSections"),
                        siteConf: u("bootstrap-data-siteConf"),
                        sponsors: u("bootstrap-data-sponsors"),
                        attendees: u("bootstrap-data-attendees"),
                        eventCustomization: u("bootstrap-data-eventCustomization"),
                        isWidget: u("bootstrap-data-isWidgetObject").isWidget
                    };
                    this.enableFeatureToggle(e.event && e.event["account-id"]),
                    e.eventID = e.event.id,
                    this.isWidget = e.isWidget,
                    this.bodyView = new S({
                        el: t(document.body),
                        bootstrapData: e,
                        triggerGoogleAnalytics: !1
                    }),
                    this.siteConf = this.bodyView.siteConf,
                    this.loadTemplates(),
                    this.me = v.get("me"),
                    this.event = v.get("event"),
                    this.eventCustomization = new C(n.isEmpty(e.eventCustomization) ? {
                        id: this.event.get("id")
                    } : e.eventCustomization),
                    this.agenda = new p({
                        eventId: this.event.get("id"),
                        startDate: this.event.get("local-start-date"),
                        viewState: this.eventCustomization.get("agenda-view-type")
                    }),
                    this.tabSections = new y,
                    this.tabSections.eventId = this.event.get("id"),
                    this.tabSections.set(n.isEmpty(e.siteSections) ? {} : e.siteSections, {
                        parse: !0
                    }),
                    v.set("agenda", this.agenda),
                    v.set("canGoBack", !1);
                    var a = this;
                    this.on("route", function(t, e) {
                        i.trigger("analytics:routeChanged"),
                        a.bodyView.sendUrlToWhiteLabelDomain()
                    })
                },
                createRoutes: function(t) {
                    var e = this
                      , i = u("bootstrap-data-event")
                      , a = "whitelabel" === i.websiteType
                      , o = [].concat(s(t));
                    o.reverse(),
                    n(o).each(function(t) {
                        var n = d(t, 2)
                          , i = n[0]
                          , s = n[1];
                        return a ? void (i.startsWith(":unique_name") ? e.route(i.replace(/^:unique_name(\/?)/, ""), s, e[s].bind(e, null)) : e.route(i, s, e[s].bind(e))) : void e.route(i, s, e[s].bind(e))
                    })
                },
                executedRoutesCount: 0,
                execute: function(t, e) {
                    this.scrollParentIFrameToTop(),
                    v.set("canGoBack", this.executedRoutesCount > 0),
                    this.executedRoutesCount++,
                    t && t.apply(this, e)
                },
                scrollParentIFrameToTop: function() {
                    this.executedRoutesCount > 0 && window.parentIFrame && window.parentIFrame.sendMessage("scrollToTop", "*")
                },
                tabPage: function(t, e) {
                    e = parseInt(e, 10);
                    var i = this.siteConf.get("tabs").findWhere({
                        id: e
                    });
                    this.siteConf.set("currentTab", e || "home");
                    var a = this.getSections(e || this.siteConf.getTabIdByType("home"))
                      , s = n.bind(function() {
                        var t = new I({
                            model: this.tabSections,
                            siteConf: this.siteConf,
                            isMobile: this.isMobile(),
                            tabSection: i ? i.toJSON() : null
                        });
                        this.bodyView.setMainView(t),
                        t.render()
                    }, this)
                      , o = function() {};
                    c.fetch(a, s, o),
                    this.showLoader()
                },
                agenda: function() {
                    function t(t, n) {
                        return e.apply(this, arguments)
                    }
                    var e = a(regeneratorRuntime.mark(function t(e, a) {
                        var s, o, r;
                        return regeneratorRuntime.wrap(function(t) {
                            for (; ; )
                                switch (t.prev = t.next) {
                                case 0:
                                    this.siteConf.set("currentTab", "agenda"),
                                    s = this.getAgendaModels(),
                                    o = n.bind(function() {
                                        !a && this.agenda.set("viewState", this.eventCustomization.get("agenda-view-type"));
                                        var t = new P(this.event.get("time-zone-id"));
                                        a = t.getDayIndex(a, this.event.get("start-date"), this.event.get("end-date"), this.eventCustomization.get("agendaDefaultDay"));
                                        var e = this.agenda.getDay(this.event.get("start-date"), a)
                                          , n = new M({
                                            model: new i.Model({
                                                agenda: this.agenda,
                                                currentDay: e,
                                                daysCount: this.agenda.get("day").length - 1
                                            })
                                        });
                                        this.bodyView.setMainView(n),
                                        n.render()
                                    }, this),
                                    r = function() {}
                                    ,
                                    c.fetch(s, o, r),
                                    !a && this.showLoader();
                                case 6:
                                case "end":
                                    return t.stop()
                                }
                        }, t, this)
                    }));
                    return t
                }(),
                session: function(t, e) {
                    this.siteConf.set("currentTab", "agenda");
                    var i = this.getAgendaModels();
                    this.polls = this.polls || new m({
                        eventId: this.event.get("id")
                    }),
                    this.partners = this.partners || new w({
                        eventId: this.event.get("id")
                    });
                    var a = !("private" === this.event.get("privacy") || "private-community" === this.event.get("privacy"));
                    (a || this.event.isJoined()) && !this.polls.fetched && i.push(this.polls),
                    !this.partners.fetched && i.push(this.partners);
                    var s = n.bind(function() {
                        this.polls.setPartners(this.partners);
                        var t = this.agenda.getSession(e);
                        t.setPolls(this.polls);
                        var n = new V({
                            model: t,
                            event: v.get("event")
                        });
                        this.bodyView.setMainView(n),
                        n.render()
                    }, this)
                      , o = function() {};
                    c.fetch(i, s, o),
                    this.showLoader()
                },
                speaker: function(t, e) {
                    this.siteConf.set("currentTab", "agenda");
                    var i = this.getAgendaModels()
                      , a = n.bind(function() {
                        e = parseInt(e, 10);
                        var t = this.agenda.get("speaker").get(e)
                          , n = new R({
                            model: t,
                            event: this.event
                        });
                        this.bodyView.setMainView(n),
                        n.render()
                    }, this)
                      , s = function() {};
                    c.fetch(i, a, s),
                    this.showLoader()
                },
                missedRoute: function(t) {
                    this.isWidget && (t = this.appendQueryString(t, {
                        widget: !0
                    })),
                    window.location = "/" + t
                },
                loadTemplates: function() {
                    var e = {}
                      , i = this.bodyView.$('[data-type="template"]');
                    i.each(function() {
                        var i = t(this)
                          , a = i.attr("data-name")
                          , s = r.compile(n.unescape(i.html()));
                        e[a] = s
                    }),
                    r.sectionsTemplates = e
                },
                getAgendaModels: function() {
                    var t = [];
                    return this.event.isJoinRequired() || (!this.agenda.get("fetched") && t.push(this.agenda),
                    !this.eventCustomization.get("fetched") && t.push(this.eventCustomization)),
                    t
                },
                getSections: function(t) {
                    var e = [];
                    if (!this.event.isJoinRequired()) {
                        var n = this.tabSections.at(0) && this.tabSections.at(0).get("tabId");
                        n != t && (this.tabSections.tabId = t,
                        this.tabSections.fetched = !1),
                        !this.tabSections.fetched && e.push(this.tabSections)
                    }
                    return e
                },
                loadUrl: function(t) {
                    i.history.loadUrl(t),
                    this.autoDetectLinks()
                },
                showLoader: function() {
                    this.bodyView && this.bodyView.removeMainView();
                    var e = t(".main-view");
                    e.hasClass("no-loader") ? e.removeClass("no-loader") : e.html(A({}))
                },
                appendQueryString: function(t, e) {
                    var i = t.indexOf("?") == -1 ? "?" : "&"
                      , a = n.map(e, function(t, e) {
                        return e + "=" + t
                    })
                      , s = a.join("&");
                    return t + i + s
                },
                autoDetectLinks: function() {
                    var e = this;
                    t(document).delegate("a", "click", function(n) {
                        var a = t(this).attr("href")
                          , s = t(this).attr("target");
                        if (a && "_blank" != s) {
                            var o = 0 === a.indexOf("javascript")
                              , r = 0 === a.indexOf("http:") || 0 === a.indexOf("https:")
                              , d = r || 0 === a.indexOf("data:") || 0 === a.indexOf("mailto:") || 0 === a.indexOf("tel:");
                            return d ? void (e.event.get("whitelabel-web") && window !== window.top && (window.top.location.href = a)) : (n.preventDefault(),
                            void (o || i.history.navigate(a, !0)))
                        }
                    })
                },
                isMobile: function t() {
                    var e = new z(navigator.userAgent)
                      , t = !!e.mobile();
                    return v.set("isMobile", t),
                    t
                }
            });
            n.extend(_.prototype, D);
            var k = new _({});
            i.history.start({
                silent: !0,
                pushState: history.pushState
            });
            var q, O = window.location.hash.replace("#", "/").split("?")[0];
            return q = O && O.length > 1 ? O : window.location.pathname,
            q = q.replace(/\/$/, ""),
            k.loadUrl(q),
            _
        }
        .apply(e, o),
        !(void 0 !== r && (t.exports = r))
    }
});
//# sourceMappingURL=AppRouterInMigrationToReact.js.map
