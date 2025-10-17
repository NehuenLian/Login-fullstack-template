import { describe, it, expect } from "vitest";
import { validateEmail, validatePasswordLenght, validatePasswordCase, validatePasswordSymbols, 
  validateConfirmPassword } from '$lib/utils/validations.js';

describe('Email validation', () => {
    it('must return true for an empty email', () => {
        expect(validateEmail('user@domain.com')).toBe(true);
    });

    it('must return false for an emmil with no @', () => {
        expect(validateEmail('userdomain.com')).toBe(false);
    } );
})

describe('Password validation', () => {
    it('must validate max lenght (>= 8)', () => {
        expect(validatePasswordLenght('short7')).toBe(false); // chars
        expect(validatePasswordLenght('longpassword8')).toBe(true) // 13 chars
    });

    it('must require upper and lower', () => {
        expect(validatePasswordCase('onlylowercase')).toBe(false);
        expect(validatePasswordCase('ONLYUPPERCASE')).toBe(false);
        expect(validatePasswordCase('CorrectPassword')).toBe(true);
    });
    it('must require one symbol', () => {
        expect(validatePasswordSymbols('Nosymbolpass')).toBe(false);
        expect(validatePasswordSymbols('Symbolpass%$#')).toBe(true);
    });
})

describe('Confirm Password Validation', () => {
    it('must return true if passwords are identic', () => {
        expect(validateConfirmPassword('pass123', 'pass123')).toBe(true);
    });

    it('must be false if passwords are not identic', () => {
        expect(validateConfirmPassword('pass123', 'pass456')).toBe(false);
    })
})