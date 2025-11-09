import { redirect } from '@sveltejs/kit';

export async function handle({ event, resolve }) {
    const sessionCookie = event.cookies.get('refresh_token');
    const protectedRoutes = ['/dashboard'];
    const currentPathName = event.url.pathname;

    const isProtected = protectedRoutes.some(path => currentPathName.startsWith(path));
    
    if (isProtected && !sessionCookie) {
        throw redirect(303, '/login');
    }

    return await resolve(event);
}
