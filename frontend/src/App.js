import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [packages, setPackages] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // Form states
  const [showCreateForm, setShowCreateForm] = useState(false);
  const [showEditForm, setShowEditForm] = useState(false);
  const [showLocationForm, setShowLocationForm] = useState(false);
  const [selectedPackage, setSelectedPackage] = useState(null);
  const [showLocationHistory, setShowLocationHistory] = useState(false);
  
  // Form states
  const [createForm, setCreateForm] = useState({
    shipping_date: '',
    status: 'Pending',
    destination: '',
    weight: ''
  });
  
  const [editForm, setEditForm] = useState({
    shipping_date: '',
    status: '',
    destination: '',
    weight: ''
  });
  
  const [locationForm, setLocationForm] = useState({
    location: '',
    registration_date: ''
  });

  // Fetch all packages
  const fetchPackages = async () => {
    try {
      setLoading(true);
      const response = await axios.get('/packages/');
      setPackages(response.data);
      setError(null);
    } catch (err) {
      setError('Error loading packages: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPackages();
  }, []);

  // Create new package
  const handleCreatePackage = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/packages/', createForm);
      setPackages([...packages, response.data]);
      setCreateForm({ shipping_date: '', status: 'Pending', destination: '', weight: '' });
      setShowCreateForm(false);
      setError(null);
    } catch (err) {
      setError('Error creating package: ' + err.message);
    }
  };

  // Update package
  const handleUpdatePackage = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.put(`/packages/${selectedPackage.id}`, editForm);
      setPackages(packages.map(pkg => 
        pkg.id === selectedPackage.id ? response.data : pkg
      ));
      setShowEditForm(false);
      setSelectedPackage(null);
      setError(null);
    } catch (err) {
      setError('Error updating package: ' + err.message);
    }
  };

  // Delete package
  const handleDeletePackage = async (id) => {
    if (window.confirm('Are you sure you want to delete this package?')) {
      try {
        await axios.delete(`/packages/${id}`);
        setPackages(packages.filter(pkg => pkg.id !== id));
        setError(null);
      } catch (err) {
        setError('Error deleting package: ' + err.message);
      }
    }
  };

  // Add location
  const handleAddLocation = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`/packages/${selectedPackage.id}/location`, locationForm);
      setLocationForm({ location: '', registration_date: '' });
      setShowLocationForm(false);
      setError(null);
      alert('Location added successfully!');
      // Reload packages to show new location
      fetchPackages();
    } catch (err) {
      setError('Error adding location: ' + err.message);
    }
  };

  // Fetch location history
  const [locationHistory, setLocationHistory] = useState([]);
  const fetchLocationHistory = async (packageId) => {
    try {
      const response = await axios.get(`/packages/${packageId}/location_history`);
      setLocationHistory(response.data);
      setShowLocationHistory(true);
      setError(null);
    } catch (err) {
      // If 404, means no history (not a real error)
      if (err.response && err.response.status === 404) {
        setLocationHistory([]);
        setShowLocationHistory(true);
        setError(null);
      } else {
        setError('Error loading history: ' + err.message);
      }
    }
  };

  // Open edit form
  const openEditForm = (package_item) => {
    setSelectedPackage(package_item);
    setEditForm({
      shipping_date: package_item.shipping_date,
      status: package_item.status,
      destination: package_item.destination,
      weight: package_item.weight.toString()
    });
    setShowEditForm(true);
  };

  // Open location form
  const openLocationForm = (package_item) => {
    setSelectedPackage(package_item);
    setLocationForm({
      location: '',
      registration_date: new Date().toISOString().split('T')[0]
    });
    setShowLocationForm(true);
  };

  // Format date
  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US');
  };

  // Get CSS class for status
  const getStatusClass = (status) => {
    switch (status.toLowerCase()) {
      case 'pending': return 'status-pending';
      case 'delivered': return 'status-delivered';
      case 'in transit': return 'status-transit';
      case 'returned': return 'status-returned';
      default: return '';
    }
  };

  // Clear error
  const clearError = () => {
    setError(null);
  };

  if (loading) {
    return (
      <div className="container">
        <div className="header">
          <h1>Package Tracking</h1>
        </div>
        <div className="section">
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container">
      <div className="header">
        <h1>📦 Package Tracking System</h1>
      </div>

      {error && (
        <div className="section" style={{ backgroundColor: '#f8d7da', border: '1px solid #f5c6cb' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <p style={{ color: '#721c24', margin: 0 }}>{error}</p>
            <button 
              onClick={clearError} 
              style={{ 
                background: 'none', 
                border: 'none', 
                color: '#721c24', 
                fontSize: '18px', 
                cursor: 'pointer',
                padding: '0 8px'
              }}
            >
              ✕
            </button>
          </div>
        </div>
      )}

      {/* Package Creation Section */}
      <div className="section">
        <h2>➕ New Package</h2>
        {!showCreateForm ? (
          <button className="btn" onClick={() => setShowCreateForm(true)}>
            Create New Package
          </button>
        ) : (
          <form onSubmit={handleCreatePackage}>
            <div className="form-row">
              <div className="form-group">
                <label>Shipping Date:</label>
                <input
                  type="date"
                  value={createForm.shipping_date}
                  onChange={(e) => setCreateForm({...createForm, shipping_date: e.target.value})}
                  required
                />
              </div>
              <div className="form-group">
                <label>Status:</label>
                <select
                  value={createForm.status}
                  onChange={(e) => setCreateForm({...createForm, status: e.target.value})}
                  required
                >
                  <option value="Pending">Pending</option>
                  <option value="In Transit">In Transit</option>
                  <option value="Delivered">Delivered</option>
                  <option value="Returned">Returned</option>
                </select>
              </div>
              <div className="form-group">
                <label>Destination:</label>
                <input
                  type="text"
                  value={createForm.destination}
                  onChange={(e) => setCreateForm({...createForm, destination: e.target.value})}
                  placeholder="Destination address"
                  required
                />
              </div>
              <div className="form-group">
                <label>Weight (kg):</label>
                <input
                  type="number"
                  step="0.01"
                  value={createForm.weight}
                  onChange={(e) => setCreateForm({...createForm, weight: e.target.value})}
                  placeholder="0.00"
                  required
                />
              </div>
            </div>
            <div className="actions">
              <button type="submit" className="btn btn-success">Create Package</button>
              <button type="button" className="btn btn-danger" onClick={() => setShowCreateForm(false)}>
                Cancel
              </button>
            </div>
          </form>
        )}
      </div>

      {/* Package List */}
      <div className="section">
        <h2>📋 Package List ({packages.length})</h2>
        {packages.length === 0 ? (
          <p>No packages found.</p>
        ) : (
          packages.map(package_item => (
            <div key={package_item.id} className="package-card">
              <h3>Package #{package_item.id}</h3>
              <div className="package-info">
                <div className="info-item">
                  <div className="info-label">Shipping Date</div>
                  <div className="info-value">{formatDate(package_item.shipping_date)}</div>
                </div>
                <div className="info-item">
                  <div className="info-label">Status</div>
                  <div className={`info-value ${getStatusClass(package_item.status)}`}>
                    {package_item.status}
                  </div>
                </div>
                <div className="info-item">
                  <div className="info-label">Destination</div>
                  <div className="info-value">{package_item.destination}</div>
                </div>
                <div className="info-item">
                  <div className="info-label">Weight</div>
                  <div className="info-value">{package_item.weight} kg</div>
                </div>
              </div>
              <div className="actions">
                <button 
                  className="btn" 
                  onClick={() => openEditForm(package_item)}
                >
                  ✏️ Edit
                </button>
                <button 
                  className="btn btn-success" 
                  onClick={() => openLocationForm(package_item)}
                >
                  📍 Add Location
                </button>
                <button 
                  className="btn" 
                  onClick={() => fetchLocationHistory(package_item.id)}
                >
                  🗺️ View History
                </button>
                <button 
                  className="btn btn-danger" 
                  onClick={() => handleDeletePackage(package_item.id)}
                >
                  🗑️ Delete
                </button>
              </div>
            </div>
          ))
        )}
      </div>

      {/* Edit Modal */}
      {showEditForm && selectedPackage && (
        <div className="section" style={{ backgroundColor: '#fff3cd', border: '1px solid #ffeaa7' }}>
          <h2>✏️ Edit Package #{selectedPackage.id}</h2>
          <form onSubmit={handleUpdatePackage}>
            <div className="form-row">
              <div className="form-group">
                <label>Shipping Date:</label>
                <input
                  type="date"
                  value={editForm.shipping_date}
                  onChange={(e) => setEditForm({...editForm, shipping_date: e.target.value})}
                  required
                />
              </div>
              <div className="form-group">
                <label>Status:</label>
                <select
                  value={editForm.status}
                  onChange={(e) => setEditForm({...editForm, status: e.target.value})}
                  required
                >
                  <option value="Pending">Pending</option>
                  <option value="In Transit">In Transit</option>
                  <option value="Delivered">Delivered</option>
                  <option value="Returned">Returned</option>
                </select>
              </div>
              <div className="form-group">
                <label>Destination:</label>
                <input
                  type="text"
                  value={editForm.destination}
                  onChange={(e) => setEditForm({...editForm, destination: e.target.value})}
                  required
                />
              </div>
              <div className="form-group">
                <label>Weight (kg):</label>
                <input
                  type="number"
                  step="0.01"
                  value={editForm.weight}
                  onChange={(e) => setEditForm({...editForm, weight: e.target.value})}
                  required
                />
              </div>
            </div>
            <div className="actions">
              <button type="submit" className="btn btn-success">Update Package</button>
              <button type="button" className="btn btn-danger" onClick={() => setShowEditForm(false)}>
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Add Location Modal */}
      {showLocationForm && selectedPackage && (
        <div className="section" style={{ backgroundColor: '#d1ecf1', border: '1px solid #bee5eb' }}>
          <h2>📍 Add Location - Package #{selectedPackage.id}</h2>
          <form onSubmit={handleAddLocation}>
            <div className="form-row">
              <div className="form-group">
                <label>Location:</label>
                <input
                  type="text"
                  value={locationForm.location}
                  onChange={(e) => setLocationForm({...locationForm, location: e.target.value})}
                  placeholder="Ex: São Paulo Distribution Center"
                  required
                />
              </div>
              <div className="form-group">
                <label>Registration Date:</label>
                <input
                  type="date"
                  value={locationForm.registration_date}
                  onChange={(e) => setLocationForm({...locationForm, registration_date: e.target.value})}
                  required
                />
              </div>
            </div>
            <div className="actions">
              <button type="submit" className="btn btn-success">Add Location</button>
              <button type="button" className="btn btn-danger" onClick={() => setShowLocationForm(false)}>
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      {/* Location History */}
      {showLocationHistory && (
        <div className="section" style={{ backgroundColor: '#e8f5e8', border: '1px solid #c3e6c3' }}>
          <h2>🗺️ Location History</h2>
          {locationHistory.length === 0 ? (
            <p>No locations registered for this package.</p>
          ) : (
            locationHistory.map(location => (
              <div key={location.id} className="location-item">
                <strong>{location.location}</strong>
                <div className="data">{formatDate(location.registration_date)}</div>
              </div>
            ))
          )}
          <button 
            className="btn" 
            onClick={() => setShowLocationHistory(false)}
            style={{ marginTop: '15px' }}
          >
            Close History
          </button>
        </div>
      )}
    </div>
  );
}

export default App;
