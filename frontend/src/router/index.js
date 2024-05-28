import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
history: createWebHistory(),
routes: [
    {
        path: '/',
        name: 'app',
        component: () => import('@/App.vue')
    },]
});

export default router
export const routes = router.options.routes;