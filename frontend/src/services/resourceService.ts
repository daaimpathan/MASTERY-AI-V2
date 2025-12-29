/**
 * Resource API Service
 * Handles all resource-related API calls
 */

import axios from 'axios';
import type {
    Resource,
    ResourceRequest,
    ResourceCreateData,
    ResourceUpdateData,
    ResourceRequestCreateData,
    ResourceRequestActionData,
} from '../types/resource';

const API_BASE_URL = '/api/v1';

// Get auth token from localStorage
const getAuthToken = () => {
    return localStorage.getItem('access_token');
};

// Create axios instance with auth header
const createAuthHeaders = () => ({
    headers: {
        Authorization: `Bearer ${getAuthToken()}`,
    },
});

// Resource API calls

export const fetchResources = async (): Promise<Resource[]> => {
    const response = await axios.get(`${API_BASE_URL}/resources`, createAuthHeaders());
    return response.data;
};

export const createResource = async (data: ResourceCreateData): Promise<Resource> => {
    const formData = new FormData();
    formData.append('title', data.title);
    formData.append('type', data.type);
    formData.append('class_id', data.class_id);

    if (data.description) {
        formData.append('description', data.description);
    }
    if (data.url) {
        formData.append('url', data.url);
    }
    if (data.content) {
        formData.append('content', data.content);
    }
    if (data.file) {
        formData.append('file', data.file);
    }

    const response = await axios.post(`${API_BASE_URL}/resources`, formData, {
        headers: {
            Authorization: `Bearer ${getAuthToken()}`,
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};

export const getResource = async (id: string): Promise<Resource> => {
    const response = await axios.get(`${API_BASE_URL}/resources/${id}`, createAuthHeaders());
    return response.data;
};

export const updateResource = async (
    id: string,
    data: ResourceUpdateData
): Promise<Resource> => {
    const response = await axios.put(
        `${API_BASE_URL}/resources/${id}`,
        data,
        createAuthHeaders()
    );
    return response.data;
};

export const deleteResource = async (id: string): Promise<void> => {
    await axios.delete(`${API_BASE_URL}/resources/${id}`, createAuthHeaders());
};

// Resource Request API calls

export const createResourceRequest = async (
    data: ResourceRequestCreateData
): Promise<ResourceRequest> => {
    const response = await axios.post(
        `${API_BASE_URL}/resources/requests`,
        data,
        createAuthHeaders()
    );
    return response.data;
};

export const fetchResourceRequests = async (): Promise<ResourceRequest[]> => {
    const response = await axios.get(
        `${API_BASE_URL}/resources/requests`,
        createAuthHeaders()
    );
    return response.data;
};

export const approveRequest = async (
    id: string,
    data: ResourceRequestActionData
): Promise<ResourceRequest> => {
    const response = await axios.put(
        `${API_BASE_URL}/resources/requests/${id}/approve`,
        data,
        createAuthHeaders()
    );
    return response.data;
};

export const rejectRequest = async (
    id: string,
    data: ResourceRequestActionData
): Promise<ResourceRequest> => {
    const response = await axios.put(
        `${API_BASE_URL}/resources/requests/${id}/reject`,
        data,
        createAuthHeaders()
    );
    return response.data;
};
