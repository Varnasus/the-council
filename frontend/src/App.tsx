import React, { useState } from 'react';
import { 
  Container, 
  TextField, 
  Button, 
  Typography, 
  Paper,
  Box,
  Grid
} from '@mui/material';
import axios from 'axios';

interface Solution {
  analysis: Record<string, any>;
  solution: Record<string, any>;
}

interface Results {
  [key: string]: Solution;
}

const App: React.FC = () => {
  const [problem, setProblem] = useState('');
  const [results, setResults] = useState<Results | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!problem.trim()) return;

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/api/solve', { problem });
      setResults(response.data);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          AI Arena
        </Typography>
        
        <Paper elevation={3} sx={{ p: 3, mb: 4 }}>
          <TextField
            fullWidth
            multiline
            rows={4}
            variant="outlined"
            label="Enter your problem statement"
            value={problem}
            onChange={(e) => setProblem(e.target.value)}
            sx={{ mb: 2 }}
          />
          <Button
            variant="contained"
            color="primary"
            onClick={handleSubmit}
            disabled={loading || !problem.trim()}
            fullWidth
          >
            {loading ? 'Solving...' : 'Solve Problem'}
          </Button>
        </Paper>

        {results && (
          <Grid container spacing={3}>
            {Object.entries(results).map(([agent, solution]) => (
              <Grid item xs={12} md={4} key={agent}>
                <Paper elevation={3} sx={{ p: 3 }}>
                  <Typography variant="h5" gutterBottom>
                    {agent}
                  </Typography>
                  
                  <Typography variant="h6" gutterBottom>
                    Analysis:
                  </Typography>
                  <Box sx={{ mb: 2 }}>
                    {Object.entries(solution.analysis).map(([key, value]) => (
                      <Typography key={key} variant="body2">
                        <strong>{key}:</strong> {JSON.stringify(value)}
                      </Typography>
                    ))}
                  </Box>

                  <Typography variant="h6" gutterBottom>
                    Solution:
                  </Typography>
                  <Box>
                    {Object.entries(solution.solution).map(([key, value]) => (
                      <Typography key={key} variant="body2">
                        <strong>{key}:</strong> {JSON.stringify(value)}
                      </Typography>
                    ))}
                  </Box>
                </Paper>
              </Grid>
            ))}
          </Grid>
        )}
      </Box>
    </Container>
  );
};

export default App; 