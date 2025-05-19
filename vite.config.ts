/// <reference types="vitest/config" />
import react from "@vitejs/plugin-react";
import type { UserConfig } from "vite";

export default {
  root: "./frontend",
  plugins: [react()],
  test: {
    environment: "happy-dom",
  },
} satisfies UserConfig;
