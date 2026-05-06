// @ts-check
import { test, expect } from '@playwright/test';

test.describe('Enjoy Institute Management System', () => {
  
  test.beforeEach(async ({ page }) => {
    // Go to the login page
    await page.goto('/auth/login');
  });

  test('Successful Admin Login', async ({ page }) => {
    // Fill credentials
    await page.fill('input[type="text"]', 'admin');
    await page.fill('input[type="password"]', 'password123'); // Adjust if different
    
    // Click Login
    await page.click('button:has-text("Sign In")');

    // Should redirect to dashboard
    await expect(page).toHaveURL(/.*dashboard/);
    await expect(page.locator('h1')).toContainText(/Good|Welcome/);
  });

  test('Navigation to Students and Pagination Check', async ({ page }) => {
    // Login first
    await page.fill('input[type="text"]', 'admin');
    await page.fill('input[type="password"]', 'password123');
    await page.click('button:has-text("Sign In")');
    await expect(page).toHaveURL(/.*dashboard/);

    // Go to Students page
    await page.click('a[href="/students"]');
    
    // Wait for the table to load
    await expect(page.locator('table')).toBeVisible();
    
    // Check if pagination controls are present
    const prevBtn = page.locator('button:has(svg.lucide-chevron-left)');
    const nextBtn = page.locator('button:has(svg.lucide-chevron-right)');
    
    await expect(prevBtn).toBeVisible();
    await expect(nextBtn).toBeVisible();
  });

  test('Fees Management Stats Check', async ({ page }) => {
    // Login
    await page.fill('input[type="text"]', 'admin');
    await page.fill('input[type="password"]', 'password123');
    await page.click('button:has-text("Sign In")');

    // Go to Fees page
    await page.click('a[href="/fees"]');
    
    // Check for Stat Cards
    await expect(page.locator('h2:has-text("₹")')).toHaveCount(3);
    await expect(page.locator('p:has-text("Total Expected")')).toBeVisible();
  });

  test('Responsive View Check', async ({ page }) => {
    // Set to mobile size
    await page.setViewportSize({ width: 375, height: 667 });
    
    await page.fill('input[type="text"]', 'admin');
    await page.fill('input[type="password"]', 'password123');
    await page.click('button:has-text("Sign In")');
    
    // Sidebar should be collapsed or hidden
    const sidebar = page.locator('aside');
    const width = await sidebar.evaluate((node) => node.getBoundingClientRect().width);
    expect(width).toBeLessThan(100);
  });

});
