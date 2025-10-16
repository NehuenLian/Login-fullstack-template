import { fail, redirect } from "@sveltejs/kit";

async function handleLogin({request, cookies}) {
    const formData = await request.formData();
    const email = formData.get('email');
    const password = formData.get('password');

    if (!email || !password) {
        return fail(400, { error: "Please fill in both email and password." });
    }

    if (!validateEmail(email)) {
        return fail(400, { error: "Please enter a valid email." })
    }

    const backendResponse = await fetch('http://127.0.0.1:8000/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type' : 'application/json' },
        body: JSON.stringify( {email, password} )
    });
    const responseData = await backendResponse.json();

    if (backendResponse.status == 401 || backendResponse.status == 404) {
        return fail(401, {error: "Email or password are incorrect."})
    }

    if (!backendResponse.ok) {
        return fail(500, { error: "Unexpected error occurred." });
    }

    const access_token = responseData.access_token;
    cookies.set('session', access_token, {
        httpOnly: true,
        path: '/',
        maxAge: 60 * 10,
    });
    
    throw redirect(303, '/dashboard')
}

export const actions = {
    default: handleLogin
};

function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}