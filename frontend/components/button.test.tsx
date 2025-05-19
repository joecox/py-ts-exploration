import { render } from "@testing-library/react";
import { expect, test } from "vitest";
import { Button } from "./button";

test("render button", () => {
  const { getByRole } = render(<Button>Foobar</Button>);
  expect(getByRole("button")).toBeTruthy();
});
