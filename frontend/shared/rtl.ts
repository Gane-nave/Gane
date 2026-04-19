export const RTL_LANGUAGES = ["he", "ar"] as const;

export function isRtlLanguage(languageCode: string): boolean {
  const normalized = languageCode.toLowerCase().split("-")[0];
  return RTL_LANGUAGES.includes(normalized as (typeof RTL_LANGUAGES)[number]);
}

export function computeDirection(languageCode: string): "rtl" | "ltr" {
  return isRtlLanguage(languageCode) ? "rtl" : "ltr";
}
