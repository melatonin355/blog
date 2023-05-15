# A Quick Guide to TypeScript

TypeScript is a statically typed superset of JavaScript that compiles to plain JavaScript. It was developed by Microsoft to add additional features to the language, including strong typing, which can help catch bugs and make your code more maintainable.

## Setting Up TypeScript

You can install TypeScript globally on your machine using npm (Node Package Manager).

```bash
npm install -g typescript
```

To compile a TypeScript file (a `.ts` file), you can use the `tsc` command followed by the filename.

```bash
tsc filename.ts
```


## Basic Syntax and Types

### Variable and Function Declaration

TypeScript uses the `let` and `const` keywords for variable declaration, just like modern JavaScript.

```typescript
let name: string = 'John Doe';
const age: number = 30;
```

Functions can have their parameters and return values typed.

```typescript
function greet(name: string): string {
  return `Hello, ${name}!`;
}
```

### Interfaces

Interfaces define a contract for classes and ensure a certain structure for objects.

```typescript
interface Person {
  name: string;
  age: number;
}

let john: Person = { name: 'John', age: 30 };
```

### Classes

TypeScript supports modern JavaScript classes including constructors, properties, and methods. It also adds visibility modifiers (`public`, `private`, `protected`).

```typescript
class Person {
  constructor(public name: string, private age: number) {}

  public greet() {
    return `Hello, ${this.name}!`;
  }
}
```

### Enums

Enums allow us to define a set of named constants.

```typescript
enum Color {
  Red,
  Green,
  Blue
}

let c: Color = Color.Green;
```

## Type Inference

TypeScript is smart enough to infer types in many cases. If you set a variable to a number, TypeScript will infer that you want that variable to always be a number.

```typescript
let x = 10; // TypeScript infers that this should be a number
x = 'hello'; // This will raise a compile error
```

## Type Assertion

Sometimes you know more about a value than TypeScript does. You can use type assertion to tell TypeScript "trust me, I know what I'm doing."

```typescript
let someValue: any = "this is a string";

let strLength: number = (<string>someValue).length;
```

## Generics

Generics allow you to write reusable components that can work over a variety of types rather than a single one.

```typescript
function identity<T>(arg: T): T {
  return arg;
}

let output = identity<string>("myString");
```

## Modules

TypeScript can use ES6 style import/export syntax to include or exclude modules.

```typescript
// lib.ts
export function sayHello(name: string) {
  return `Hello, ${name}!`;
}

// main.ts
import { sayHello } from './lib';

console.log(sayHello('John'));
```

This is a basic overview of TypeScript. You can dive deeper into the language by exploring advanced topics like Decorators, Mixins, and Advanced Types. The [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) is a great resource for learning more about TypeScript.
