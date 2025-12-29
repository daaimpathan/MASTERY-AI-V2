export interface RubricCriterion {
    criterion_name: string;
    max_score: number;
    weight: number;
    description: string;
}

export interface Rubric {
    id: string;
    name: string;
    description: string;
    criteria: RubricCriterion[];
}
