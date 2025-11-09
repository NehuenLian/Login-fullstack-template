function getStoredToken() {
    if (typeof window === 'undefined') return null;

    return sessionStorage.getItem('access_token');
}

function setStoredToken(token) {
    if (typeof window === 'undefined') return;
    sessionStorage.setItem('access_token', token);
}

export async function fetchWithApi(url, options = {}) {
    const token = getStoredToken(); // get sessionStorage token

    let res = await fetch(url, { ...options, credentials: 'include', 
        headers: {
            ...options.headers,
            ...(token ? { 'Authorization': 'Bearer ' + token } : {})
        }
    });

    if (res.status === 401) {
        const errorData = await res.json();
        const errorMessages = ["Missing refresh token", 
                                "Invalid token type", 
                                "Refresh token expired", 
                                "Invalid token"];
        
        if (errorMessages.includes(errorData.detail)) {

            const refreshRes = await fetch('http://localhost:8000/api/auth/refresh', 
            { method: 'POST', credentials: 'include'});

            if (refreshRes.ok) {
                const data = await refreshRes.json();
                const newAccessToken = data.access_token;
                setStoredToken(newAccessToken);
                
                res = await fetch(url, { ...options,  credentials: 'include',
                    headers: {
                        ...options.headers,
                        'Authorization': 'Bearer ' + newAccessToken
                    }
                });
            } 
            else {
                window.location.href = '/login';
                return;
            }
        } 
    }
    return res;
}