import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
// path alias config
import path, { dirname } from "node:path";
import { fileURLToPath } from "node:url";

function getDirname(importMetaUrl: string): string {
  return dirname(fileURLToPath(importMetaUrl));
}

const __dirname = getDirname(import.meta.url);

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  // global scss variables
  css: {
    preprocessorOptions: {
      scss: {
        // additionalData: `@import "/src/styles/variables.scss";`, // deprecated warning
        // Instead, use modern @use syntax in your SCSS files
        api: "modern-compiler", // Use modern Sass API
      },
    },
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
      "@components": path.resolve(__dirname, "./src/components"),
      "@pages": path.resolve(__dirname, "./src/pages"),
      "@utils": path.resolve(__dirname, "./src/utils"),
      "@hooks": path.resolve(__dirname, "./src/hooks"),
      "@types": path.resolve(__dirname, "./src/types"),
      "@assets": path.resolve(__dirname, "./src/assets"),
      "@styles": path.resolve(__dirname, "./src/styles"),
      "@api": path.resolve(__dirname, "./src/api"),
      "@store": path.resolve(__dirname, "./src/store"),
    },
  },
});
