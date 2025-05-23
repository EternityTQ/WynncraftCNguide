import { defineUserConfig } from "vuepress";

import { registerComponentsPlugin } from '@vuepress/plugin-register-components'
import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "Wynncraft中文攻略",
  description: "Wynncraft中文攻略",
  
  theme,

  head: [
    // ...

    // 导入相应链接
    ["link", { rel: "preconnect", href: "https://fonts.googleapis.com" }],
    [
      "link",
      { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "" },
    ],
    [
      "link",
      {
        href: "https://fonts.googleapis.com/css2?family=Montserrat:wght@400&family=Noto+Sans+SC&display=swap",
        rel: "stylesheet",
      },
    ],
    [
      "link",
      {
        href: "https://fonts.googleapis.com/css2?family=Peralta&display=swap",
        rel: "stylesheet",
      },
    ],
    [
      "link",
      {
        href: "https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap",
        rel: "stylesheet",
      },
    ],
  ],

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
