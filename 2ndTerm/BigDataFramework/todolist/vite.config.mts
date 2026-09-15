import VueRouter from 'vue-router/vite';
import { fileURLToPath, URL } from 'node:url'
import Vue from '@vitejs/plugin-vue'
import Fonts from 'unplugin-fonts/vite'
import { defineConfig } from 'vite'
import Vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
import Layouts from 'vite-plugin-vue-layouts-next'
import Components from 'unplugin-vue-components/vite';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [VueRouter({ dts: 'src/typed-router.d.ts' }), Vue({
    template: { transformAssetUrls },
  }), // https://github.com/vuetifyjs/vuetify-loader/tree/master/packages/vite-plugin#readme
  Vuetify({
    autoImport: true,
    styles: {
      configFile: 'src/styles/settings.scss',
    },
  }), 

  Layouts(),
  Components({ dts: 'src/components.d.ts' }),
  
  Fonts({
    fontsource: {
      families: [
        {
          name: 'Roboto',
          weights: [100, 300, 400, 500, 700, 900],
          styles: ['normal', 'italic'],
        },
      ],
    },
  })],
  define: { 'process.env': {} },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('src', import.meta.url)),
    },
    extensions: [
      '.js',
      '.json',
      '.jsx',
      '.mjs',
      '.ts',
      '.tsx',
      '.vue',
    ],
  },
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://syntaxwiki.com:9993',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/,'')
      }
    }
  },
})