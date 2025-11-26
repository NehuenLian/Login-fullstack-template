import { redirect } from "@sveltejs/kit";

async function handleLogout({ cookies }) {

    const token = cookies.get('refresh_token');
    if (!token) {
        throw redirect(303, '/login');
    }
    cookies.delete('refresh_token', { path: '/' });

    return { success: true };
}

export const actions = {
    default: handleLogout
}