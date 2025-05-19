/// <reference types="@vitest/browser/providers/playwright" />

import { cleanup } from "@testing-library/react";
import { afterEach } from "vitest";
import { cleanup as browserCleanup } from "vitest-browser-react";

afterEach(() => {
  cleanup();
  browserCleanup();
});
