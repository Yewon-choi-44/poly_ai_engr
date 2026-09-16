/**
 * router/index.ts
 *
 * Automatic routes for ./src/pages/*.vue
 */

// Composables
import { setupLayouts } from 'virtual:generated-layouts'
import { createRouter, createWebHistory } from 'vue-router'
import { routes } from 'vue-router/auto-routes'
import LoginAccount from '@/pages/LoginAccount.vue'
import RegisterAccount from '@/pages/RegisterAccount.vue'


routes.push(...[
  {path: '/login', component: LoginAccount },
  {path: '/signup', component: RegisterAccount}
])
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: setupLayouts(routes),
})

export default router
