export declare const languages: Set<string>;
export declare function getName(champId: number, lang?: string): string;
export declare function getChampion(name: string, lang?: string): object;
export declare function getId(name: string, lang?: string): number;
export declare function all(lang?: string): Array<string>;
export declare function random(lang?: string): string;
