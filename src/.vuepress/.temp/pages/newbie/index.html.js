export const data = JSON.parse("{\"key\":\"v-4ff12110\",\"path\":\"/newbie/\",\"title\":\"新手指南\",\"lang\":\"zh-CN\",\"frontmatter\":{\"title\":\"新手指南\",\"icon\":\"route\",\"description\":\"\"},\"headers\":[],\"readingTime\":{\"minutes\":0.02,\"words\":7},\"filePathRelative\":\"newbie/README.md\",\"autoDesc\":true}")

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept()
  if (__VUE_HMR_RUNTIME__.updatePageData) {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  }
}

if (import.meta.hot) {
  import.meta.hot.accept(({ data }) => {
    __VUE_HMR_RUNTIME__.updatePageData(data)
  })
}
