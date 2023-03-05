WebFont.load({
    google: {
      families: [
        "Montserrat:100,100italic,200,200italic,300,300italic,400,400italic,500,500italic,600,600italic,700,700italic,800,800italic,900,900italic",
        "DM Sans:regular,italic,500,500italic,700,700italic:latin,latin-ext",
      ],
    },
  });

  !(function (o, c) {
    var n = c.documentElement,
      t = " w-mod-";
    (n.className += t + "js"),
      ("ontouchstart" in o ||
        (o.DocumentTouch && c instanceof DocumentTouch)) &&
        (n.className += t + "touch");
  })(window, document);

  window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", "G-REZ8MWBW1B", { anonymize_ip: false });
      !(function (f, b, e, v, n, t, s) {
        if (f.fbq) return;
        n = f.fbq = function () {
          n.callMethod
            ? n.callMethod.apply(n, arguments)
            : n.queue.push(arguments);
        };
        if (!f._fbq) f._fbq = n;
        n.push = n;
        n.loaded = !0;
        n.version = "2.0";
        n.agent = "plwebflow";
        n.queue = [];
        t = b.createElement(e);
        t.async = !0;
        t.src = v;
        s = b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t, s);
      })(
        window,
        document,
        "script",
        "https://connect.facebook.net/en_US/fbevents.js"
      );
      fbq("init", "474056224626923");
      fbq("track", "PageView");