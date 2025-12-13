import jwtDecode from "jwt-decode"; // Default import
import { PUBLIC_API_URL } from '$env/static/public';

const API_URL = PUBLIC_API_URL;

function getStoredAccessToken() {
    if (typeof window === 'undefined') return null;
    return sessionStorage.getItem('access_token');
}

function setStoredAccessToken(token) {
    if (typeof window === 'undefined') return;
    sessionStorage.setItem('access_token', token);
}

function clearStoredToken() {
    if (typeof window === 'undefined') return;
    sessionStorage.removeItem('access_token');
}


async function refresh() { // -> bool

    const response = await fetch(`${API_URL}/api/auth/refresh`, {
        method: 'POST',
        credentials : 'include'
    });

    if (response.status === 401) {
        clearStoredToken();
        window.location.href = '/logout';
        return;
    }

    if (!response.ok) {
        clearStoredToken();
        return false;
    }

    const data = await response.json();
    sessionStorage.setItem('access_token', data.access_token);

    return true;
}

export async function validateAndRefreshToken() { // -> bool

    const accessToken = getStoredAccessToken();

    if (accessToken) {
        try {
            const decoded = jwtDecode(accessToken);
            const now = Date.now() / 1000;

            if (decoded.exp > now + 60) {
                return true;
            }
            else {
                return await refresh();
            }
        }
        catch {
            return await refresh();
        }
    }
    
    if (!accessToken) {
        return await refresh();
    }
}
