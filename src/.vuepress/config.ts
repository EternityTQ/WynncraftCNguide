import { defineUserConfig } from "vuepress";
import theme from "./theme.js";
import { defineClientConfig } from "vuepress/client";
import { defineSearchConfig } from "vuepress-plugin-search-pro/client";

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
        href: "https://fonts.googleapis.com/css2?family=Montserrat:wght@500&family=Noto+Sans+SC&display=swap",
        rel: "stylesheet",
      },
    ],
    
    ['link', { rel: 'Minecraft', href: '/assets/font/Minecraft.ttf' }],
  ],
  

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
