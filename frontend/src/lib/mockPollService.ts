// Mock poll service using localStorage for immediate functionality
// This allows polls to work without Firebase configuration
// Note: This is a temporary solution - polls only work on the same browser

interface PollData {
    id: string;
    question: string;
    created_at: string;
    is_active: boolean;
}

interface PollResponse {
    studentName: string;
    answer: 'yes' | 'no';
    timestamp: string;
}

class MockPollService {
    private pollKey = 'mastery_ai_active_poll';
    private responsesKey = 'mastery_ai_poll_responses';
    private listeners: Map<string, Set<(data: any) => void>> = new Map();
    private pollInterval: number | null = null;

    constructor() {
        // Start polling for changes every 500ms
        this.startPolling();
    }

    private startPolling() {
        if (this.pollInterval) return;

        this.pollInterval = setInterval(() => {
            this.notifyListeners();
        }, 500);
    }

    private notifyListeners() {
        // Notify poll listeners
        const pollListeners = this.listeners.get(this.pollKey);
        if (pollListeners) {
            const pollData = this.getActivePoll();
            pollListeners.forEach(callback => callback(pollData));
        }

        // Notify response listeners
        const responseListeners = this.listeners.get(this.responsesKey);
        if (responseListeners) {
            const responses = this.getResponses();
            responseListeners.forEach(callback => callback(responses));
        }
    }

    // Subscribe to poll changes
    onValue(key: string, callback: (data: any) => void): () => void {
        if (!this.listeners.has(key)) {
            this.listeners.set(key, new Set());
        }
        this.listeners.get(key)!.add(callback);

        // Immediately call with current data
        if (key === this.pollKey) {
            callback(this.getActivePoll());
        } else if (key === this.responsesKey) {
            callback(this.getResponses());
        }

        // Return unsubscribe function
        return () => {
            const listeners = this.listeners.get(key);
            if (listeners) {
                listeners.delete(callback);
            }
        };
    }

    // Set active poll
    setActivePoll(poll: PollData | null) {
        if (poll) {
            localStorage.setItem(this.pollKey, JSON.stringify(poll));
        } else {
            localStorage.removeItem(this.pollKey);
        }
        this.notifyListeners();
    }

    // Get active poll
    getActivePoll(): PollData | null {
        const data = localStorage.getItem(this.pollKey);
        return data ? JSON.parse(data) : null;
    }

    // Add response
    addResponse(response: PollResponse) {
        const responses = this.getResponses();
        responses.push(response);
        localStorage.setItem(this.responsesKey, JSON.stringify(responses));
        this.notifyListeners();
    }

    // Get all responses
    getResponses(): PollResponse[] {
        const data = localStorage.getItem(this.responsesKey);
        return data ? JSON.parse(data) : [];
    }

    // Clear responses
    clearResponses() {
        localStorage.removeItem(this.responsesKey);
        this.notifyListeners();
    }

    // Clear all poll data
    clearAll() {
        localStorage.removeItem(this.pollKey);
        localStorage.removeItem(this.responsesKey);
        this.notifyListeners();
    }
}

// Create singleton instance
export const mockPollService = new MockPollService();

// Mock Firebase-like API
export const mockDb = {
    ref: (path: string) => ({
        path,
        set: async (data: any) => {
            if (path === 'polls/active') {
                mockPollService.setActivePoll(data);
            }
        },
        remove: async () => {
            if (path === 'polls/active') {
                mockPollService.setActivePoll(null);
            } else if (path === 'polls/active/responses') {
                mockPollService.clearResponses();
            }
        },
        push: async (data: any) => {
            if (path === 'polls/active/responses') {
                mockPollService.addResponse(data);
            }
        }
    })
};

export const mockOnValue = (ref: any, callback: (snapshot: any) => void) => {
    const unsubscribe = mockPollService.onValue(
        ref.path === 'polls/active' ? 'mastery_ai_active_poll' : 'mastery_ai_poll_responses',
        (data) => {
            callback({
                val: () => data,
                exists: () => data !== null
            });
        }
    );
    return unsubscribe;
};
