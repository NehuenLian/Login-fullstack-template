import jwt_decode from 'jwt-decode';

export async function load({ cookies, fetch }) {
    const token = cookies.get('session');
    let needRefresh = true;

    if (token) {
        try {
            const decoded = jwt_decode(token);
            const now = Math.floor(Date.now() / 1000);
            if (decoded.exp - now > 120) {
                needRefresh = false;
            }
        } catch {
             needRefresh = true;
        }
    }

    if (needRefresh) {
        const res = await fetch('http://127.0.0.1:8000/api/auth/refresh', { 
            method: 'POST',
            headers: {
                cookie: cookies.get('session') ? `session=${cookies.get('session')}` : ''
            }
        });

        if (res.ok) {
            const data = await res.json();
            cookies.set('session', data.access_token, {
                httpOnly: true,
                path: '/',
                maxAge: 60*60
            });
        } else {
            cookies.delete('session', { path: '/' });
        }
    }

    return {};
}
