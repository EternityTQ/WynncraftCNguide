import { defineUserConfig } from "vuepress";
import theme from "./theme.js";
import { searchProPlugin } from "vuepress-plugin-search-pro";

export default defineUserConfig({
  base: "/WynncraftCNguide/",

  lang: "zh-CN",
  title: "Wynncraft中文攻略",
  description: "Wynncraft中文攻略",

  extendsMarkdown: (md) => {
    md.use(plugin1)
    md.linkify.set({ fuzzyEmail: false })
  },
  
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
  ],
  plugins: [
    searchProPlugin({
      // 索引全部内容
      indexContent: true,
      autoSuggestions: false,
      // 为分类和标签添加索引
      customFields: [
        {
          getter: (page) => page.frontmatter.category,
          formatter: "分类：$content",
        },
        {
          getter: (page) => page.frontmatter.tag,
          formatter: "标签：$content",
        },
      ],
    }),
  ],
  // Enable it with pwa
  // shouldPrefetch: false,
});
