import { fail, redirect } from "@sveltejs/kit";

async function handleLogin({request, cookies}) {
    const formData = await request.formData();
    const username = formData.get('username');
    const password = formData.get('password');

    if (!username || !password) {
        return fail(400, { error: "Please fill in both username and password." });
    }

    const backendResponse = await fetch('', {
        method: 'POST',
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify( {username, password} )
    });
    const responseData = await backendResponse.json();

    if (!backendResponse.ok) {
        return fail(backendResponse.statusText, { error: responseData.detail });
    }

    const access_token = responseData.access_token;
    cookies.set('session', access_token, {
        httpOnly: true,
        path: '/',
        maxAge: 60 * 60 * 24,
    });

    throw redirect(303, '/')
}

export const actions = {
    default: handleLogin
};