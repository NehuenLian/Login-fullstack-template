import { PUBLIC_API_URL } from '$env/static/public';
import { validateAndRefreshToken } from './tokenValidator.js';

const API_URL = PUBLIC_API_URL;

function getStoredAccessToken() {
    if (typeof window === 'undefined') return null;
    let token = sessionStorage.getItem('access_token');

    return token;
}

function setStoredToken(token) {
    if (typeof window === 'undefined') return;
    sessionStorage.setItem('access_token', token);
}

export async function fetchWithApi(url, options = {}) {

    const tokenIsValid = await validateAndRefreshToken(); // verifies access token expiration

    if (!tokenIsValid) {
        window.location.href = '/logout';
        return;
    }
    const token = getStoredAccessToken();

    let res = await fetch(url, { ...options,
        credentials: 'include',
    })

    if (res.status === 401) {
        window.location.href = '/logout';
        return;
    }
    return res;
}
