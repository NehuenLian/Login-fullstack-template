import { fail, redirect } from "@sveltejs/kit";

async function handleLogin({request, cookies}) {
    const formData = await request.formData();
    const username = formData.get('username');
    const password = formData.get('password');

    if (!username || !password) {
        return fail(400, { error: "Please fill in both username and password." });
    }

    const backendResponse = await fetch('http://127.0.0.1:8000/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify( {username, password} )
    });
    const responseData = await backendResponse.json();

    if (backendResponse.status == 401 || backendResponse.status == 404) {
        return fail(401, {error: "Username or password are incorrect."})
    }

    if (!backendResponse.ok) {
        return fail(500, { error: "Unexpected error occurred." });
    }

    const access_token = responseData.access_token;
    cookies.set('session', access_token, {
        httpOnly: true,
        path: '/',
        maxAge: 60 * 60 * 24,
    });
    
    throw redirect(303, '/dashboard')
}

export const actions = {
    default: handleLogin
};