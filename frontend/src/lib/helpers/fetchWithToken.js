
export async function fetchWithApi(url, options = {}) {
    let res = await fetch(url, { ...options, credentials: 'include', });

    if (res.status === 401) {
        const errorData = await res.json();
        const errorMessages = ["Missing refresh token", 
                                "Invalid token type", 
                                "Refresh token expired", 
                                "Invalid token"];
        
        if (errorMessages.includes(errorData.detail)) {

            const refreshRes = await fetch('http://127.0.0.1:8000/api/auth/refresh', 
            { method: 'POST', credentials: 'include'});

            if (refreshRes.ok) {
                res = await fetch(url, { ...options,  credentials: 'include' });
            } 
            else {
                throw new Error('Session expired');
            }
        } 

    }
    return res;
}