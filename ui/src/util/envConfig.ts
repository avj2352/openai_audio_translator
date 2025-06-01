/**
 * reads env config and returns them
 */

export const APP_VERSION = import.meta.env.VITE_APP_NAME || "0.1.1";
export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";
