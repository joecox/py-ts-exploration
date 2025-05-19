import { render } from "@testing-library/react";
import { expect, test } from "vitest";
import { Button } from "./button";

import { render as browserRender } from "vitest-browser-react";

test("render button", () => {
  const { getByRole } = render(<Button>Foobar</Button>);
  expect(getByRole("button")).toBeTruthy();
});

test("render button - browser", async () => {
  const screen = browserRender(<Button>Foobar</Button>);
  await expect.element(screen.getByRole("button")).toBeInTheDocument();
});
