import { fail, redirect } from "@sveltejs/kit";

async function handleRegister({request}) {
    const formData = await request.formData();
    const email = formData.get('email');
    const password = formData.get('password');
    const confirmPassword = formData.get('confirmPassword');

    if (!email || !password || !confirmPassword) {
        return fail(400, { error: "Please fill email, password and confirmation password." });
    }

    if (password !== confirmPassword) {
        return fail(400, {error: "Password and Confirmation password aren't identic."})
    }

    const backendResponse = await fetch('http://127.0.0.1:8000/api/auth/register', {
        method: 'POST',
        headers: {'Content-Type' : 'application/json'},
        body: JSON.stringify( {email, password })
    });
    const responseData = await backendResponse.json();

    if (backendResponse.status === 409) {
        return fail(409, {error: "This email is already in use."})
    }

    if (!backendResponse.ok) {
        return fail(500, { error: "Unexpected error occurred." });
    }

    throw redirect(303, '/login');
}

export const actions = {
    default: handleRegister
};