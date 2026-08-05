/**
 * lib/geolocation.ts — Browser Geolocation API wrapper
 * No GPS SDK — uses native browser API per AGENTS.md §2.
 * No continuous/background tracking — one-shot capture per AGENTS.md §1.
 */

export interface GeoPosition {
  latitude: number;
  longitude: number;
  accuracy: number; // metres
}

/**
 * Capture current GPS position (one-shot, user-consent required).
 * Called only during attendance marking — never in background.
 */
export function capturePosition(): Promise<GeoPosition> {
  return new Promise((resolve, reject) => {
    if (!navigator.geolocation) {
      reject(new Error("Geolocation is not supported by this browser."));
      return;
    }

    navigator.geolocation.getCurrentPosition(
      (position) => {
        resolve({
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
          accuracy: position.coords.accuracy,
        });
      },
      (error) => {
        switch (error.code) {
          case error.PERMISSION_DENIED:
            reject(new Error("Location permission denied. Please allow location access to mark attendance."));
            break;
          case error.POSITION_UNAVAILABLE:
            reject(new Error("Location unavailable. Please try again."));
            break;
          case error.TIMEOUT:
            reject(new Error("Location request timed out. Please try again."));
            break;
          default:
            reject(new Error("Unable to get location."));
        }
      },
      {
        enableHighAccuracy: true,
        timeout: 10_000,
        maximumAge: 0, // Always fresh — never cache for attendance
      }
    );
  });
}
