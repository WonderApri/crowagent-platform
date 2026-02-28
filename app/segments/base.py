"""
Defines the base class for all customer segments.
"""
from abc import ABC, abstractmethod
import streamlit as st

class Segment(ABC):
    """
    An abstract base class for customer segments.
    """
    def __init__(self, name):
        self.name = name

    def render(self):
        """
        Renders the main content area for the segment.
        """
        st.header(f"Segment: {self.name}")
        
        # Create a tab layout
        tab1, tab2, tab3 = st.tabs(["Data Input", "Analysis", "Recommendations"])

        with tab1:
            self.render_data_input_tab()
        with tab2:
            self.render_analysis_tab()
        with tab3:
            self.render_recommendations_tab()

    @abstractmethod
    def render_data_input_tab(self):
        """
        Renders the content for the 'Data Input' tab.
        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def render_analysis_tab(self):
        """
        Renders the content for the 'Analysis' tab.
        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def render_recommendations_tab(self):
        """
        Renders the content for the 'Recommendations' tab.
        This method must be implemented by subclasses.
        """
        pass
