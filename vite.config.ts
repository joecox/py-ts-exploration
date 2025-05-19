/// <reference types="vitest/config" />
import react from "@vitejs/plugin-react";
import type { UserConfig } from "vite";

export default {
  root: "./frontend",
  plugins: [react()],
  test: {
    environment: "happy-dom",
    browser: {
      provider: "playwright",
      enabled: true,
      headless: true,
      instances: [{ browser: "chromium" }],
    },
    setupFiles: ["./test-utils/setup.ts"],
  },
} satisfies UserConfig;
