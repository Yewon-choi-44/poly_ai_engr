import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
    const sessionid = ref(sessionStorage.getItem('sessionid') || null)
    const login = (id) => {
        console.log('login', id)
        sessionid.value = id
        sessionStorage.setItem('sessionid', id)
    }

    const logout = () => {
        sessionid.value = null
        sessionStorage.removeItem('sessionid')
    }

    return {
        sessionid,
        isAuthenticated,
        login,
        logout
    }
})