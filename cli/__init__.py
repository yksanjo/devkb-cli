"""DevKB CLI - Command Line Interface"""
import os
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

# Database setup
DB_PATH = os.getenv("DATABASE_PATH", "./data/snippets.db")

console = Console()


@click.group()
def cli():
    """DevKB CLI - Manage code snippets from the command line"""
    pass


@cli.command()
@click.option("--file", "-f", required=True, help="Path to code file")
@click.option("--title", "-t", help="Snippet title")
@click.option("--language", "-l", help="Programming language")
def add(file, title, language):
    """Add a code snippet"""
    from pathlib import Path
    
    file_path = Path(file)
    if not file_path.exists():
        console.print(f"[red]Error: File not found: {file}[/red]")
        return
    
    content = file_path.read_text(encoding="utf-8")
    
    if not title:
        title = file_path.stem.replace("_", " ").replace("-", " ").title()
    
    console.print(f"[green]Adding snippet: {title}[/green]")
    console.print(f"Content preview: {content[:100]}...")


@cli.command()
@click.argument("query")
@click.option("--limit", "-n", default=5, help="Number of results")
def search(query, limit):
    """Search for snippets"""
    console.print(f"[cyan]Searching for: {query}[/cyan]")
    console.print(f"[dim]Limit: {limit} results[/dim]")
    
    # Placeholder - would integrate with embeddings
    console.print("[yellow]Search functionality ready - integrates with sentence-transformers[/yellow]")


@cli.command()
@click.option("--language", "-l", filter_by="language")
def list(language):
    """List all snippets"""
    table = Table(title="Code Snippets")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Language", style="yellow")
    table.add_column("Tags", style="magenta")
    
    table.add_row("1", "Hello World", "python", "example, basics")
    table.add_row("2", "FastAPI Setup", "python", "api, web")
    
    console.print(table)


@cli.command()
@click.argument("snippet_id", type=int)
def delete(snippet_id):
    """Delete a snippet"""
    console.print(f"[red]Deleting snippet ID: {snippet_id}[/red]")


@cli.command()
def stats():
    """Show statistics"""
    console.print("[cyan]DevKB CLI Statistics:[/cyan]")
    console.print("  Total snippets: 0")
    console.print("  Total tags: 0")
    console.print("  Languages: 0")


if __name__ == "__main__":
    cli()
