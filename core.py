# Core module for Open Data Pipeline Ky5J

class DataPipeline:
    """Main data processing pipeline class."""
    
    def __init__(self):
        self.steps = []
    
    def add_step(self, step):
        """Add a processing step to the pipeline."""
        self.steps.append(step)
    
    def run(self, data):
        """Run the pipeline on the input data."""
        result = data
        for step in self.steps:
            result = step(result)
        return result
